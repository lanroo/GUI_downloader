
from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


# Functions

def select_path():
    #user to select a path from explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def donwload_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Baixando...')
    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('O seu video foi baixado!')

    

screen = Tk()
title = screen.title('Youtube Download')
Canvas = Canvas(screen, width=500, height=500)
Canvas.pack()

# image Logo

logo_img = PhotoImage(file='yt.png')

#resize image

logo_img = logo_img.subsample(2, 2)

Canvas.create_image(250,80, image=logo_img)


#Link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="URL do video: ", font=('Arial', 15))

# Select Path for saving the file

path_label = Label(screen, text="Selecione a pasta de destino", font=('Arial', 15))
select_btn = Button(screen, text="Selecionar Pasta", command=select_path)

# Add to window

Canvas.create_window(250, 280, window=path_label)
Canvas.create_window(250, 330, window=select_btn)


#Add widgets to window
Canvas.create_window(250, 170, window=link_label)
Canvas.create_window(250, 220, window=link_field)

#Downloads btns

download_btn = Button(screen, text="Baixar Video", command=donwload_file)

# Add to canvas

Canvas.create_window(250, 390, window=download_btn)


screen.mainloop()