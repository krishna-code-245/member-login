from flask import Flask, render_template, request
from datetime import date
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gym_db"
)

cursor = db.cursor(dictionary=True)

@app.route("/")
def home():
    return render_template("index.html", member=None)

@app.route("/member-login", methods=["POST"])
def member_login():

    member_id = request.form["member_id"]

    cursor.execute(
        "SELECT * FROM members WHERE member_id=%s",
        (member_id,)
    )

    member = cursor.fetchone()

    if member:

        days_left = (
            member["expiry_date"] - date.today()
        ).days

        return render_template("profile.html", member=member, days_left=days_left)

    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)