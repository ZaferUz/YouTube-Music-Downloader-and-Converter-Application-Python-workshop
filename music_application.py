# import all
from tkinter import *
from youtubeDownloader import download_video
from popup import popup_message
from music_converter import convert_mp4_to_mp3


root = Tk()


def call_downloder(link):
    global title
    title = download_video(link)
    if(title == "No video Found"):
        popup_message("Something Went Wrong, Please check your inputs", "red")

    else:
        popup_message(title+" was downloaded successfully", "green")


def call_convert(new_file_name):
    global title
    isConverted = convert_mp4_to_mp3(title, new_file_name)
    if(isConverted):
        popup_message(title+" was converted successfully to " +
                      new_file_name, "green")

    else:
        popup_message("Something Went Wrong, Please Contact developer", "red")


root.geometry("500x500")
root.title("YouTube Downloader")
Title = Label(root, text="Welcome to Zafer's YouTube \nDownloader & Converter",
              fg='red', font=("Arial Bold", 16))
Title.pack()

video_link_message = Label(
    root, text="Enter YouTube video Link", font=("Arial Bold", 15))
video_link_message.pack()
videoLinkInput = Entry(root, bd=5)
videoLinkInput.pack()

download = Button(root, text="Download", fg='black', bg='grey', font=("Arial", 10), height=1,
                  width=10, command=lambda: call_downloder(videoLinkInput.get()))
download.pack()
video_convert_message = Label(
    root, text="from mp4 to mp3 converter", font=("Arial Bold", 15))
video_convert_message.pack()
video_convert_entery = Entry(root, bd=5)
video_convert_entery.pack()

convert = Button(root, text="Convert", fg='black', bg='grey', font=("Arial", 10), height=1,
                 width=10, command=lambda: call_convert(video_convert_entery.get()))
convert.pack()


root.mainloop()
