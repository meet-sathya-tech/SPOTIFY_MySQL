Overview


SPOTIFY_MySQL is a Python-based application that integrates the Spotify Web API with a MySQL database to retrieve, process, and store Spotify track metadata. The project demonstrates API integration, database operations, data processing, and visualization using Python.


Features


Retrieve track information from the Spotify Web API.
Extract Spotify Track IDs automatically from track URLs.
Store track metadata in a MySQL database.
Process both single and multiple Spotify track URLs.
Export retrieved data to CSV format.
Visualize track popularity and duration using Matplotlib.
Handle invalid URLs and API errors through exception handling.


Technologies


Python
Spotify Web API
Spotipy
MySQL
MySQL Connector
Pandas
Matplotlib
Regular Expressions (Regex)


Implementation


This project was developed to gain practical experience with API integration and database management using Python.
The application authenticates with the Spotify Web API using the Client Credentials flow provided by Spotipy. A Spotify Track ID is extracted from the provided track URL using Regular Expressions before sending a request to the API.
The API returns track information in JSON format. The application processes the response and extracts relevant details including the track name, artist, album, popularity score, and duration.


The retrieved data can be:


Displayed using Pandas
Exported to a CSV file
Stored in a MySQL database
Visualized using Matplotlib
