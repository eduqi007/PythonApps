#SIMPLE IMAGEVIEWER VERSION 1.0
# This project is still in progress. For now, I'm focusing on making every object in the window dynamic.
# To achieve that, I'm keeping everything very simple at first so I can understand how everything works.
# Once I finish making everything dynamic, I'll start improving the visual design.
# After that, I plan to make it actually useful by adding the option to upload any image,
# and eventually turn it into a program that users can use daily on their operating system,
# simply by opening the app automatically when trying to view any image.

#Observation: Soon I am going to Organize it better using classes and separating all of it in different archives

#Problems: 1ºSometimes depending of the quantity of images and how large they are the app starts to gets slower to go forward and back and to load the images
#2º When the window of select a directory opens if u maximize the app and after that select the Folder with the images, the window will get messy until u click to select another fold again.
#Despite of that this Version is done. I am fixing all this problems in the next versions, I wanna keep this initial code for comparing my own evolving in the future. 

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

c = 0

root = Tk()

def getting_directory():
    global c
    global file_path
    global images_name
    global imgLabel
    c=0

    file_path = f"{filedialog.askdirectory(title="SELECT THE DIRECTORY")}"


    images_name = loading_image_source(file_path)

    if not images_name:
        print("No image found!")
        return
    
    try:
        img, nouse = loading_image(images_name[c])
        imgLabel = Label(root, image=img)
        imgLabel.place(x=(x_screen - resized_x) // 2, y=y_screen // 30)
        change_image("back")
    except Exception as e:
        print(f"Error! 000x1")

def loading_image_source(images_file_path):
    # Stores the image types that the program should be able to recognize in the folder containing the images to be displayed
    image_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff", ".jfif", ".avif", ".webp")

    # The files matching the selected image types from image_extensions will have their names stored here
    images_name = []

    # Using the os library (which works like the Windows prompt), it will use the listdir command on the directory passed as a parameter to the function, and through the loop, we'll check all files in the folder
    for image_name in os.listdir(images_file_path):
        # Builds the full file path: folder path + file name
        full_file_path = os.path.join(images_file_path, image_name)
        
        # Filters out non-file entries
        if os.path.isfile(full_file_path):

            # Checks whether the current file is an image of a recognized type from image_extensions
            if image_name.lower().endswith(image_extensions):
                images_name.append(image_name)
    return images_name


def loading_image(image_source):
    global y_screen, x_screen, resized_x, img_ratio, file_path

    root.update_idletasks()
    x_screen = root.winfo_width()
    y_screen = root.winfo_height()

    # Loading the image
    image_load = Image.open(f"{file_path}/{image_source}")

    # Getting the image's original width and height
    img_x, img_y = image_load.size

    # Calculating the image aspect ratio
    img_ratio = img_x / img_y

    # Setting the image height based on the window height
    img_display_height = y_screen - 150

    # Setting the new width based on the previously set height and aspect ratio
    resized_x = int(img_display_height * img_ratio)
    if resized_x > x_screen:
        resized_x = int(resized_x - (resized_x - x_screen))
        img_display_height = int(resized_x / img_ratio)

    # Creating the resized image
    img_resized = image_load.resize((resized_x, img_display_height))

    # Converting the image to be used in tkinter
    img_tk = ImageTk.PhotoImage(img_resized)

    return img_tk, resized_x


def window_resize(event):
    global img_ratio, images_path, c, img
    if event.widget == root:
        x_screen = event.width
        y_screen = event.height

        img, img_x = loading_image(images_name[c])
        imgLabel.config(image=img)
        new_width = img_x

        # Reposition to keep image centered
        delta = x_screen - new_width
        imgLabel.place(x=delta // 2, y=y_screen // 30)

        # Reposition buttons
        nextButton.place(x=(x_screen) // 2, rely=0.9)
        backButton.place(x=(x_screen - 105) // 2, rely=0.9)
        exitButton.place(x=13 / 14 * (x_screen), rely=0.9)
        uploadButton.place(x=10/ 13 * (x_screen), rely=0.9)

def change_image(direction):
    global c
    global images_name
    global img
    if direction == "next":
        if c < len(images_name) - 1:
            c += 1
    elif direction == "back":
        if c > 0:
            c -= 1
    else:
        root.quit()
        return
    img, nouse = loading_image(images_name[c])
    imgLabel.config(image=img)
    imgLabel.place(x=(x_screen - resized_x) // 2, y=y_screen // 30)
    print(c)


# Initial window size
x_screen = 1024
y_screen = 720

root.minsize(800, 600)
root.geometry(f"{x_screen}x{y_screen}")

# Basic interface
nextButton = Button(root, text=">>", padx=12, pady=5, command=lambda: change_image("next"))
backButton = Button(root, text="<<", padx=12, pady=5, command=lambda: change_image("back"))
exitButton = Button(root, text="Exit", padx=20, pady=5, command=lambda: change_image("exit"))
uploadButton = Button(root, text="Select a directory", padx=20, pady=5, command=lambda: getting_directory())

nextButton.place(x=(x_screen) // 2, rely=0.9)
backButton.place(x=(x_screen - 105) // 2, rely=0.9)
exitButton.place(x=12 / 13 * (x_screen), rely=0.9)
uploadButton.place(x=10/ 13 * (x_screen), rely=0.9)


getting_directory()

# Binds window resize event
root.bind("<Configure>", window_resize)
root.mainloop()

