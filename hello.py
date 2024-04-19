from flask import Flask
from chat import chat
from asd import asd
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)
message = "default message"
userInput = "test"
philo = 0
@cross_origin() 
@app.route("/back/<messageSent>/")
def hello_world(messageSent):
    # print("hello world", data)
    message = messageSent
    # return(json.dumps(message))
    return json.dumps(asd(message))

@cross_origin() 
@app.route("/front/<messageSent>/", methods=['POST'])
def metmessage(messageSent):
    # print("met message")
    # return message
    # userInput = messageSent
    return hello_world(messageSent)

@cross_origin() 
@app.route("/message/<messageSent>/", methods=['GET'])
def getMessage(messageSent):
    # print("get message", data)
    return(hello_world(messageSent))


@app.route("/")
def testing():
    return "<p>Hello, World!</p>"