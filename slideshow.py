from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk
import time

root = tk.Tk()
root.title("Image Slideshow")


image_paths = [
    r"D:\programming\day_2\photo\hridoy 3.jpg",
    r"D:\programming\day_2\photo\hridoy.jpg",
    r"D:\programming\day_2\photo\IMG-20240601-WA0006.jpg",
    r"D:\programming\day_2\photo\IMG_20240310_151516.jpg",
    r"D:\programming\day_2\photo\IMG_20230713_133037.jpg", 
]

image_size = (1080,1080)
images = [Image.open(path). resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images] 

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(2)

slideshow =cycle(photo_images)

def start_slideshow():
    for _ in range(len(photo_images)):
        update_image()

play_button = tk.Button(root, text="PLay Slideshow", command=start_slideshow)
play_button.pack()


# sob somoy run rakar jonno
root.mainloop()