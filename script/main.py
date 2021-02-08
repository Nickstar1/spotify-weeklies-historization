from spotifyclient import SpotifyClient
import config

def run():
    spotifyclient = SpotifyClient(config.refresh_token, config.client_id, config.client_secret, config.user_id)

    #tracks_release_radar = spotifyclient.get_playlist_tracks(config.release_radar_id)
    #response = spotifyclient.add_tracks_to_playlist(config.release_radar_collection_id, tracks_release_radar)
    #print(response)

    #tracks_discover_weekly = spotifyclient.get_playlist_tracks(config.discover_weekly_id)
    #response = spotifyclient.add_tracks_to_playlist(config.discover_weekly_collection_id, tracks_discover_weekly)
    #print(response)

    response = spotifyclient.get_auth_token(config.refresh_token)
    print(response)


if __name__ == '__main__':
    run()
