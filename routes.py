from . import app
from flask import render_template, request
from . import db_config

@app.route("/")
def main():
    return "Hello"


@app.route("/add_record", methods=["POST", "GET"])
def add_record():
    if request.method == "POST":
        question = request.form["question"]
        answer = request.form["answer"]
        answer2 = request.form["answer2"]
        correction = request.form["correction"]
        result = db_config.add_record(
            question=question,
            answer=answer,
            answer2=answer2,
            correction=correction
        )
        return result
    else:
        return render_template("add_record.html")