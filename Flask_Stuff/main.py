from flask import Flask

app = Flask(__name__)

WEBSITE_NAME = "Babo Bobo's Pizzaria"


@app.route("/")
def main():
    print("Hello")


if __name__ == "__main__":
    app.run(debug=True)
