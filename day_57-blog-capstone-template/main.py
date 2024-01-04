from flask import Flask, render_template
from post import Post
import requests


all_posts=requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
# post_objects=[]
# for post in all_posts:
#     post_obj=Post(post["id"],post["title"],post["subtitle"],post["body"])
#     post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:index>')
def get_post(index):
    requested_post=None
    for post in all_posts:
        if post["id"]==index:
            requested_post=post
    return render_template("post.html", assigned_post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
