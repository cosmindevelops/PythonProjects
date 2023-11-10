import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
               'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_char = [choice(letters) for _ in range(randint(8, 10))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]
    password_sym = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_char + password_num + password_sym

    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # Copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_and_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }}

    if not website or not email or not password:
        messagebox.showinfo(title='Invalid Operation', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as file:
                # Read json data
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                # Write updated json data
                json.dump(new_data, file, indent=4)
        else:
            # Update json data
            data.update(new_data)
            with open('data.json', 'w') as file:
                # Write updated json data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title='Success', message="Details saved successfully")


# ------------------------- SEARCH PASSWORD --------------------------- #

def search_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            try:
                email = data[website]['email']
                password = data[website]['password']
            except KeyError:
                messagebox.showinfo(title='Invalid website', message=f"There is no username or password for that website")
            else:
                if website in data:
                    messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message=f"No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #

# Window Setup
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canva Setup
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

# Label Setup
website_label = Label(text='Website')
website_label.grid(column=1, row=2)

email_and_username_label = Label(text='Email/Username:')
email_and_username_label.grid(column=1, row=3)

password_label = Label(text='Password')
password_label.grid(column=1, row=4)

# Entry Setup
website_entry = Entry(width=33)
website_entry.grid(column=2, row=2, pady=2)
website_entry.focus()

email_and_username_entry = Entry(width=52)
email_and_username_entry.grid(column=2, row=3, columnspan=2, pady=2)
email_and_username_entry.insert(0, 'andrew@gmail.com')

password_entry = Entry(width=33)
password_entry.grid(column=2, row=4, pady=2)

# Button Setup
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=3, row=4, padx=2, pady=2)

add_button = Button(text='Add', width=44, command=save_password)
add_button.grid(column=2, row=5, columnspan=2)

search_button = Button(text='Search', width=14, command=search_password)
search_button.grid(column=3, row=2)

window.mainloop()
