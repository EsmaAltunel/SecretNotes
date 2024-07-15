import tkinter
from tkinter import *
from tkinter import messagebox
import cryptocode
from PIL import Image, ImageTk

parent = tkinter.Tk()
parent.title("Secret Notes")
parent.config(pady=30, padx=30)
FONT = ("Arial", "12", "normal")

image = Image.open('secrett2.png')
image = ImageTk.PhotoImage(image)

image_label = tkinter.Label(parent, image=image)
image_label.pack()


def save_directory():
    title = my_entry.get()
    secret = my_text.get("1.0", END)
    password = my_entry_2.get()
    myEncryptedMessage = cryptocode.encrypt(secret, password)


    if len(title) == 0 or len(secret) == 0 or len(password) == 0 :
        tkinter.messagebox.showinfo(message="Enter all spaces!")
    else:
        directory = open("mytext3.txt", "a")
        directory.write(f"\n{title}\n{myEncryptedMessage}")

        my_entry.delete(0, END)
        my_entry_2.delete(0, END)
        my_text.delete("1.0", END)
def decryption():
    myEncryptedMessage = my_text.get("1.0", END)
    password = my_entry_2.get()

    if len(myEncryptedMessage) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
          myDecryptedMessage = cryptocode.decrypt(myEncryptedMessage,password)
          my_text.delete("1.0", END)
          my_text.insert("1.0", myDecryptedMessage)


my_label = tkinter.Label(text="Enter your title", font=FONT)
my_label.pack()

my_entry = tkinter.Entry(width=50)
my_entry.pack()

my_label_2 = tkinter.Label(text="Enter your secret", font=FONT)
my_label_2.pack()

my_text = tkinter.Text(width=50, height=20)
my_text.pack()

my_label_3 = tkinter.Label(text="Enter master key", font=FONT)
my_label_3.pack()

my_entry_2 = tkinter.Entry(width=50)
my_entry_2.pack()

my_button = tkinter.Button(text="Save & Encyrpt", command=save_directory)
my_button.pack()

my_button_2 = tkinter.Button(text="Decrypt", command=decryption)
my_button_2.pack()

parent.mainloop()