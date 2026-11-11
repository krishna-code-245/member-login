import os
from datetime import date

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def connect_to_database():
    if os.environ.get("RENDER") == "true":
        required_variables = (
            "MYSQLHOST",
            "MYSQLPORT",
            "MYSQLUSER",
            "MYSQLPASSWORD",
            "MYSQLDATABASE",
        )
        missing_variables = [
            name for name in required_variables if not os.environ.get(name)
        ]
        if missing_variables:
            raise ValueError(
                "Missing required Render environment variables: "
                + ", ".join(missing_variables)
            )

    ssl_ca = os.environ.get("MYSQL_SSL_CA")
    return mysql.connector.connect(
        host=os.environ.get("MYSQLHOST", "localhost"),
        port=int(os.environ.get("MYSQLPORT", "3306")),
        user=os.environ.get("MYSQLUSER", "root"),
        password=os.environ.get("MYSQLPASSWORD", ""),
        database=os.environ.get("MYSQLDATABASE", "gym_db"),
        connection_timeout=10,
        ssl_ca=ssl_ca,
        ssl_verify_cert=bool(ssl_ca),
    )


def database_error_response(message):
    return render_template("error.html", message=message), 503


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/member-login")
def member_login():
    member_id = request.form.get("member_id", "").strip()
    if not member_id:
        return render_template("error.html", message="Enter a membership ID."), 400

    connection = None
    try:
        connection = connect_to_database()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT member_id, member_name, membership_type, expiry_date "
                "FROM members WHERE member_id = %s",
                (member_id,),
            )
            member = cursor.fetchone()
    except (mysql.connector.Error, ValueError):
        app.logger.exception("Member lookup failed; check the Render MySQL settings and members table.")
        return database_error_response(
            "The member database is temporarily unavailable. Please try again later."
        )
    finally:
        if connection is not None:
            connection.close()

    if member is not None:
        days_left = (member["expiry_date"] - date.today()).days
        return render_template("profile.html", member=member, days_left=days_left)

    return render_template(
        "error.html",
        message="Membership ID not found. Check the ID and try again.",
    ), 404


@app.get("/health")
def health():
    connection = None
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM members LIMIT 1")
    except (mysql.connector.Error, ValueError):
        app.logger.exception("Database health check failed; check the Render MySQL settings and members table.")
        return {
            "status": "error",
            "message": "Database unavailable. Check Render MySQL settings and the members table.",
        }, 503
    finally:
        if connection is not None:
            connection.close()

    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
