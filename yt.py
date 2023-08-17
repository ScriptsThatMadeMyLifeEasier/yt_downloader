from pytube import YouTube
from PIL import Image
import requests
from io import BytesIO
from pytube import Playlist
import os

import pyperclip
from plyer import notification

link = pyperclip.paste()

yt = YouTube(link)

print(yt.title)
print(yt.views)

notification.notify(
    title = "started downloading",
    message = f"{yt.title} ",
    app_icon="",
    timeout=5
)

down = yt.streams.get_highest_resolution()

print(yt.thumbnail_url)

response = requests.get(yt.thumbnail_url)
img = Image.open(BytesIO(response.content))
img.save("/home/dheeraj/Desktop/Projects/yt_vid/logo.ico")


down.download('/home/dheeraj/Videos/youtube_videos')

notification.notify(
    title = "Downloaded",
    message = f"{yt.title} has been downloaded",
    app_icon="/home/dheeraj/Desktop/Projects/yt_vid/logo.ico",
    timeout=15
)

os.remove("/home/dheeraj/Desktop/Projects/yt_vid/logo.ico")

