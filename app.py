from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.debug = True
app.secret_key = "youcantguessthis123"
@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["post", "get"])
def greet():
    flash("Hi "+str(request.form['name_input'])+ ", nice to meet you!")
    return render_template("index.html")

