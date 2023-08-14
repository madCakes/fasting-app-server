from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World, from flask"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {}
    
    e


if __name__== "__main__":
    app.run(debug=True)
