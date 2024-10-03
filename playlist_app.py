import os
from googleapiclient.discovery import build

# Load the API key from the environment variable. (You can also hardcode the API key here. But rwmember to keep it secret)
api_key = os.getenv('YOUTUBE_API_KEY')


# Set up YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

def search_videos(artist_name, max_results=10):
    """
    Search for videos related to the gospel artist.
    """
    request = youtube.search().list(
        q=artist_name,
        part='snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    
    videos = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        videos.append({'id': video_id, 'title': video_title})
    
    return videos

def create_playlist(playlist_name, description="A playlist of gospel artist videos"):
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

def add_video_to_playlist(playlist_id, video_id):
    """
    Add a video to the playlist.
    """
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    request.execute()

if __name__ == "__main__":
    artist_name = "YOUR_GOSPEL_ARTIST_NAME"
    playlist_name = f"{artist_name} Playlist"
    
    # Step 1: Search for videos
    videos = search_videos(artist_name)
    
    # Step 2: Create a new playlist
    playlist_id = create_playlist(playlist_name)
    
    # Step 3: Add each video to the playlist
    for video in videos:
        add_video_to_playlist(playlist_id, video['id'])
        print(f"Added video: {video['title']} to playlist.")
    
    print(f"Playlist '{playlist_name}' created with {len(videos)} videos.")
