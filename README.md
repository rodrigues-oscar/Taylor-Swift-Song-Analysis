# Taylor Swift Song Analysis

## Part 1: Extracting Taylor Swift Song Data From Spotify

First, we need to get data on music from Taylor Swift. To do this, I have written a a Python script that utilizes the Spotipy library to fetch detailed data about Taylor Swift's albums, tracks, and their audio features from the Spotify API. The key steps include:

- Setting up API credentials securely from environment variables.
- Searching for Taylor Swift as the artist and obtaining her unique artist URI.
- Fetching Taylor Swift's albums and iterating through each album to retrieve track information.
- Extracting track details, including name, number, duration, explicitness, popularity, and audio features.
- Storing the collected data in a structured pandas DataFrame.
- Saving the DataFrame to a CSV file for further analysis.