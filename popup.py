from tkinter import *


def popup_message(message, color):
    popup = Tk()

    def leave_mini():
        popup.destroy()

    popup.title("Download Status")
    Label(popup, text=message, fg=color).pack()
    Button(popup, text="Okay", command=leave_mini).pack()
    popup.mainloop()
