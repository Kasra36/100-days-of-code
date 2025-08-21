from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
FONT = ("Comic Sans MS", 10, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [(choice(letters)) for char in range(randint(2, 4))] + [(choice(numbers)) for char in range(randint(8, 10))] + [(choice(symbols)) for char in range(randint(2, 4))]

    shuffle(password_list)

    strong_password = "".join(password_list)

    password_entry.insert(0, strong_password)

    pyperclip.copy(strong_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = user_entry.get()
    password = password_entry.get()

    if len(website) != 0 and len(password) != 0:
        
        confirmed = messagebox.askyesno(title=website, message=f"Do you confirm?\nUsername: {username}\nPassword: {password}")
        
        if confirmed: 
            with open("data.txt", mode="a") as f:
                f.write(f"{website} | {username} | {password}\n")
        
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    
    else:
        messagebox.showerror(title="Input Error", message="Do not leave any fields empty")
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", font=FONT)
user_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


user_entry = Entry(width=40)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "@gmail.com")

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttoms
generate_buttom = Button(text="Generate Password", font=FONT, width=15, command=generate_password)
generate_buttom.grid(column=2, row=3)

add_buttom = Button(text="Add", font=FONT, width=30, command=save)
add_buttom.grid(column=1, row=4, columnspan=2)


window.mainloop()
