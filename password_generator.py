import string
from random import choice, shuffle
import tkinter as tk
from tkinter import messagebox


BG = "#0a0a0f"
SURFACE = "#12121a"
CARD = "#1a1a28"
BORDER = "#2a2a3d"
ACCENT = "#7c3aed"
ACCENT2 = "#a855f7"
GLOW = "#c084fc"
TEXT = "#f0f0ff"
MUTED = "#6b7280"
SUCCESS = "#10b981"
ERROR = "#ef4444"
WHITE = "#ffffff"


def generate_password():
    try:
        length = int(float(length_var.get()))

        chars = string.ascii_lowercase
        required = []

        if uppercase_var.get():
            chars += string.ascii_uppercase
            required.append(choice(string.ascii_uppercase))
        if numbers_var.get():
            chars += string.digits
            required.append(choice(string.digits))
        if special_var.get():
            chars += string.punctuation
            required.append(choice(string.punctuation))

        if not chars:
            set_status("Sélectionne au moins un type de caractère", ERROR)
            return

        remaining = [choice(chars) for _ in range(length - len(required))]
        all_chars = required + remaining
        shuffle(all_chars)
        password = "".join(all_chars)

        password_var.set(password)
        password_entry.config(fg=GLOW)

        update_strength(password)

        app_name = app_entry.get().strip()
        if app_name:
            try:
                with open("mesmotdepasse.txt", "a", encoding="utf-8") as f:
                    f.write(f"{app_name} : {password}\n")
                set_status("✓  Mot de passe sauvegardé", SUCCESS)
            except IOError:
                set_status("Erreur lors de la sauvegarde", ERROR)
        else:
            set_status("⚠  Entre un nom de service pour sauvegarder", GLOW)

        animate_button()

    except ValueError:
        set_status("Longueur invalide", ERROR)


def update_strength(pwd):
    score = 0
    if len(pwd) >= 12: score += 1
    if len(pwd) >= 20: score += 1
    if any(c in string.ascii_uppercase for c in pwd): score += 1
    if any(c in string.digits for c in pwd): score += 1
    if any(c in string.punctuation for c in pwd): score += 1

    labels = ["Très faible", "Faible", "Moyen", "Fort", "Très fort", "Extrême"]
    colors = [ERROR, "#f97316", "#eab308", "#3b82f6", SUCCESS, GLOW]

    strength_label.config(text=labels[score], fg=colors[score])

    for i, bar in enumerate(strength_bars):
        if i < score:
            bar.config(bg=colors[score])
        else:
            bar.config(bg=BORDER)


def copy_password():
    pwd = password_var.get()
    if not pwd:
        set_status("Aucun mot de passe à copier", ERROR)
        return
    window.clipboard_clear()
    window.clipboard_append(pwd)
    set_status("✓  Copié dans le presse-papier", SUCCESS)


def set_status(msg, color):
    status_label.config(text=msg, fg=color)
    window.after(3000, lambda: status_label.config(text=""))


def animate_button():
    gen_btn.config(text="✓  Généré !", bg=SUCCESS)
    window.after(1500, lambda: gen_btn.config(text="⚡  Générer", bg=ACCENT))


def update_length_label(val):
    v = int(float(val))
    length_display.config(text=str(v))


def on_closing():
    if messagebox.askokcancel("Quitter", "Fermer Gen Password ?"):
        window.destroy()


window = tk.Tk()
window.title("Gen Password")
window.geometry("720x820")
window.resizable(False, False)
window.configure(bg=BG)
window.protocol("WM_DELETE_WINDOW", on_closing)

try:
    window.tk.call("tk", "scaling", 1.2)
except Exception:
    pass


outer = tk.Frame(window, bg=BG)
outer.pack(fill="both", expand=True, padx=40, pady=32)


header = tk.Frame(outer, bg=BG)
header.pack(fill="x", pady=(0, 20))

tk.Label(header, text="GEN", font=("Courier", 42, "bold"), bg=BG, fg=WHITE).pack(side="left")
tk.Label(header, text="PASSWORD", font=("Courier", 42, "bold"), bg=BG, fg=ACCENT2).pack(side="left")

tk.Label(header, text="par Noah  •  22/06/22", font=("Courier", 9),
         bg=BG, fg=MUTED).pack(side="right", anchor="s", pady=(16, 0))


