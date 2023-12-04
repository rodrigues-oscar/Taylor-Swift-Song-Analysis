# Taylor Swift Song Analysis

**_Dear Reader_**,

As a **_lover_** of Taylor Swift's music, **_this is me trying_** to leverage my data science skills for a deeper analysis of her musical journey. I am going to start by generating a dataset of her music with the help of Spotify's API. Then, I will clean the dataset - this will allow me to perform statistical analyses which can uncover insights such as the relationship between the **_mean (taylor's version)_** tempo of an album and it's popularity.

Sidenote: I highly encourage you to blast some of Taylor's music as you read through this, I promise it just **_hits different_**.

## Part 1: Extracting Taylor Swift Song Data From Spotify

With no data, all we have is a **_blank space_**. So first, we need to get data on music from Taylor Swift - I have written a Python script, titled [SongDataExtractor.py](https://github.com/rodrigues-oscar/Taylor-Swift-Song-Analysis/blob/main/SongDataExtractor.py), that utilizes the Spotipy library to fetch detailed data about Taylor Swift's albums and tracks from the Spotify API. The key steps include:

- Setting up API credentials securely from environment variables.
- Searching for Taylor Swift as the artist and obtaining her unique artist URI.
- Fetching Taylor Swift's albums and iterating through each album to retrieve track information.
- Extracting track details, including name, number, duration, explicitness, popularity, and audio features.
- Storing the collected data in a structured pandas data frame.
- Saving the data frame to a CSV file for further analysis.

## Part 2: Cleaning The Dataset

Never in my **_wildest dreams (taylor's version)_** did I think that our raw data would be so **_clean (taylor's version)_**. When reading our raw data into a dataframe, pandas correctly assigns types to all of our columns - running `df.dtypes` returns:

```
Album Name              object
Track Number             int64
Track Name              object
Track Duration (ms)      int64
Explicit                  bool
Popularity               int64
Acousticness           float64
Danceability           float64
Energy                 float64
Instrumentalness       float64
Key                      int64
Liveness               float64
Loudness               float64
Speechiness            float64
Tempo                  float64
Time Signature           int64
Valence                float64
Album URI               object
Track URI               object
dtype: object
```

However, We do have duplicates in our data.. kind of. Spotify treats an album and its deluxe version as two separate albums entirely. So I wrote a quick little Python script titled [SongDataCleaner.py](https://github.com/rodrigues-oscar/Taylor-Swift-Song-Analysis/blob/main/SongDataCleaner.py). In the script, I manually curated a list of the albums I wanted to keep (prioritizing Taylor's Version and then the deluxe version) and then used the [`Series.isin`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html) function to create a new dataframe with the albums I wanted.

## Part 3: Generating Visualizations And Deriving Insights

Now that we have a set of cleaned data, we're in the **_end game_**.

## Conclusion

**_Is it over now? (taylor's version) (from the vault)_**

Unfortunately yes but you should drop me a follow as I have more fun projects planned.

If you have feedback or a **_question...?_**, please reach out to me at rodrigues-oscar@outlook.com