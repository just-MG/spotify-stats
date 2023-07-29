import requests
import base64

class tokenObtainer:
    userId = ""
    userSecret = ""
    apiURL = "https://accounts.spotify.com/api/token"
    def __init__(self, userId, userSecret):
        self.userId = userId
        self.userSecret = userSecret
        self.headers = {"Authorization": "Basic " + base64.b64encode((self.userId + ":" + self.userSecret).encode("ascii")).decode("ascii")}
        self.data = {"grant_type": "client_credentials"}

    def getToken(self):
        return requests.post(self.apiURL, headers=self.headers, data=self.data).json()['access_token']
    

class getTracks:
    token = ""
    def __init__(self, token):
        self.token = token
    async def fetchAPI(self, endpoint):
        link = await requests.get(url=f"https://api.spotify.com/v1/{endpoint}", headers={"Authorization": f"Bearer {self.token}"})
        return await link.json
    
    async def getTopTracks(self):
        return await self.fetchAPI("v1/me/top/tracks?time_range=short_term&limit=5")


if __name__ == "__main__":
    token = (tokenObtainer("", "").getToken())
    print(token)
    print(getTracks.getTopTracks(token))