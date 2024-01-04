import requests
from bs4 import BeautifulSoup
import lxml

# URL="https://www.empireonline.com/movies/features/best-movies-2/"
# response=requests.get(URL)
# website_html=response.text

#Entire page of EMPIRE ONLINE is now rendered by JavaScript, so there are no <h3> tags in the source code
#NOTED: IF YOU'RE UNABLE TO RETRIEVE THE INFO YOU REQUIRED, a way to save the rendered HTML :-
#copy(document.querySelector('html').outerHTML) under the CONSOLE tab in the DEVELOPER TOOLS of the
#WEBSITE
WEB_FILE = "100-top-movies.html"
def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        print(f"You need to save the rendered HTML to {WEB_FILE}")
        exit()
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")

soup=read_web_file()
all_movies=soup.find_all(name="h3", class_="jsx-4245974604")
new_movies_lst=all_movies[::-1]
print(new_movies_lst)

with open("100-top-movies.txt", "w") as file:
    for movie in new_movies_lst:
        file.write(f"{str(movie.getText())}\n")


