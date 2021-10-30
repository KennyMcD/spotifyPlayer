import pip._vendor.requests
import tkinter
import tkinter.font as font
import json

USER_PLAYLIST_URL = "https://api.spotify.com/v1/users/1274420919/playlists"
CURR_PLAYING_URL = "https://api.spotify.com/v1/me/player/currently-playing"
SKIP_URL = "https://api.spotify.com/v1/me/player/next"
PREV_URL = "https://api.spotify.com/v1/me/player/previous"
DEVICE_URL = "https://api.spotify.com/v1/me/player/devices"
PLAY_URL = "https://api.spotify.com/v1/me/player/play"
PAUSE_URL = "https://api.spotify.com/v1/me/player/pause"
ACCESS_TOKEN = "BQCC8wgTrrK0bmjrsylc5ZqXgp7N-bGgwcfmOpzqyYfRj4-O__g_ug5ka_SfE0wHygPAnpkPJTiI6lfrf-L2oL3LBjlTm0PjFuWFkrQTzk00qYDKmUlMZNiqw733ZGlBlr3PotFrvBdc6KDEPLAI9H-oAzuMhJQCquNDHoUzdp8vpJ3TP4MyRgkBJwgtKUy6mxta6aRFZ7S9HKrbesQ"


def create_playlist(name, public):
    response = pip._vendor.requests.post(
        USER_PLAYLIST_URL,
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


def get_devices():
    response = pip._vendor.requests.get(
        DEVICE_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    json_resp = response.json()

    return json_resp


def next_track():
    response = get_devices()
    print(response)
    device = response.get('devices')

    try:
        device_id = device[0].get('id')
    except IndexError:
        print("No active devices available!")

    response = pip._vendor.requests.post(
        SKIP_URL,
        device_id,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
    )


def prev_track():
    response = get_devices()
    print(response)
    device = response.get('devices')
    try:
        device_id = device[0].get('id')
    except IndexError:
        print("No active devices available!")

    response = pip._vendor.requests.post(
        PREV_URL,
        device_id,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
    )


def pause_track():
    response = get_devices()
    device = response.get('devices')
    try:
        device_id = device[0].get('id')
    except IndexError:
        print("No active devices available!")

    response = pip._vendor.requests.put(
        PAUSE_URL,
        device_id,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
    )


def play_track():
    response = get_curr_track()
    item = response.get('item')
    print(item)
    uri = item.get('uri')

    pip._vendor.requests.put(
        PLAY_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={

            "uris": [uri]
        }
    )


def get_curr_track():
    response = pip._vendor.requests.get(
        CURR_PLAYING_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    json_resp = response.json()
    return json_resp

# Handle front end


def start_window():
    # Set window dimensions
    window = tkinter.Tk()
    window.geometry("350x250")
    frame = tkinter.Frame(window)

    # Entry vars
    playlistName = tkinter.StringVar()

    # Labels
    playlistLabel = tkinter.Label(window, text="Playlist Name")

    # Entries
    playlistEntry = tkinter.Entry(window, textvariable=playlistName)

    # Buttons
    playlistButton = tkinter.Button(window, text="Create Playlist", width=25,
                                    command=lambda: create_playlist(name=playlistName.get(), public=False))
    prevButton = tkinter.Button(
        window, text="⏪️", width=3, command=lambda: prev_track())
    prevButton['font'] = font.Font(size=30)
    playButton = tkinter.Button(
        window, text="⏯", width=3, command=lambda: pause_track())
    playButton['font'] = font.Font(size=30)
    nextButton = tkinter.Button(
        window, text="⏩️", width=3, command=lambda: next_track())
    nextButton['font'] = font.Font(size=30)

    frame.pack()
    playlistLabel.pack()
    playlistEntry.pack()
    playlistButton.pack()
    prevButton.pack(in_=frame, side=tkinter.LEFT)
    nextButton.pack(in_=frame, side=tkinter.RIGHT)
    playButton.pack(in_=frame, side=tkinter.RIGHT)
    window.mainloop()


def main():

    # playlist = create_playlist(
    #     name = "jammies code",
    #     public = False
    # )
    #print(f"Playlist: {playlist}")
    start_window()


if __name__ == '__main__':
    main()
