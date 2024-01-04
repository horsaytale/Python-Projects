from flask import Flask, render_template, request
import requests
import datetime
import smtplib

my_email="texperiment660@gmail.com"
password="g3tScr3w3dm8#d3Ad"

app=Flask(__name__)
all_posts=requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route("/")
def home():
    time=datetime.datetime.today().date()
    my_name="Amber"
    return render_template("index.html", posts=all_posts, name=my_name, time_now=time)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method=='POST':
        data = request.form
        name=data['name']
        email=data['email']
        phone=data['phone']
        message=data['message']
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="experi121te89@yahoo.com",
                                msg=f"Subject:Hello\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def get_post(index):
    requested_post=None
    for post in all_posts:
        if post['id']==index:
            requested_post=post
    return render_template('post.html', assigned_post=requested_post)

if __name__=="__main__":
    app.run(debug=True)


# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == "POST":
#         data = request.form
#         data = request.form
#         send_email(data["name"], data["email"], data["phone"], data["message"])
#         return render_template("contact.html", msg_sent=True)
#     return render_template("contact.html", msg_sent=False)
#
#
# def send_email(name, email, phone, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(OWN_EMAIL, OWN_PASSWORD)
#         connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)