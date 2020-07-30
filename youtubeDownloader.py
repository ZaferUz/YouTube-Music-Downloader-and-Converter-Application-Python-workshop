from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context


def download_video(video_link):
    try:
        yt = YouTube(str(video_link))
        stream = yt.streams.first()
        stream.download()
        return yt.title
    except:
        return "No video Found"
