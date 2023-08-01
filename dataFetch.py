import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

class caller:
    load_dotenv()
    SPOTIPY_CLIENT_ID=os.getenv('CLIENT_ID')
    SPOTIPY_CLIENT_SECRET=os.getenv('CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI='http://127.0.0.1:1919'
    SCOPE = 'user-top-read'

    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.SPOTIPY_CLIENT_ID, client_secret=self.SPOTIPY_CLIENT_SECRET, redirect_uri=self.SPOTIPY_REDIRECT_URI, scope=self.SCOPE))

    def getTopTracks(self):
        results = self.sp.current_user_top_tracks(limit=5)
        answers = []
        for idx, item in enumerate(results['items']):
            answers.append(f"{idx+1} {item['name']} // {item['artists'][0]['name']}")
        return answers
        

    def getTopArtists(self):
        results = self.sp.current_user_top_artists(limit=5)
        answers = []
        for idx, item in enumerate(results['items']):
            answers.append(f"{idx+1} {item['name']}")
        return answers
    

