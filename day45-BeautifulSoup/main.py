# NOTE TO PUT /ROBOTS.TXT FOR EVERY WEBSITE U WANT TO SCRAPE DATA FROM
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web = response.text

soup = BeautifulSoup(yc_web, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
print(articles)

article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get('href'))
article_upvotes = [int(article.getText().split()[0]) for article in soup.find_all(name="span", class_="score")]
print(article_upvotes)
print(article_texts)
print(article_links)

max_index = article_upvotes.index(max(article_upvotes))
# print(article_texts[max_index])
# print(article_links[max_index])
# print(article_upvotes[max_index])

# import lxml

# with open("website.html", encoding="utf8") as file:
#     contents=file.read()
#
# soup=BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
# # print(soup.p)
# # print(soup.li)
# all_anchor_tag=soup.find_all(name="a")
# print(all_anchor_tag)
# # all_p=soup.find_all(name="p")
# # print(all_p)
#
#
# # for tag in all_anchor_tag:
# #     To retrieve all text under anchor tags
# #     print(tag.getText())
# #     print(tag.get('href'))
#
# heading=soup.find(name="h1", id="name")
# print(heading)
#
# section_heading=soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# #to retrieve info based on selectors eg. body p a
# company_url=soup.select_one(selector="p a")
# print(company_url)
# #based on id selector
# name=soup.select_one(selector="#name")
# print(name)
# #based on class selector
# class_select=soup.select(".heading")
# print(class_select)
