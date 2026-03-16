from flask import Flask, render_template, request

app = Flask(__name__)

WEBSITE_NAME = "Babo Bobo's Pizzaria"


@app.route(
    "/",
)
def main():
    return render_template("index.html", status="waiting")


@app.route("/", methods=["POST"])
def button1():
    status = "waiting"
    if request.method == "POST":
        if "button1" in request.form:
            status = "clicked"
        elif "button2" in request.form:
            status = "waiting(reset)"

    return render_template("index.html", status=status)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
