from imports import *


@app.route("/")
def main():
    return render_template("index.html", status="waiting")
