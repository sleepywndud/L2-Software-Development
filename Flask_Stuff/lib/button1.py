from imports import *

counter = 0


@app.route("/", methods=["POST"])
def button1():
    global counter

    if request.method == "POST":
        if "button1" in request.form:
            counter += 1

    return render_template("index.html", counter=counter)
