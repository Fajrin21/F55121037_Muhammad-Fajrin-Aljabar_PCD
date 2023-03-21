import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

def brightness_correction(img):
    brightness = 100
    bright_img = cv2.add(img, brightness)
    return bright_img

def grayscale(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

def show_image(img, x, y, title):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=x, y=y)
    title_label = tk.Label(root, text=title)
    title_label.place(x=x, y=y-20)

def process_image(method):
    global original_img
    if method == 'brightness_correction':
        corrected_img = brightness_correction(original_img)
        show_image(corrected_img, 350, 120, 'Brightness Correction')
    elif method == 'grayscale':
        corrected_img = grayscale(original_img)
        show_image(corrected_img, 650, 120, 'Grayscaling')

def show_creator():
    creator_label = tk.Label(root, text='Nama : Muhammad Fajrin Aljabar    '
                                        'NIM : F55121037    Kelas : A')
    creator_label.place(x=150, y=50)

def open_image():
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        show_image(original_img, 50, 120, 'Gambar Original')
        size_label.config(text='Dimensi : {} x {}'.format(original_img.shape[1], original_img.shape[0]))

root = tk.Tk()
root.geometry('800x800')
root.title('F55121037')

title_label = tk.Label(root, text='Gambar Asli')
title_label.place(x=50, y=20)

open_button = tk.Button(root, text='Load an image', command=open_image)
open_button.place(x=50, y=50)

size_label = tk.Label(root, text='Dimensi : -')
size_label.place(x=450, y=620)

correction_box = tk.LabelFrame(root, text='Perbaikan Citra', padx=5, pady=5)
correction_box.place(x=50, y=690, width=170, height=70)

brightness_button = tk.Button(correction_box, text='Kecerahan', command=lambda: process_image('brightness_correction'))
brightness_button.pack(side=tk.LEFT, padx=5)

smoothing_button = tk.Button(correction_box, text='Grayscaling', command=lambda: process_image('grayscale'))
smoothing_button.pack(side=tk.LEFT, padx=5)

show_creator()  
root.mainloop()

