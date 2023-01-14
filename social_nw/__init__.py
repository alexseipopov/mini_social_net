from flask import Flask, session, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwerty"

@app.route("/")
def index():
    login = "alex"
    if request.args.get("login") == login:
        session["log_in"] = "qwerty"
        return "success login"
    return "fail login"

@app.route("/logout")
def logout():
    session.pop("log_in")
    return "success logout"

@app.route("/lk")
def lk():
    if "log_in" in session:
        return "auth"
    else:
        return "unauth"