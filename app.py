from flask import Flask, render_template, request, jsonify, session, redirect, url_for # type: ignore
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "AI_ZOZ_SECRET"
app.permanent_session_lifetime = timedelta(minutes=10)

# بيانات المستخدمين الافتراضية
users = {"admin": "1234", "zoz": "ai2025"}

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        session["user"] = username
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Invalid username or password"})

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("dashboard.html", user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
