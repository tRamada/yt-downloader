from movie.editor import*

mp4_file = 'video.mp4'
mp3_file = 'audio.mp3'

videoclip = VideoFileClip(mp4_file)

audioclip = videoclip.audio

audioclip.write_audiofile(mp3_file)

audioclip.close()

videoclip.close()