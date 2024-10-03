# Crawl Youtube with Python through Youtube API

This is a Python program that Crawl Youtube to get specific video titles and tags by calling Youtube API. This program get Theophilus Sunday's name by mentions and tags, then create a playlist based on this search. This program is only limited to this but other function can be added by automating search and implementing a User Interface for users to interact with. It is better to limit calls to the API


## Steps to be Taken

To create a Python program that crawls YouTube to find videos mentioning a specific gospel artist and then creates a playlist, I used the YouTube Data API. Here's an overview of the steps involved:

### Set up the YouTube Data API:

- Get an API key from the Google Developer Console.

### Install the required libraries:
`google-api-python-client` to interact with the YouTube API.

### Search for videos mentioning the artist:

- Use the `youtube.search().list()` method to search for videos based on keywords (the gospel artist’s name).

### Create a playlist:

- Use the API to create a new playlist.
- Add the video results to that playlist using the playlistItems.insert() method.

### Program structure:

- Search for the artist's videos.
- Create a playlist.
- Add videos to the playlist.
