from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

# API SECTION & URL
API_KEY = "f08ffe98a10d163ffa8b51a9eedde113"
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMDhmZmU5OGExMGQxNjNmZmE4YjUxYTllZWRkZTExMyIsInN1YiI6IjYyMmVhN2IyNjg4Y2QwMDAxYmU1MWUzNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2h2-21LiBI1XMxTyByrFdiLVgGE2lfzk6-vDQiwToAE"
MOVIE_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE FORM
class EditForm(FlaskForm):
    new_rating = StringField(label='Your rating out of 10, e.g. 7.3')
    new_review = StringField(label='Your review')
    submit = SubmitField(label='Done')


class AddForm(FlaskForm):
    new_movie = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(300), nullable=False)


db.create_all()


# ADDED NEW MOVIE
# new_movie=Movie(title="Phone Booth", year=2002, description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to jaw-d ropping climax.",
#                 rating=7.2, ranking=10, review="My favourite caller was the caller.",
#                 img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    movie_id = request.args.get('id')
    if movie_id:
        # print(movie_id)
        ID_URL = f"https://api.themoviedb.org/3/movie/{movie_id}"
        response = requests.get(ID_URL, params={"api_key": API_KEY})
        response.raise_for_status()
        movie_data = response.json()
        new_movie = Movie(title=movie_data['original_title'], year=movie_data["release_date"][:4],
                          description=movie_data["overview"],
                          img_url=f"{MOVIE_DB_IMAGE_URL}{movie_data['poster_path']}")
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')
    movie_selected = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_selected.rating = float(form.new_rating.data)
        movie_selected.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie_selected, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        parameters = {
            "api_key": API_KEY,
            "query": form.new_movie.data
        }
        response = requests.get(MOVIE_URL, params=parameters)
        response.raise_for_status()
        movie_data = response.json()["results"]
        return render_template("select.html", movies=movie_data)
    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
