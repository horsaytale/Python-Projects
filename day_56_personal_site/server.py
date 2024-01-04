from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("astral.html")
# As long as the amber file is under template, there's no need to locate the file unless it
# is under another directory, then has to use a path
if __name__=="__main__":
    app.run(debug=True)