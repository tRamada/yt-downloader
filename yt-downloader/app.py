from pytube import YouTube

# RUN 'get-streams.py' FIRST
# This only download the video without audio

while True:
    link = input('Youtube link (or quit): ')
    if link.lower() == 'quit':
        break
    youtube_video = YouTube(link)

    print('Title: ', youtube_video.title)
    print('Views: ', youtube_video.views)
    print('Length: ', youtube_video.length) # *Length in seconds*
    print('Rating: ', youtube_video.rating) # *Out of 5*
    # Change the value after run get-streams.py
    to_download = youtube_video.streams.get_by_itag("299")
    print('Downloading...')
    to_download.download("D:/Work/Programing/Languages/Python/yt-downloader/yt-videos")
    print('Download Complete!')