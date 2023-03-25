from tkinter import *
import os

root = Tk()
root.title('Button')
root.geometry("1280x720")


def reload():
    randomButton.config(text="Planets")

bgdirectory = os.path.dirname(__file__)
bgpath = "button/button.png"
bg_file_path = os.path.join(bgdirectory,bgpath)
random_btn = PhotoImage(file=bg_file_path)

img_label = Label(image=random_btn)
img_label.pack(pady=20)
#


button = Button(root, image=random_btn, command=reload)
button.pack(pady=20)
#Creates an actual button with an event; attaches png to button

randomButton = Label(root, text='')
randomButton.pack(pady=20)

mainloop()

