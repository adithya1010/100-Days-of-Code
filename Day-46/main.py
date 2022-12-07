from bs4 import BeautifulSoup
import requests
from pprint import pprint
# Getting the year from the user
import spotipy
from spotipy.oauth2 import SpotifyOAuth
date = input("Which year do you want to travel to? Type the date in this form YYYY-MM-DD:")

# Using BeautifulSoup to scrape the site

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [song.getText().strip("\n\t") for song in song_names]
pprint(song_list)



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="0db6ad16291a4e87883b97ebf9845d23",
        client_secret="d35ddba917604dba82e683ded65cbf97",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
