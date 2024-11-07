import string
from random import randint, choice
from tkinter import *

def Noah_generate_password():
    password_min = 12
    password_max = 20
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for _ in range(randint(password_min, password_max)))
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    app_name = app_name_entry.get().strip()
    if app_name:
        try:
            with open("mesmotdepasse.txt", "a+") as file:
                file.write(f"{app_name} : {password}\n")
        except IOError:
            print("Erreur lors de l'écriture dans le fichier.")
    else:
        print("Veuillez entrer le nom de l'application.")

window = Tk()
window.title("Générateur de Mot de Passe")
window.config(background='#1e1e2f')

frame = Frame(window, bg='#1e1e2f')
width, height = 612, 512
image = PhotoImage(file="logoge.png").zoom(20).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#1e1e2f', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg='#1e1e2f')

app_name_label = Label(right_frame, text="Nom de l'application", font=("Arial", 18, "bold"), bg='#1e1e2f', fg='#f1f1f1')
app_name_label.pack(pady=(10, 5))

app_name_entry = Entry(right_frame, font=("Arial", 18), bg='#2c2c3e', fg='#f1f1f1', insertbackground='white', borderwidth=2, relief="groove")
app_name_entry.pack(pady=(0, 15), ipady=5)

password_label = Label(right_frame, text="Mot de passe", font=("Arial", 18, "bold"), bg='#1e1e2f', fg='#f1f1f1')
password_label.pack(pady=(15, 5))

password_entry = Entry(right_frame, font=("Arial", 18), bg='#2c2c3e', fg='#f1f1f1', insertbackground='white', borderwidth=2, relief="groove")
password_entry.pack(pady=(0, 15), ipady=5)

generate_password_button = Button(
    right_frame, text="Générer mon mot de passe",
    font=("Arial", 18, "bold"), bg='#3b8d99', fg='white', activebackground='#4fa7b2', activeforeground='white', command=Noah_generate_password
)
generate_password_button.pack(fill=X, pady=(10, 20))

right_frame.grid(row=0, column=1, sticky=W)
frame.pack(expand=YES)

Noah_BarMenu = Menu(window)
Noah_FileMenu = Menu(Noah_BarMenu, tearoff=0, bg='#2c2c3e', fg='#f1f1f1')
Noah_FileMenu.add_command(label="Nouveau mot de passe", command=Noah_generate_password)
Noah_FileMenu.add_command(label="Mes liens")
Noah_FileMenu.add_command(label="Quitter", command=window.quit)
Noah_BarMenu.add_cascade(label="Fichier", menu=Noah_FileMenu)
window.config(menu=Noah_BarMenu)

window.mainloop()
