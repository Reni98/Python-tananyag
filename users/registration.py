from mysql.connector import Error
import random
import tkinter
from tkinter import *
import myconnection
from tkinter import messagebox

# Adatbázis kapcsolat
conn = myconnection.conn

frame = tkinter.Tk()

frame.title("Regisztráció")
frame.configure(bg="#ff5733")
frame.geometry("400x500")

# Felhasználónév címke és beviteli mező
lbl_username = Label(frame, text="Felhasználónév:", font=("Raleway", 14, "bold"), bg="#ff5733")
lbl_username.place(x=15, y=15)
txt_username = Entry(frame, width=20, font=("Raleway", 15))
txt_username.place(x=130, y=15)

# Jelszó címke és beviteli mező
lbl_password = Label(frame, text="Jelszó:", font=("Raleway", 14, "bold"), bg="#ff5733")
lbl_password.place(x=15, y=60)
txt_password = Entry(frame, width=20, font=("Raleway", 15), show="*")
txt_password.place(x=130, y=55)

lbl_firstname = Label(frame, text="Keresztnév:", font=("Raleway", 14, "bold"), bg="#ff5733")
lbl_firstname.place(x=15, y=90)
txt_firstname = Entry(frame, width=20, font=("Raleway", 15))
txt_firstname.place(x=130, y=95)

lbl_lastname = Label(frame, text="Vezetéknév:", font=("Raleway", 14, "bold"), bg="#ff5733")
lbl_lastname.place(x=15, y=135)
txt_lastname = Entry(frame, width=20, font=("Raleway", 15))
txt_lastname.place(x=130, y=135)

# Regisztrációs függvény
def register():
    id_number = random.randint(100, 9999)
    username = txt_username.get().strip()
    password = txt_password.get().strip()
    firstname = txt_firstname.get().strip()
    lastname = txt_lastname.get().strip()

    try:
        if conn.is_connected():
            pst = conn.cursor()
            sql_query = '''
                INSERT INTO felhasznalo (user_id, user_firstname, user_lastname, username, user_password) 
                VALUES (%s, %s, %s, %s, %s)
            '''
            pst.execute(sql_query, (id_number, firstname, lastname, username, password))
            conn.commit()
            messagebox.showinfo("Regisztráció", "Sikeres volt a regisztráció")
        else:
            messagebox.showerror("Hiba", "Nem sikerült csatlakozni az adatbázishoz.")
    except Error as e:
        messagebox.showerror("Hiba", f"Hiba történt: {e}")
    finally:
        if 'pst' in locals():
            pst.close()

# Regisztráció gomb
button_login = Button(frame, text="Regisztráció", height=2, width=15, command=register)
button_login.place(x=260, y=200)

frame.mainloop()
