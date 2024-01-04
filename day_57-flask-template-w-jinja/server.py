from flask import Flask,render_template
import random
from datetime import datetime
import requests

# AGE_URL="https://api.agify.io/"
# GENDER_URL="https://api.genderize.io/"

app=Flask(__name__)

@app.route("/")
def home():
    my_name="Amber"
    current_year = datetime.now().year
    random_number=random.randint(1,10)
    return render_template("index.html", num=random_number, year=current_year, name=my_name)
# You can insert many keyword variables after the template input, as to use them in the rendered
# template

@app.route("/guess/<name>")
def guess_name(name):
    # parameters = {
    #     "name":name
    # }
    # age_response=requests.get(AGE_URL,params=parameters)
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_response.raise_for_status()
    age_data=age_response.json()
    age_value=age_data["age"]

    # gender_response = requests.get(GENDER_URL, params=parameters)
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender_value = gender_data["gender"]

    return render_template("guess.html", age=age_value,gender=gender_value,name=name)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    response=requests.get(blog_url)
    all_posts=response.json()
    return render_template("blog.html",posts=all_posts)

if __name__=='__main__':
    app.run(debug=True)