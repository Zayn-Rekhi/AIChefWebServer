from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from model import generate_recipe

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('list', type=list)


@app.route('/',methods = ['POST', 'GET'])
def predict():
    ABC = parser.parse_args()
    ingredients = [",".join(eval(request.data)['ingredients'])]

    recipe = generate_recipe(ingredients)
    print(recipe)

    return jsonify("whatever")


if __name__ == "__main__":
    app.run(debug=True)
