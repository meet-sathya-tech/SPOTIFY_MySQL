import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mysql.connector

# Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='cf63e7bdff264cf88d16a61bbf840c4c',
    client_secret='abb6a051ba1b43cdbcbf1714b465ba4c'
))

# MySQL connection config
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Nandha@2005',
    'database': 'spotify'
}

# Connect to MySQL
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Read URLs from file
file_path = r"D:\nandhadownloads\my_sql_project1\venv\track_urls.txt"
with open(file_path, 'r') as file:
    track_urls = file.readlines()

for track_url in track_urls:
    track_url = track_url.strip()
    try:
        match = re.search(r'track/([a-zA-Z0-9]+)', track_url)
        # if not match:
        #     print(f"Invalid URL format: {track_url}")
        #     continue
        
        track_id = match.group(1)
        track = sp.track(track_id)
        
        track_data = (
            track['name'],
            track['artists'][0]['name'],
            track['album']['name'],
            track['popularity'],
            track['duration_ms'] / 60000
        )
        
        insert_query = """
        INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, track_data)
        connection.commit()
        
        print(f"Inserted: {track['name']} by {track['artists'][0]['name']}")
    
    except Exception as e:
        print(f"Error processing {track_url}: {e}")

cursor.close()
connection.close()
print("All tracks processed.")