def card(parent, pady=(0, 16)):
    f = tk.Frame(parent, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
    f.pack(fill="x", pady=pady)
    inner = tk.Frame(f, bg=CARD)
    inner.pack(fill="x", padx=16, pady=14)
    return inner


c1 = card(outer)
tk.Label(c1, text="SERVICE", font=("Courier", 9, "bold"), bg=CARD, fg=MUTED).pack(anchor="w")
app_entry = tk.Entry(c1, font=("Courier", 14), bg=SURFACE, fg=TEXT,
                     insertbackground=ACCENT2, relief="flat", bd=0)
app_entry.pack(fill="x", pady=(6, 0), ipady=6)
app_entry.insert(0, "ex: GitHub, Gmail…")
app_entry.bind("<FocusIn>", lambda e: app_entry.delete(0, "end") if app_entry.get().startswith("ex:") else None)


c2 = card(outer)
top = tk.Frame(c2, bg=CARD)
top.pack(fill="x")
tk.Label(top, text="LONGUEUR", font=("Courier", 9, "bold"), bg=CARD, fg=MUTED).pack(side="left")
length_display = tk.Label(top, text="16", font=("Courier", 13, "bold"), bg=CARD, fg=ACCENT2)
length_display.pack(side="right")

length_var = tk.StringVar(value="16")
slider = tk.Scale(c2, from_=6, to=48, orient="horizontal", variable=length_var,
                  command=update_length_label, showvalue=False,
                  bg=CARD, troughcolor=BORDER, activebackground=ACCENT,
                  highlightthickness=0, sliderrelief="flat",
                  fg=TEXT, bd=0, sliderlength=18)
slider.pack(fill="x", pady=(8, 0))


c3 = card(outer)
tk.Label(c3, text="COMPOSITION", font=("Courier", 9, "bold"), bg=CARD, fg=MUTED).pack(anchor="w", pady=(0, 8))

special_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)

def styled_check(parent, text, var):
    f = tk.Frame(parent, bg=CARD)
    f.pack(fill="x", pady=3)
    cb = tk.Checkbutton(f, text=text, variable=var,
                        font=("Courier", 11), bg=CARD, fg=TEXT,
                        selectcolor=ACCENT, activebackground=CARD,
                        activeforeground=TEXT, relief="flat",
                        highlightthickness=0, cursor="hand2")
    cb.pack(anchor="w")

styled_check(c3, "Majuscules  A – Z", uppercase_var)
styled_check(c3, "Chiffres      0 – 9", numbers_var)
styled_check(c3, "Symboles   ! @ # …", special_var)


c4 = card(outer)
top2 = tk.Frame(c4, bg=CARD)
top2.pack(fill="x")
tk.Label(top2, text="MOT DE PASSE", font=("Courier", 9, "bold"), bg=CARD, fg=MUTED).pack(side="left")
strength_label = tk.Label(top2, text="", font=("Courier", 9, "bold"), bg=CARD, fg=MUTED)
strength_label.pack(side="right")

password_var = tk.StringVar()
password_entry = tk.Entry(c4, textvariable=password_var, font=("Courier", 17, "bold"),
                          bg=SURFACE, fg=GLOW, insertbackground=ACCENT2,
                          relief="flat", bd=0, state="normal")
password_entry.pack(fill="x", pady=(8, 10), ipady=8)

bars_frame = tk.Frame(c4, bg=CARD)
bars_frame.pack(fill="x")
strength_bars = []
for _ in range(5):
    b = tk.Frame(bars_frame, bg=BORDER, height=6, width=80)
    b.pack(side="left", padx=2)
    strength_bars.append(b)


btn_row = tk.Frame(outer, bg=BG)
btn_row.pack(fill="x", pady=(4, 0))

gen_btn = tk.Button(btn_row, text="⚡  Générer", font=("Courier", 15, "bold"),
                    bg=ACCENT, fg=WHITE, relief="flat", cursor="hand2",
                    activebackground=ACCENT2, activeforeground=WHITE,
                    command=generate_password, pady=12)
gen_btn.pack(side="left", fill="x", expand=True, padx=(0, 8))

copy_btn = tk.Button(btn_row, text="📋", font=("Courier", 15),
                     bg=CARD, fg=TEXT, relief="flat", cursor="hand2",
                     activebackground=BORDER, activeforeground=WHITE,
                     command=copy_password, pady=12, width=4,
                     highlightbackground=BORDER, highlightthickness=1)
copy_btn.pack(side="right")


status_label = tk.Label(outer, text="", font=("Courier", 10),
                        bg=BG, fg=SUCCESS)
status_label.pack(pady=(10, 0))


footer = tk.Frame(outer, bg=BG)
footer.pack(side="bottom", fill="x", pady=(16, 0))
tk.Frame(footer, bg=BORDER, height=1).pack(fill="x", pady=(0, 10))
tk.Label(footer, text="© 2025 Gen Password  —  Tous droits réservés",
         font=("Courier", 8), bg=BG, fg=MUTED).pack()


window.mainloop()