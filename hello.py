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
@app.route("/back/<phi>/<messageSent>/")
def hello_world(phi, messageSent):
    philo = phi
    print("hello world")
    message = messageSent
    # return(json.dumps(message))
    return json.dumps(asd(message, philo))

@cross_origin() 
@app.route("/front/<phi>/<messageSent>/", methods=['POST'])
def metmessage(phi, messageSent):
    philo = phi
    print("met message")
    # return message
    userInput = messageSent
    return hello_world(phi, messageSent)

@cross_origin() 
@app.route("/message/<phi>/<messageSent>/", methods=['GET'])
def getMessage(phi, messageSent):
    philo = phi
    print("get message")
    return(hello_world(phi, messageSent))


@app.route("/")
def testing():
    return "<p>Hello, World!</p>"