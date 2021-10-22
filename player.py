import pip._vendor.requests
import tkinter
import json

USER_PLAYLIST_URL = "https://api.spotify.com/v1/users/1274420919/playlists"
ACCESS_TOKEN = "BQCHBfa6h3dVQK6XpzG-dh2rffLLHf6no-baQnM5YWPcVOqkc-pgSluWakk9UUJn8VW2rWQGM3cEofi7MxqwuED_CWtf5RSMUxZhs9repx8PTWNVgeUKeDDM3M1iX7LX-3TOZG4nWfbZKnHUigJjTliWdiT6V6gHN4ggdSlmzkM3qX3ta7ETMS81TCkqgn6Jfz7fHWqx1rkh"

def create_playlist(name,public):
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
    button = tkinter.Button(window, text= "Create Playlist", width=25, command=lambda : create_playlist(name= playlistName.get() ,public= False))
    
    frame.pack()
    playlistLabel.pack()
    playlistEntry.pack()
    button.pack()
   
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