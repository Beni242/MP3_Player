import tkinter
import customtkinter
import pygame
from PIL import Image, ImageTk
import time
import math

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # Fixed: removed duplicate root =
root.title("Music player")
root.geometry("400x500")  # Fixed: use x instead of *

#mixer

pygame.mixer.init()

list_of_songs = ['music/City.wav']
list_of_covers = ['img/city.jpg'] 

#funtion to play music
def play_music():
    pass


def skip_forward():
    pass


def skip_backward():
    pass

def volume():
    pass
#buttons

# Play button (center)
play_button = customtkinter.CTkButton(master=root, text='Play', command=play_music)
play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

# Next button (right side) - anchor to EAST so right edge is at relx
skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=50)
skip_f.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)

# Back button (left side) - anchor to WEST so left edge is at relx
skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_backward, width=50)
skip_b.place(relx=0.2, rely=0.7, anchor=tkinter.CENTER)

# Volume

slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=200)
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)




root.mainloop()