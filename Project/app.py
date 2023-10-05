from flask import Flask, render_template ,url_for
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/index.html")
def logo():
    return render_template("index.html")
@app.route("/maths.html")
def math():
    return render_template("maths.html")
@app.route("/ds.html")
def ds():
    return render_template("ds.html")
@app.route("/dbms.html")
def dbms():
    return render_template("dbms.html")
@app.route("/vr.html")
def vr():
    return render_template("vr.html")
@app.route("/py.html")
def py():
    return render_template("py.html")
@app.route("/dlca.html")
def dlca():
    return render_template("dlca.html")
@app.route("/hvse.html")
def hvse():
    return render_template("hvse.html")
@app.route("/dashboard.html")
def dashboard():
    return render_template("dashboard.html")
@app.route("/login_submit.php")
def lsubmit():
    return render_template("login_submit.php")
@app.route("/signup_submit.php")
def ssubmit():
    return render_template("signup_submit.php")
@app.route("/database_connect.php")
def db():
    return render_template("database_connect.php")

app.run(debug=True)
