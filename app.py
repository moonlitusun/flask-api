from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return [{"a": 1}]


if __name__ == "__main__":
    print(32432)
