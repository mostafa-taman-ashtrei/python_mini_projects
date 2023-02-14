from pytube import YouTube
from sys import argv

video_link = argv[1]
youtube_lib = YouTube(video_link)
download_path = 'videos'

print(f"Title -> {youtube_lib.title}")
print(f"Views -> {youtube_lib.views}")
print(f"Author -> {youtube_lib.author}")
print(f"Keywords -> {youtube_lib.keywords}")
print(f"length -> {youtube_lib.length}")
print(f"Desc -> {youtube_lib.description}")


download_stream = youtube_lib.streams.get_highest_resolution()
download_stream.download(download_path)
