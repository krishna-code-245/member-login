import os
from datetime import date

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def connect_to_database():
    return mysql.connector.connect(
        host=os.environ.get("MYSQLHOST", "localhost"),
        port=int(os.environ.get("MYSQLPORT", "3306")),
        user=os.environ.get("MYSQLUSER", "root"),
        password=os.environ.get("MYSQLPASSWORD", ""),
        database=os.environ.get("MYSQLDATABASE", "gym_db"),
        connection_timeout=10,
        ssl_ca=os.environ.get("MYSQL_SSL_CA"),
        ssl_verify_cert=bool(os.environ.get("MYSQL_SSL_CA")),
    )


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/member-login")
def member_login():
    member_id = request.form.get("member_id", "").strip()
    if not member_id:
        return render_template("error.html", message="Enter a membership ID."), 400

    connection = connect_to_database()
    try:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT member_id, member_name, membership_type, expiry_date "
                "FROM members WHERE member_id = %s",
                (member_id,),
            )
            member = cursor.fetchone()
    finally:
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
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
