
import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 12
    password_max = 20
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint (password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    with open("mesmotdepasse.txt", "a+") as file:
        file.write(password + "\n")
        file.close()
        
def application_name():
    application_min = 1
    application_max = 20
    application = "".join(Entry(all_chars) for x in range(randint (application_min, application_max)))
    all_chars = string.ascii_letters + string.punctuation + string.digits

    application_name.delete(0, END)
    application_name.insert(0, application_name)

    with open("mesmotdepasse.txt", "a+") as file:
        file.write(password + "\n")
        file.close()

window = Tk()
window.title("Générateur de Mot de passe")

window.config(background='#464646')

frame = Frame(window, bg='#464646')

width = 612
height = 512
image = PhotoImage(file="logoge.png").zoom(20).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#464646', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg='#464646')

bievenue = Label(right_frame, text="Bienvenue !", font=("Arial", 30), bg='#464646', fg='white')
bievenue.pack()


label_title = Label(right_frame, text="Mot de passe", font=("Arial", 20), bg='#464646', fg='white')
label_title.pack()

password_entry = Entry(right_frame, font=("Arial", 20), bg='#464646', fg='white')
password_entry.pack()

generate_password_button = Button(right_frame, text="Générer mon nouveau mot de passe", font=("Arial", 20), bg='#037a8a', fg='white', command=generate_password)
generate_password_button.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

menu_bar = Menu(window)

# Pages 

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Mes liens")
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu) 

window.config(menu=menu_bar)

window.mainloop()