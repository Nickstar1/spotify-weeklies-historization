import requests
import json
import base64 

class SpotifyClient:
    def __init__(self, refresh_token, client_id, client_secret, user_id):
        self.authorization = str(base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')), 'utf-8')
        self.api_token = self.get_auth_token(refresh_token)
        self.user_id = user_id


    def get_auth_token(self, refresh_token):
        url = 'https://accounts.spotify.com/api/token'
        response = requests.post(
            url, 
            headers={
                'Authorization': f'Basic {self.authorization}'
            }, 
            data={
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token
            }
        )
        return response.json()['access_token']


    def get_playlist_tracks(self, playlist_id):
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}?fields=tracks.items(track(uri))' 
        response = requests.get(
            url,
            headers={
                'Authorization': f'Bearer {self.api_token}'
            }
        )
        return [track['track']['uri'] for track in response.json()['tracks']['items']]
        
    
    def add_tracks_to_playlist(self, playlist_id, track_list):
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
        response = requests.post(
            url,
            headers={
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json'
            },
            data=json.dumps({
                'uris': track_list
            })
        )
        return response.json()


    def get_all_playlists(self):
        url = 'https://api.spotify.com/v1/me/playlists'
        response = requests.get(
            url,
            headers={
                'Authorization': f'Bearer {self.api_token}'
            }
        )
        return response.json()['items']
        