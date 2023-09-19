from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

""" 

Setting up the client credentials flow to access Spotify's API
Docs: https://spotipy.readthedocs.io/en/2.22.1/#client-credentials-flow

"""

load_dotenv() # Added .env file to .gitignore to hide Spotify API's client_id and client_secret from public GitHub repository
clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")
clientCredentialsManager = SpotifyClientCredentials(
    client_id=clientId,
    client_secret=clientSecret
)
sp = spotipy.Spotify(client_credentials_manager=clientCredentialsManager)

"""

Here are the steps to extracting song data:

1. Search by Artist for "Taylor Swift"
2. Get artist URI
3. Search for Albums based on artist URI
4. Get album names and URIs
5. Search for Tracks based on album URI
6. Get track names, numbers, durations, explicit classificaitons, URIs
7. Search for Audio Features based on track URIs
8. Get audio features
9. Append to list

"""

artistName = "Taylor Swfit"
searchForArtistResult = sp.search(q=artistName, limit=1, type="artist") # Searching for artist based on inputted string to get artist URI
artistUri = searchForArtistResult["artists"]["items"][0]["uri"] # Accessing JSON object to retrieve artist URI

searchForAlbumsResult = sp.artist_albums(artistUri, album_type="album", limit=50) # Searching for albums based on artist URI to get album URIs
artistAlbums = searchForAlbumsResult['items'] # Accessing 'items' to traverse down one layer of JSON object
numberOfAlbums = len(artistAlbums)

trackDatabase = []

for album in range(numberOfAlbums):
    albumName = artistAlbums[album]['name'] # Accessing JSON object to retrieve album name
    albumUri = artistAlbums[album]['uri'] # Accessing JSON object to retrieve album URI
    
    searchForAlbumTracksResult = sp.album_tracks(albumUri, limit=50)  # Searching for album tracks based on album URI to get tracks within each album
    albumTracks = searchForAlbumTracksResult['items'] # Accessing 'items' to traverse down one layer of JSON object
    numberOfTracks = len(albumTracks)
    
    for track in range(numberOfTracks):
        trackName = albumTracks[track]['name'] # Accessing JSON object to retrieve track name
        trackNumber = albumTracks[track]['track_number'] # Accessing JSON object to retrieve track number within album
        trackDuration = albumTracks[track]['duration_ms'] # Accessing JSON object to retrieve track duration in milliseconds
        trackExplicit = albumTracks[track]['explicit'] # Accessing JSON object to retrieve track's explicit qualification
        trackUri = albumTracks[track]['uri'] # Accessing JSON object to retrieve track URI

        searchForTrackPopularity = sp.track(trackUri) # Searching for track based on track URI to find track popularity
        trackPopularity = searchForTrackPopularity['popularity'] # Accessing JSON object to retrieve track popularity
        
        searchForTrackAudioFeaturesResult = sp.audio_features(trackUri) # Searching for audio features based on track URI to find audio features
        trackFeatures = searchForTrackAudioFeaturesResult[0] # Accessing list to retrieve JSON object

        trackAcousticness = trackFeatures['acousticness'] # Accessing JSON object to retrieve track acousticness
        trackDanceability = trackFeatures['danceability'] # Accessing JSON object to retrieve track danceability
        trackEnergy = trackFeatures['energy'] # Accessing JSON object to retrieve track energy
        trackInstrumentalness = trackFeatures['instrumentalness'] # Accessing JSON object to retrieve track instrumentalness
        trackKey = trackFeatures['key'] # Accessing JSON object to retrieve track key
        trackLiveness = trackFeatures['liveness'] # Accessing JSON object to retrieve track liveness
        trackLoudness = trackFeatures['loudness'] # Accessing JSON object to retrieve track loudness
        trackSpeechiness = trackFeatures['speechiness'] # Accessing JSON object to retrieve track speechiness
        trackTempo = trackFeatures['tempo'] # Accessing JSON object to retrieve track tempo
        trackTimeSignature = trackFeatures['time_signature'] # Accessing JSON object to retrieve track time signature
        trackValence = trackFeatures['valence'] # Accessing JSON object to retrieve track valence
        
        trackDatabase.append([ # Appending data to list 
            albumName,
            trackNumber,
            trackName,
            trackDuration,
            trackExplicit,
            trackPopularity,
            trackAcousticness,
            trackDanceability,
            trackEnergy,
            trackInstrumentalness,
            trackKey,
            trackLiveness,
            trackLoudness,
            trackSpeechiness,
            trackTempo,
            trackTimeSignature,
            trackValence,
            albumUri,
            trackUri,
            ])

df = pd.DataFrame(trackDatabase, columns=[ # Converting list to dataframe
    'Album Name',
    'Track Number',
    'Track Name',
    'Track Duration (ms)',
    'Explicit',
    'Popularity',
    'Acousticness',
    'Danceability',
    'Energy',
    'Instrumentalness',
    'Key',
    'Liveness',
    'Loudness',
    'Speechiness',
    'Tempo',
    'Time Signature',
    'Valence',
    'Album URI',
    'Track URI',
])

df.to_csv('TaylorSwiftSongData.csv', index=False) # Save as CSV and drop index