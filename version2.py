# import necessary modules.
from time import sleep
import pyautogui
from tkinter import *
import random

# classic Tkinter functions.
root = Tk()
root.title('Osu! Paint Tool')
root.geometry("1920x1080")  # change to your screen size.
my_canvas = Canvas(root, width=1920, height=1080, bg="black")  # change to your OSU play window. change BG for "background".
my_canvas.pack(pady=1)
# add your timing of the beatmap.
minute = 3 * 60
second = 23
song_length = (minute+second)
# add the BPM of the song. (this is to help with the calculation of delay between draws.)
bpm = 170
draw_delay = (song_length/bpm)/2

song_duration = range(int(song_length / (draw_delay*2)))

# a numbers between 0 and 255 (for rgb randomisation).
rand_color = list(range(0, 255))

# rgb converter.
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

# time before the program runs.
sleep(5)
# main body of function of creating random colours and images.
for i in song_duration:
    r = random.choice(rand_color)  # create random RED value.
    g = random.choice(rand_color)  # create random GREEN value.
    b = random.choice(rand_color)  # create random BLUE value.
    # first variable values of mouse location.
    x1, y1 = pyautogui.position()
    # print(x1, y1) # uncomment if you want to see the values in console.
    sleep(draw_delay)  # delay to let program have time between mouse movements.
    # second variable values of mouse location.
    x2, y2 = pyautogui.position()
    # print(x2, y2) # uncomment if you want to see the values in console.
    sleep(draw_delay)
    # create x shape, outline = random colour. Change colour letter in fill to have a filled shape.
    my_canvas.create_rectangle(x1, y1, x2, y2, outline=_from_rgb((r, g, b)),  fill="")

# outline=_from_rgb((r, g, b))
# create a postscript to be deciphered by "wand" module.
my_canvas.update()
my_canvas.postscript(file="OsuImage.ps", colormode="color")
root.mainloop()

from wand.image import Image

picture_name = "Monochrome Butterfly.jpg"
with Image(filename="OsuImage.ps") as img:
    img.format = 'jpeg'
    img.save(filename=picture_name)
