from flask import Flask, request
from flask_restful import Api, Resource
from preprocessing import preprocess_data
from model import ML_model as model

app = Flask(__name__)
api = Api(app)



class isAlive(Resource):
    def get(self):
        return {'message': 'The server works fine'}, 200


class Predict(Resource):
    def get(self):
        pass

    def post(self):
        get_json = request.get_json(force = True)
        if preprocess_data.check_for_errors(get_json) == "good":
            result = preprocess_data.preprocess(get_json)
            price = model.predict(result)
            return f"The price is :{price}", 200
        else:
            res = preprocess_data.check_for_errors(get_json)
            return res, 200


@app.route('/predict', methods = ['POST'])
def get_data():
    get_json = request.get_json(force=True)
    try:
        result = preprocess_data.preprocess(get_json)
        price = model.predict(result)
        return f"The price is :{price}", 200
    except:
        return "Ooops something went wrong with the required inputs, please check: https://github.com/adamflasse/Api_deployment/blob/main/README.md for more info"




api.add_resource(isAlive, "/")

#api.add_resource(Predict, '/predict')


if __name__ == "__main__":
    app.run(debug=True)
