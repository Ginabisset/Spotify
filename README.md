# Spotify
Takes a date input in the format 'YYYY-MM-DD', web scrapes the Billboard 100 songs at that date and creates a Spotify playlist containing those songs 

Please first create a Spotify developer app here:
https://developer.spotify.com/dashboard

This will give you the following details to set these environment variables:

os.environ['SPOTIPY_CLIENT_ID'] # On the app > Settings > Client ID
os.environ['SPOTIPY_CLIENT_SECRET'] # On the app > Settings > Client Secret
os.environ['SPOTIPY_REDIRECT_URI'] # your redirect URI when setting up the Spotify app
os.environ['USER_ID'] # your Spotify username (str)


To run the code, please use the spotify.py file. 

Also, please note, if the search query cannot find the song it will skip it. 
