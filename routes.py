from . import app
from flask import render_template


@app.route("/")
def main():
    return "Hello"

@app.route("/add_record")
def add_record():
    return render_template("add_record.html")