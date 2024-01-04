from flask import Flask, render_template, request
import requests

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    username=request.form['username']
    password=request.form['password']
    return render_template('login.html', login_user=username,login_pass_word=password)
    #return f"<h1>Name: {username}, Password: {password}"

if __name__=="__main__":
    app.run(debug=True)