from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Product(Resource):
    """
    need to have only one endpoint that will takes to args
    """
    def get(self):
        return "Hello", 200


api.add_resource(Product,'/product')


if __name__ == '__main__':
    app.run()