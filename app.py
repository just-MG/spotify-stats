import dataFetch

def startUp():
    print("Welcome to Spotify Stats!")


if __name__ == "__main__":
    call = dataFetch.caller()
    print(call.getTopTracks()[:4])
    print(call.getTopArtists()[:4])
