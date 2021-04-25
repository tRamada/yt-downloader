from pytube import YouTube

link = input('Youtube link (or quit): ')
youtube_video = YouTube(link)

for video in youtube_video.streams:
    print(video)