
from os import link
from queue import Empty
from tkinter import *
from tkinter import filedialog
from turtle import width

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
link_label = Label(screen, text="URL do video: ")

#Add widgets to window
Canvas.create_window(250, 170, window=link_label)
Canvas.create_window(250, 220, window=link_field)


screen.mainloop()