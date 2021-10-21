import pip._vendor.requests

SPOTIFY_CREATE_PLAYLIST_URL = "https://api.spotify.com/v1/users/1274420919/playlists"
ACCESS_TOKEN = "BQC49w_6iJlOAYvhmwDnCsNQeG1DTnG9iNUOG-jTRNdqdyT7eGd1X7Zlv29ccCJsF-acuMbnGuZ61LLLy26hraF-7wAeuESNzPL2gytia02oee_H-j0EUb1fb-O8yUsMQnb-XvfxPGT_ieJvn_WATzacWPiySSqTut3gSKv7r8KLiqtB2TYLpy7xPuQDzZcDWbqM02U0YH9N"

def create_playlist(name,public):
    response = pip._vendor.requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp


def main():
    playlist = create_playlist(
        name = "jammies code",
        public = False
    )

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()