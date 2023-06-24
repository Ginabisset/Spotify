import spotipy
import os
from web_scraping import song_titles, question

OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'


scope = "playlist-modify-private"

spotify = spotipy.oauth2.SpotifyOAuth(scope=scope)

sp = spotipy.Spotify(auth_manager=spotify)

# Create a new playlist
name = f'{question} Billboard 100'
sp.user_playlist_create(user=os.environ['USER_ID'], name=name, collaborative=False, description='', public=True)

# Get new playlist ID.
playlist_id = sp.current_user_playlists()['items'][0]['id']


# Add Billboard songs to playlist. The search could be improved by also scraping the artist.
items = []
for item in song_titles:
    result = sp.search(q=item, type='track', limit=1)
    try:
        result['tracks']['items'][0]['uri']
    except IndexError:
        item = f"track{item[8:]}"
        result = sp.search(q=item, type='track', limit=1)
        try:
            result['tracks']['items'][0]['uri']
        except IndexError:
            pass
        else:
            result = result['tracks']['items'][0]['uri']
            items.append(result)
    else:
        result = result['tracks']['items'][0]['uri']
        items.append(result)

print(items)
print(len(items))
# Adds URL encoded items to the playlist
sp.playlist_add_items(playlist_id=playlist_id, items=items, position=0)
