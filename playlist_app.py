import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Scopes define the level of access required
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def authenticate_youtube():
    """
    Authenticate using OAuth 2.0 and return the YouTube service object.
    """
    # OAuth 2.0 client secrets file from the Developer Console
    client_secrets_file = "/Users/kehindeoabe/Downloads/Crawl_Youtube_with_python/client_secrets_file.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    
    # Use run_local_server() instead of run_console() for browser-based OAuth flow
    credentials = flow.run_local_server(port=0)

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", credentials=credentials)

    return youtube

def create_playlist(youtube, playlist_name, description="A playlist of gospel artist videos"):
    """
    Create a new playlist on YouTube.
    """
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": playlist_name,
                "description": description,
                "tags": ["gospel", "music", "artist"],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "public"
            }
        }
    )
    response = request.execute()
    return response['id']



if __name__ == "__main__":
    # Authenticate and get YouTube service object
    youtube = authenticate_youtube()

    # Define the playlist name
    playlist_name = "My Gospel Playlist"

    # Create a new playlist
    playlist_id = create_playlist(youtube, playlist_name)
    print(f"Created playlist with ID: {playlist_id}")

    
