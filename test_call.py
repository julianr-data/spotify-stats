## calling Spotify API with my personal credentials and Spotipy ##

# basic imports
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# setting scope
scope = "user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


top_artists = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')

print(top_artists)
