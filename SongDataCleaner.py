import pandas as pd

df = pd.read_csv('rawSongData.csv')

albumsToBeKept= ['spotify:album:1o59UpKw81iHR0HPiSkJR0', # 1989 (Taylor's Version) [Deluxe]
                 'spotify:album:5AEDGbliTTfjOB8TSm1sxt', # Speak Now (Taylor's Version)
                 'spotify:album:1fnJ7k0bllNfL1kVdNVW1A', # Midnights (The Til Dawn Edition)
                 'spotify:album:6kZ42qRrzov54LcAk4onW9', # Red (Taylor's Version)
                 'spotify:album:4hDok0OAJd57SGIT8xuWJH', # Fearless (Taylor's Version)
                 'spotify:album:6AORtDjduMM3bupSWzbTSG', # evermore (deluxe version)
                 'spotify:album:1pzvBxYgT6OVwJLtHkrdQK', # folklore (deluxe version)
                 'spotify:album:1NAmidJlEaVgA3MpcPFYGq', # Lover
                 'spotify:album:6DEjYFkNZh67HP7R9PSZvv'  # reputation                 
                     ]

df = df[df['Album URI'].isin(albumsToBeKept)]
df = df.reset_index(drop=True)

df.to_csv('cleanedSongData.csv', index=False)