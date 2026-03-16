from imports import *


@app.route("/", methods=["POST"])
def button1():
    status = "waiting"  # set initial (when file ran) status to "waiting"
    if request.method == "POST":  # buttons are done through requests
        if "button1" in request.form:
            status = "clicked"  # change status when value=button1 clicked in html
        elif "button2" in request.form:
            status = "waiting(reset)"  # "

    return render_template("index.html", status=status)  # sends everything to render
