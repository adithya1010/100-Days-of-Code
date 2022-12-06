from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

# Get all H3s

all_movies_title = soup.find_all(name="h3", class_="title")
# print(all_movies_title)

# Getting the title of each H3 and forming a list of all titles
movie_titles = [movie.getText() for movie in all_movies_title]
# Reversing the list using reverse()
movie_titles.reverse()
print(movie_titles)

# Writing the top 100 movies to a file called movies.txt
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")


