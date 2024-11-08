import string
from random import randint, choice
from tkinter import *

def Noah_generate_password():
    length = int(length_var.get())
    include_special_chars = special_chars_var.get()

    # Crée une liste de caractères en fonction du choix de l'utilisateur
    all_chars = string.ascii_letters + string.digits
    if include_special_chars:
        all_chars += string.punctuation

    # Génère le mot de passe
    password = "".join(choice(all_chars) for _ in range(length))
    
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

# Configuration de l'interface
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

# Champ pour le nom de l'application
app_name_label = Label(right_frame, text="Nom de l'application", font=("Arial", 18, "bold"), bg='#1e1e2f', fg='#f1f1f1')
app_name_label.pack(pady=(10, 5))

app_name_entry = Entry(right_frame, font=("Arial", 18), bg='#2c2c3e', fg='#f1f1f1', insertbackground='white', borderwidth=2, relief="groove")
app_name_entry.pack(pady=(0, 15), ipady=5)

# Menu déroulant pour la longueur du mot de passe
length_label = Label(right_frame, text="Longueur du mot de passe", font=("Arial", 18, "bold"), bg='#1e1e2f', fg='#f1f1f1')
length_label.pack(pady=(15, 5))

length_var = StringVar(value="12")
length_menu = OptionMenu(right_frame, length_var, *[str(i) for i in range(10, 51)])
length_menu.config(font=("Arial", 14), bg='#2c2c3e', fg='#f1f1f1', highlightthickness=0)
length_menu.pack(pady=(0, 15))

# Case à cocher pour inclure les caractères spéciaux
special_chars_var = BooleanVar(value=True)
special_chars_check = Checkbutton(
    right_frame, text="Inclure des caractères spéciaux", 
    variable=special_chars_var, font=("Arial", 14), bg='#1e1e2f', fg='#f1f1f1', 
    selectcolor='#2c2c3e', activebackground='#1e1e2f', activeforeground='#f1f1f1'
)
special_chars_check.pack(pady=(0, 15))

# Champ pour afficher le mot de passe généré
password_label = Label(right_frame, text="Mot de passe", font=("Arial", 18, "bold"), bg='#1e1e2f', fg='#f1f1f1')
password_label.pack(pady=(15, 5))

password_entry = Entry(right_frame, font=("Arial", 18), bg='#2c2c3e', fg='#f1f1f1', insertbackground='white', borderwidth=2, relief="groove")
password_entry.pack(pady=(0, 15), ipady=5)

# Bouton de génération de mot de passe
generate_password_button = Button(
    right_frame, text="Générer mon mot de passe",
    font=("Arial", 18, "bold"), bg='#3b8d99', fg='white', activebackground='#4fa7b2', activeforeground='white', command=Noah_generate_password
)
generate_password_button.pack(fill=X, pady=(10, 20))

right_frame.grid(row=0, column=1, sticky=W)
frame.pack(expand=YES)

# Menu
Noah_BarMenu = Menu(window)
Noah_FileMenu = Menu(Noah_BarMenu, tearoff=0, bg='#2c2c3e', fg='#f1f1f1')
Noah_FileMenu.add_command(label="Nouveau mot de passe", command=Noah_generate_password)
Noah_FileMenu.add_command(label="Mes liens")
Noah_FileMenu.add_command(label="Quitter", command=window.quit)
Noah_BarMenu.add_cascade(label="Fichier", menu=Noah_FileMenu)
window.config(menu=Noah_BarMenu)

window.mainloop()
