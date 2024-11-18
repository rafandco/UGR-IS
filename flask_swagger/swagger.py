from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/multiply', methods=['POST'])
def multiply_two_numbers():
    """
    Multiplies two numbers provided as query parameters
    ---
    parameters:
      - name: number1
        in: query
        type: number
        required: true
      - name: number2
        in: query
        type: number
        required: true
    responses:
      200:
        description: The result of the multiplication
    """
    num1 = float(request.args.get("number1"))
    num2 = float(request.args.get("number2"))
    multiplication_result = num1 * num2
    return jsonify({"result": multiplication_result})

if __name__ == '__main__' :
    app.run()