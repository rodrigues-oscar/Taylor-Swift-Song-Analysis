# Taylor Swift Song Analysis

**_Dear Reader_**,

As a **_lover_** of Taylor Swift's music, **_this is me trying_** to leverage my data science skills for a deeper analysis of her musical journey.

## Part 1: Extracting Taylor Swift Song Data From Spotify

With no data, all we have is a **_blank space_**. So first, we need to get data on music from Taylor Swift - I have written a Python script that utilizes the Spotipy library to fetch detailed data about Taylor Swift's albums and tracks from the Spotify API. The key steps include:

- Setting up API credentials securely from environment variables.
- Searching for Taylor Swift as the artist and obtaining her unique artist URI.
- Fetching Taylor Swift's albums and iterating through each album to retrieve track information.
- Extracting track details, including name, number, duration, explicitness, popularity, and audio features.
- Storing the collected data in a structured pandas data frame.
- Saving the data frame to a CSV file for further analysis.