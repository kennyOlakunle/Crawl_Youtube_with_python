# Crawl Youtube with Python through Youtube API and OAuth 2.0 client

This is a Python program that Crawl Youtube to get specific video titles and tags by calling Youtube API. This program get Theophilus Sunday's name by mentions and tags, then create a playlist based on this search. This program is only limited to this but other function can be added by automating search and implementing a User Interface for users to interact with. It is better to limit calls to the API.

## YouTube Playlist Creator Documentation

### Overview

This Python script utilizes the YouTube Data API to authenticate a user and create a new playlist on their YouTube channel. It employs OAuth 2.0 for secure access and enables users to organize their favorite videos into a custom playlist.

### Requirements
- Python 3.x
- google-auth-oauthlib library
- google-api-python-client library
- A Google Cloud project with the YouTube Data API enabled
- OAuth 2.0 client secrets file

### Installation
To install the required libraries, you can use pip:

```
pip install google-auth-oauthlib google-api-python-client.

```

### Usage
1. Set up a Google Cloud project and enable the YouTube Data API.
2. Obtain the OAuth 2.0 client secrets file (client_secrets_file.json).
3. Replace the client_secrets_file path in the code with the path to your client secrets file.
4. Run the script. A web browser will open for user authentication. Once authenticated, the script will create a new playlist.
