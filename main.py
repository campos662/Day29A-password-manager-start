import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #password_list = []

    password_letters = [random.choice(letters) for x in range(nr_letters)]

    #for char in range(nr_letters):
     # password_list.append(random.choice(letters))

    password_symbols = [random.choice(symbols) for y in range(nr_symbols)]

    #for char in range(nr_symbols):
     # password_list += random.choice(symbols)

    password_numbers = [random.choice(numbers) for z in range(nr_numbers)]

    #for char in range(nr_numbers):
     # password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    #password = ""
    #for char in password_list:
     # password += char

    password = "".join(password_list)

    password_output.insert(0, password)
    pyperclip.copy(password)


    #print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_input = str(website_input.get())
    us_input = str(user_input.get())
    pass_input = str(password_output.get())
    new_data = {
        web_input: {
            "email": us_input,
            "password": pass_input,

        }
    }
    if web_input == "" or us_input == "" or pass_input == "":
        messagebox.showerror(title="Some fields are empty!!", message="You must complete all fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_output.delete(0, END)

# ---------------------------- Find password ------------------------------- #

def find_password():
    try:
        web_input = str(website_input.get())
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        email = data[web_input]["email"]
        password = data[web_input]["password"]
        user_input.delete(0, END)
        password_output.delete(0, END)
        user_input.insert(0, email)
        password_output.insert(0, password)
    except KeyError:
        tkinter.messagebox.showerror(title="Website not found!!", message="We haven't found the website you are looking for!!")
    except FileNotFoundError:
        tkinter.messagebox.showerror(title="No records available", message="You haven't populated any website yet")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager!!")
window.config(bg="white", pady= 50, padx= 50)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.config(bg="white", highlightthickness=0)
website_label.grid(column=0, row=1)


user_label = Label(text="Email/ User: ")
user_label.config(bg="white", highlightthickness=0)
user_label.grid(column=0, row=2)


password_label = Label(text="Password: ")
password_label.config(bg="white", highlightthickness=0)
password_label.grid(column=0, row=3)

website_input= Entry()
website_input.config(bg="white", highlightthickness=0, width=21)
website_input.grid(column=1, row=1)
website_input.focus()


user_input= Entry()
user_input.config(bg="white", highlightthickness=0, width=39)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0,"carlos@email.com")

password_output= Entry()
password_output.config(bg="white", highlightthickness=0, width=21)
password_output.grid(column=1, row=3,)

generate_button = Button(text="Generate Password", highlightthickness=0, command=password_generator)
#generate_button.config(bg="white")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=36, command=save)
#add_button.config(bg="white")
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search website", highlightthickness=0, width= 13, command=find_password)
#generate_button.config(bg="white")
search_button.grid(column=2, row=1)








window.mainloop()