import spotipy  
from spotipy.oauth2 import SpotifyOAuth  
  
sp_oauth = SpotifyOAuth(client_id=24f4535b2d7143a49b3ec244cfb10f8e, client_secret=8e6217241a674f34855373fb471e2af5, redirect_uri=www.clubcotton.id.au, scope=SCOPE)  
  
access_token = sp_oauth.get_access_token()  
refresh_token = sp_oauth.get_refresh_token()  