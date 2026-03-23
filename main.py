import tkinter
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import Thread
import time
import math

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # Fixed: removed duplicate root =
root.title("Music player")
root.geometry("400x500")  # Fixed: use x instead of *

#mixer

pygame.mixer.init()

list_of_songs = ['music/Alex Warren.mp3', "music/One_Direction.mp3"]
list_of_covers = ['img/photo_1.png', 'img/photo_2.png'] 
current_song_index = 0
is_playing = False
is_paused = False
song_loaded = False


def get_album_cover(song_index):
    image1 = Image.open(list_of_covers[current_song_index])
    image2 = image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=.19, rely=.06)
   # Extract song name (remove 'music/' prefix)
    song_name = list_of_songs[song_index].replace('music/', '').replace('.mp3', '')
    song_name_label = tkinter.Label(root, text=song_name, bg="#222222", fg='white')
    song_name_label.place(relx=0.4, rely=0.6)


 #Update progress bar
def progress():
    try:
       # Get the current song's length in seconds
        song = pygame.mixer.Sound(list_of_songs[current_song_index])
        song_length = song.get_length()  # Total length in seconds
        
        while pygame.mixer.music.get_busy():
            if pygame.mixer.music.get_pos() > 0:
                current_pos = pygame.mixer.music.get_pos() / 1000  # Convert ms to seconds
                # Calculate percentage (0.0 to 1.0)
                if song_length > 0:
                    progress_percentage = current_pos / song_length
                    progressbar.set(progress_percentage)
            time.sleep(0.5)
    except:
        pass


def threading():
    t1 = Thread(target=progress, daemon=True)
    t1.start()


#function to play/pause music
def play_pause_music():
    global current_song_index, is_playing, is_paused, song_loaded
    
    if not song_loaded:
        # First time playing, load the song
        threading()
        song_name = list_of_songs[current_song_index]
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(.5)
        get_album_cover(current_song_index)
        is_playing = True
        is_paused = False
        song_loaded = True
        play_button.configure(text='Pause')
    elif is_playing and not is_paused:
        # Music is playing, so pause it
        pygame.mixer.music.pause()
        is_paused = True
        is_playing = False
        play_button.configure(text='Play')
    elif is_paused:
        # Music is paused, so resume it
        pygame.mixer.music.unpause()
        is_paused = False
        is_playing = True
        play_button.configure(text='Pause')


def skip_forward():
     global current_song_index, is_playing, is_paused, song_loaded
     current_song_index = (current_song_index + 1) % len(list_of_songs)
     pygame.mixer.music.stop()
     is_playing = False
     is_paused = False
     song_loaded = False
     play_pause_music()
     play_button.configure(text='Pause')


def skip_backward():
     global current_song_index, is_playing, is_paused, song_loaded
     current_song_index = (current_song_index - 1) % len(list_of_songs)
     pygame.mixer.music.stop()
     is_playing = False
     is_paused = False
     song_loaded = False
     play_pause_music()
     play_button.configure(text='Pause')

def volume(value):
    pygame.mixer.music.set_volume(float(value))


#buttons

# Play/Pause button (center)
play_button = customtkinter.CTkButton(master=root, text='Play', command=play_pause_music, width=100)
play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

# Next button (right side)
skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=50)
skip_f.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)

# Back button (left side)
skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_backward, width=50)
skip_b.place(relx=0.2, rely=0.7, anchor=tkinter.CENTER)

# Volume

slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=200)
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

#progress bar

progressbar = customtkinter.CTkProgressBar(master=root, progress_color="#ededf6", width=200)
progressbar.place(relx=.5, rely=.85, anchor=tkinter.CENTER)



root.mainloop()