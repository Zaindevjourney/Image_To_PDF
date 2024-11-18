import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

#function to convert  image to pdf

def images_to_pdf(images, pdf_name):
    try:
        #CREATE A NEW PDF FILE
        pdf = Image.open(images[0])
        pdf.save(pdf_name, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
        messagebox.showinfo("success", "Image  have been successfully converted to PDF. ")

    except Exception as e:
        messagebox.showerror("Error","Failed to convert image to pdf.\nError: " + str(e))

#FUNCTION TO SELECT IMAGE
def select_images():
    images = filedialog.askopenfilenames(title="Select Images",  filetypes=(("Image files", "*.jpg;*.png"),
                                                                             ("All files", "*.*")),
                                                                             initialdir="C:/")
    return images

#FUCTION TO SELECT PDF NAME AND PATH 
def select_pdf():
    pdf = filedialog.asksaveasfilename(title="Save PDF as", defaultextension=".pdf", initialdir="C:/",
                                       filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
    return pdf
#CREATE GUI
root = tk.Tk()
root.title("convert Images To PDF")
select_images_btn = tk.Button(root, text="Select Images", command=select_images)
select_pdf_btn = tk.Button(root, text="Select PDF", command=select_pdf)
convert_btn = tk.Button(root, text="Convert", command=lambda: images_to_pdf(select_images(),select_pdf()))
select_images_btn.pack()
select_pdf_btn.pack()
convert_btn.pack()
root.mainloop()