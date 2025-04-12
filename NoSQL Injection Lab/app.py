from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client['vulnsite']
users = db['users']

# Seed users if empty
if users.count_documents({}) == 0:
    users.insert_many([
        {
            "username": "admin",
            "password": "admin123",
            "role": "admin",
            "full_name": "Administrator",
            "last_login": "2025-04-09 10:00 AM"
        },
        {
            "username": "john",
            "password": "john123",
            "role": "user",
            "full_name": "John Doe",
            "last_login": "2025-04-08 2:30 PM"
        },
        {
            "username": "alice",
            "password": "alice123",
            "role": "user",
            "full_name": "Alice Smith",
            "last_login": "2025-04-07 9:15 AM"
        }
    ])

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")
        else:
            username = request.form["username"]
            password = request.form["password"]

        print(f"Received → username: {username}, password: {password}")

        # ❗ Vulnerable NoSQL query
        user = users.find_one({
            "username": username,
            "password": password
        })

        if user:
            session["user"] = {
                "username": user["username"],
                "full_name": user["full_name"],
                "role": user["role"],
                "last_login": user["last_login"]
            }
            return redirect(url_for("dashboard")), 302
        else:
            return "Login failed", 401

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
