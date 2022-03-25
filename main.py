import random
from tkinter import *
from tkinter import messagebox

from tkinter import *

# loading Python Imaging Library
from PIL import ImageTk, Image,  ImageEnhance

# To get the dialog box to open when required
from tkinter import filedialog
import random


def ReduceOpacity(im, opacity):
    """
    Returns an image with reduced opacity.
    Taken from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/362879
    """
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='"pen')
    return filename


def save_image(saveimg):
    saveimg.save(f'watermarked_image{random.randint(10,100)}.jpg')
    upload_button.config(text="Saved successfully!")


def open_logo(img):
    print("opening logo")
    main_image = img
    y = openfilename()
    logo = Image.open(y)
    image_copy = main_image.copy()
    logo = logo.resize((int(image_copy.width / 2), int(image_copy.height / 5)), Image.ANTIALIAS)
    logo = ReduceOpacity(logo, 0.5)
    position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
    watermarked_image = image_copy.paste(logo, position, logo)
    watermarked_image = image_copy
    img_to_save = image_copy
    upload_button.config(text="Save Image", command=lambda: save_image(img_to_save))
    watermarked_image = watermarked_image.resize((250, 250), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    watermarked_image = ImageTk.PhotoImage(watermarked_image)

    # create a label
    panel = Label(window, image=watermarked_image)

    # set the image as img
    panel.image = watermarked_image
    panel.grid(row=1, column=1)
    # image_copy.save('pasted_image.jpg')


def open_img():
    # Select the Imagename  from a folder
    x = openfilename()

    # opens the image
    img = Image.open(x)
    main_img = img
    upload_button.config(text="Set watermark", command=lambda: open_logo(main_img))
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    # create a label
    panel = Label(window, image=img)

    # set the image as img
    panel.image = img
    panel.grid(row=1,column=1)



window = Tk()
window.title("Image watermarking app")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50)



upload_button = Button(text="Upload an image",  width="36", command=open_img)
upload_button.grid(row=2, column=1)


window.mainloop()