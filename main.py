import tkinter as tk
from tkinter import ttk
import random
import pyperclip as pc

# -------------- Hilfsfunktionen für Passwörter --------------

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_punct=True):
    """
    Erstellt ein zufälliges Passwort mit gewünschter Länge und Zeichentypen.
    """
    chars = ''
    if use_upper:
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_lower:
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if use_digits:
        chars += '0123456789'
    if use_punct:
        chars += '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    if not chars:
        return ''
    # Mindestens je ein Zeichen pro Kategorie
    password = []
    if use_upper:
        password.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if use_lower:
        password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
    if use_digits:
        password.append(random.choice('0123456789'))
    if use_punct:
        password.append(random.choice('!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
    # Rest auffüllen
    while len(password) < length:
        password.append(random.choice(chars))
    random.shuffle(password)
    return ''.join(password)

# -------------- GUI Funktionen --------------

def update_password_display():
    """
    Zeigt das generierte Passwort im Label an.
    """
    strength = strength_var.get()
    if strength == 1:
        pw = generate_password(8, True, True, True, True)      # Schwach: 8 Zeichen
    elif strength == 2:
        pw = generate_password(12, True, True, True, True)     # Normal: 12 Zeichen
    else:
        pw = generate_password(16, True, True, True, True)     # Stark: 16 Zeichen
    password_var.set(pw)

def copy_password(event=None):
    """
    Kopiert das aktuell angezeigte Passwort in die Zwischenablage.
    """
    pc.copy(password_var.get())

# -------------- Hauptfenster und Tabs --------------

root = tk.Tk()
root.geometry("400x350")
root.resizable(False, False)
root.title("Password Generator")

tabControl = ttk.Notebook(root)
pwgen_frame = ttk.Frame(tabControl)
pwlist_frame = ttk.Frame(tabControl)
tabControl.add(pwgen_frame, text='PW Generator')
tabControl.add(pwlist_frame, text='PW List')
tabControl.pack(expand=1, fill="both")

# -------------- Passwort Generator Tab --------------

# Begrüßung
tk.Label(pwgen_frame, text="Willkommen im Password Generator :)", font=('times', 15, 'bold', 'italic')).place(x=35, y=10)

# Sicherheitsstufe-Label
tk.Label(pwgen_frame, text="Wählen Sie eine Sicherheitsstufe!", padx=20, font=('times', 12, 'bold', 'italic')).place(x=70, y=72)

# Radiobuttons für Sicherheitsstufe
strength_var = tk.IntVar(value=1)
tk.Radiobutton(pwgen_frame, text="Schwach", value=1, variable=strength_var).place(x=70, y=115)
tk.Radiobutton(pwgen_frame, text="Normal", value=2, variable=strength_var).place(x=175, y=115)
tk.Radiobutton(pwgen_frame, text="Stark", value=3, variable=strength_var).place(x=270, y=115)

# Passwort-Anzeige
password_var = tk.StringVar(value="")
password_label = tk.Label(pwgen_frame, bg="lightgray", justify="center", textvariable=password_var, font=('times', 20))
password_label.place(x=75, y=200, width=250)
password_label.bind("<Button-3>", copy_password)  # Rechtsklick kopiert Passwort

# Copy-Button
copy_btn = tk.Button(pwgen_frame, bg="green", text="Copy", command=copy_password, cursor='hand2')
copy_btn.place(x=268, y=160, width=50, height=30)

# Passwort generieren Button
generate_btn = tk.Button(
    pwgen_frame,
    bg='#FBD975',
    text="Password Generieren",
    cursor='hand2',
    command=update_password_display,
    padx=25
)
generate_btn.place(x=85, y=160, width=180, height=30)

# -------------- Passwort Liste Tab --------------

tk.Label(
    pwlist_frame,
    text="Passwort Liste",
    justify="center",
    padx=20,
    font=('times', 15, 'bold', 'italic')
).pack(pady=20)

# Hier könntest du z.B. ein Textfeld einfügen, das Passwörter speichert

# -------------- Footer --------------

tk.Label(root, text="© Copyright by DravenSoft since 2021", font=("Arial", 9)).pack(side="bottom", pady=2)

# -------------- Mainloop --------------

root.mainloop()
# Ende des Programms
# Hinweis: Dieses Programm ist ein einfaches Beispiel und sollte nicht für echte Sicherheitsanwendungen verwendet werden.