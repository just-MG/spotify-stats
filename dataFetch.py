import requests
import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
SPOTIPY_CLIENT_ID=os.getenv('CLIENT_ID')
SPOTIPY_CLIENT_SECRET=os.getenv('CLIENT_SECRET')
SPOTIPY_REDIRECT_URI='http://127.0.0.1'
SCOPE = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

results = sp.current_user_top_tracks()

print(results)