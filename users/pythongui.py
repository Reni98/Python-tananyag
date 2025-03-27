import tkinter
from tkinter import *
from PIL import Image, ImageTk  # A képkezeléshez szükséges

import myconnection
from tkinter import messagebox

# Adatbázis kapcsolat
conn = myconnection.conn

frame = tkinter.Tk()
frame.title("Bejelentkezés")
frame.configure(bg="#ff5733")
frame.geometry("400x170")

# Felhasználónév címke és beviteli mező
lbl_username = Label(frame, text="Felhasználónév:", font=("Raleway", 14, "bold"), bg="#ff5733")
lbl_username.place(x=15, y=15)
txt_username = Entry(frame, width=20, font=("Raleway", 15))
txt_username.place(x=130, y=15)

# Jelszó címke és beviteli mező
lbl_password = Label(frame, text="Jelszó:", font=("Raleway", 14, "bold"), bg="#ff5733")
lbl_password.place(x=15, y=60)
txt_password = Entry(frame, width=20, font=("Raleway", 15), show="*")
txt_password.place(x=130, y=60)

# Bejelentkezési függvény
def user_login():
    username = txt_username.get().strip()
    password = txt_password.get().strip()

    if username == "" or password == "":
        messagebox.showinfo("Error", "Kérlek add meg a felhasználónevet és a jelszót")
        return

    if conn.is_connected():
        try:
            pst = conn.cursor()
            sql_query = 'SELECT user_firstname FROM felhasznalo WHERE username=%s AND user_password=%s'
            pst.execute(sql_query, (username, password))
            rs = pst.fetchone()

            if rs is None:
                messagebox.showinfo("Error", "Hibás felhasználónév vagy jelszó!")
            else:
                firstname = rs[0]  # Keresztnév lekérdezése
                messagebox.showinfo("Login", "Sikeres bejelentkezés!")
                frame.destroy()  # A jelenlegi bejelentkezési ablak bezárása
                open_welcome_window(firstname)  # Megnyitjuk az új ablakot

        except Exception as e:
            messagebox.showerror("Hiba", f"Valami hiba történt: {e}")

        finally:
            pst.close()  # Kurzort lezárni!

# Üdvözlőablak megnyitása
def open_welcome_window(firstname):
    welcome_window = Tk()
    welcome_window.title("Üdvözlünk!")
    welcome_window.geometry("350x250")
    welcome_window.configure(bg="#85C1E9")

    # Kép betöltése
    image = Image.open("profil.png")  # A kép elérési útja
    image = image.resize((100, 100))  # Kép méretezése
    photo = ImageTk.PhotoImage(image)

    lbl_image = Label(welcome_window, image=photo, bg="#85C1E9")
    lbl_image.image = photo  # Fontos, hogy megőrizzük a referenciát
    lbl_image.pack(pady=10)

    # Üdvözlőszöveg
    lbl_welcome = Label(welcome_window, text=f"Szia {firstname}!", font=("Raleway", 16, "bold"), bg="#85C1E9")
    lbl_welcome.pack(pady=10)

    welcome_window.mainloop()

# Bejelentkezés gomb
button_login = Button(frame, text="Login", height=2, width=15, command=user_login)
button_login.place(x=260, y=110)

frame.mainloop()
