from flask import Flask, request
from chat import chat
from asd import asd
from flask_cors import CORS, cross_origin
import json

# @app.route('/data')
# def data():
#     # here we want to get the value of user (i.e. ?user=some-value)
#     user = request.args.get('user')

app = Flask(__name__)
CORS(app)
message = "default message"
userInput = "test"
philo = 0
@cross_origin() 
@app.route("/back/<messageSent>/")
def hello_world(messageSent):
    global message 
    global philo
    respon =  asd(message, philo)
    return json.dumps(respon)

# @cross_origin() 
# @app.route("/back/", methods=['POST'])
# def hello_world(messageSent):
#     # print("hello world", data)
#     message = request.args.get('message')
#     philo = request.args.get('philo')
#     print("message is ", message, "philo is", philo)
#     # return(json.dumps(message))
#     return json.dumps(asd(message, philo))


@cross_origin() 
@app.route("/front", methods=["POST", "GET"])
def metmessage():
    global philo
    messages = request.args.get('message')
    philo = request.args.get('philo')
    global message 
    message = messages
    return "hi"

@cross_origin() 
@app.route("/message/<messageSent>/", methods=['GET'])
def getMessage(messageSent):
    global message 
    return(hello_world(message))


@app.route("/")
def testing():
    return "<p>Hello, World!</p>"