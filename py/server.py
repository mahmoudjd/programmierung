# from getpass import getpass 

# user = input("Username: ")

# pw = getpass("password:")

# print(user, pw)

from flask import Flask 

app = Flask(__name__)

@app.route("/")

def index():
    return "Hi, I'm a website!"

