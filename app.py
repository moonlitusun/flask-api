from src import formula_group
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return [{"a": 1}]


formula_group.run(app)


# if __name__ == "__main__":
#     app.run(debug=True)
