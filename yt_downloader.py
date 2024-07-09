# prompt: A script to download YouTube videos and convert them to .mp3, can you add auto search and pick first result to download

# do !pip install pytube
from pytube import YouTube

def download_video(url):
  yt = YouTube(url)
  video = yt.streams.filter(only_audio=True).first()
  video.download()

def search_and_download(query):
  from googleapiclient.discovery import build
  youtube = build('youtube', 'v3', developerKey="YOUR_API_KEY")
  search_response = youtube.search().list(q=query, type="video", part="id,snippet", maxResults=1).execute()
  video_id = search_response["items"][0]["id"]["videoId"]
  download_video("https://www.youtube.com/watch?v=" + video_id)

query = "your search query"
search_and_download(query)