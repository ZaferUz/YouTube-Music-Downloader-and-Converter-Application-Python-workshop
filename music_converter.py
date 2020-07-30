
from moviepy.editor import *


def convert_mp4_to_mp3(mp4_file, mp3_file):
    try:
        videClip = VideoFileClip(mp4_file+".mp4")
        audioClip = videClip.audio
        audioClip.write_audiofile(mp3_file+".mp3")
        audioClip.close()
        videClip.close()
        return True
    except Exception as ex:
        print(ex)
        return False
