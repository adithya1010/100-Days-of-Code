from bs4 import BeautifulSoup
import requests

# Getting HTML code of ycombinator website using API request
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text



soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

article = soup.find(name="span", class_="titleline")
article_tag = article.a
# print(article_tag)

article_text = article_tag.getText()
print(article_text)


# Getting the link and no of upvotes from the first link
article_link = article_tag.get("href")
print(article_link)
article_upvote = soup.find(name="span", class_="score").getText()
print(article_upvote)

















































# import lxml
#
# # Reading the website
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# # Parsing and displaying title with Soup
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# # Finding all anchor tags
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
#
# # Get all anchor tags
#
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
#
# # Get heading with id name
# name_heading = soup.find(name="h1", id="name")
# # print(name_heading)
#
# # Get heading with class heading
#
# heading_heading = soup.find(name="h3", class_="heading")
# # print(heading_heading.text)
#
#
# # Select one a tag where it has p and a CSS selectors
# company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# # Select one tag which has the id name
# name_id = soup.select_one(selector="#name")
# print(name_id)
#
# # Select one tag which has the class heading
# heading_class = soup.select_one(selector=".heading")
# print(heading_class)

