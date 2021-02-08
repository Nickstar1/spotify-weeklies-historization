# Historization of Spotify Release Radar and Discover Weekly
This script is designed to historize Spotify's Release Radar and Discover Weekly playlists. All Tracks will be stored in it's coresponding playlist. </br></br>

The following steps are necessary, otherwise the script won't work.

## Step 1 - Creating an app
1. Open the [Spoitfy for Developers dashboard](https://developer.spotify.com/dashboard/login) and log into your Spoitfy account.
2. Create a new app, give it a name and a description.
3. In your dashbord navigate to edit settings.
4. Add a redirect URI and press save (redirect URI can be any link to a website, e.g. http://mysite.com/callback/)

## Step 2 - Editing config file
1. Copy both Client ID and Client Secret from your developers dashboard. 
2. Replace client_id and client_secret in the config.py file with the credentials of your app.
3. Change user_id to your Spotify account name.
Optional: Open Spotify, create 2 playlists and name them however you like (e.g. Discover Weekly Collection, Release Radar Collection)
4. In Spotify navigate to your Release Radar, Discover Weekly and your 2 playlists where you want all your tracks to be stored in. Right click each playlist and click share > Copy Spotify URI. The Spotify URI spotify:playlists:yourplaylistID.
5. Replace release_radar_collection_id, discover_weekly_collection_id, release_radar_id and discover_weekly_id with the correct IDs of your playlists.

## Step 3 - URL encode redirect URI
1. Choose any URL encoder/decoder (e.g. https://meyerweb.com/eric/tools/dencoder/).
2. Paste in your redirect URI and click encode.
3. Copy your encoded redirect URI - you will need it the 5th step.

## Step 4 - Base64 encode your app credentials
1. Choose any base64 encoder/decoder (e.g. https://www.base64encode.org/)
2. Enter your credentials (Client ID and Client Secret) seperated with an colon (:). e.g. thisismyappid:thisismyappsecret
3. Click encode and copy it - you will need it in the next step.

## Step 5 - Obtain access and refresh token
1. Replace client_id and redirect_uri in the following link to your Client ID and encoded redirect URI, click on that link and follow the instructions:
https://accounts.spotify.com/authorize?client_id=thereshouldbeyourclientID&response_type=code&redirect_uri=http%3A%2F%2Fmysite.com%2Fcallback%2F&scope=playlist-modify-private%20playlist-modify-public
2. You will be redirected to the website you chose in step 1.4. Copy the response in the address bar (everything after code=).
3. Replace yourbase64encodedstring with your in step 4.3 base64 encoded credentials, code with your response from step 5.2 and redirect_uri with your encoded redirect URI in the following command:
curl -H "Authorization: Basic yourbase64encodedstring" -d grant_type=authorization_code -d code=responsefromstep5.2 -d redirect_uri=yourencodedredirecturi https://accounts.spotify.com/api/token
4. Open a terminal and paste command with your correct credentials and press enter.
5. If everything works correctly you should receive a response like this: {"access_token":"B...G","token_type":"Bearer","expires_in":3600,"refresh_token":"A...4","scope":"playlist-modify-private playlist-modify-public"}
6. Replace the refresh_token in the config.py file with your obtained refresh token and you are good to go!