from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

data = { 
        1: {"name": "text_1", "text": "some text"},
        2: {"name": "text2", "text": "other text"}
    }

class Data(Resource):
    def get(self, id=0):
        if id:
            return data[id], 200
        else:
            return data, 200


api.add_resource(Data, "/text", "/text/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
