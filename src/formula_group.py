from flask import request

def run(app):
    print(432234)

    @app.route("/formula-group/create", methods=["POST"])
    def create():
        data = request.get_json()

        print(data['name'])
        return [{"a": 12}]

    @app.route("/formula-group/list")
    def list():
        return [{"a": 12}]
