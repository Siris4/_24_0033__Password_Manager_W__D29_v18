from tkinter import *   #imports JUST about everything except for MessageBoxes, etc.. (eveyrthing = classes, constants)
from tkinter import messagebox

#constants:
my_dummy_email = "test2.omego2000@yahoo.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Challenge: Add button that will: add, and append (on the next line) the: website URL, the user's email, and user made Password to a file called: "data29_01.txt" (formatting as csv with commas)

#tk insert

#to remove ONLY the website URL and the Password:
#tk delete

def save():
    get_website_url = website_entry.get()
    get_email_username = email_username_entry.get()
    get_password = password_entry.get()

    messagebox.showinfo(title="Title", message="Hello, I know you hate pop-up boxes, but here I am. Here to annoy you anyhow.")

    with open("data29_01.txt", mode="a") as data_file:    # OR data_file = open("data29_01.txt", mode="a"):  # data_file.close(), but our current code line, we do not have to use the .close() code bit afterwards.
        contents = data_file.write(f"{get_website_url}, {get_email_username}, {get_password}\n")
        # print(contents)    # anything you want to write here
        # anything you want to write here

    website_entry.delete(0, END)    #or (0, 'end')
    password_entry.delete(0, END)    #or (0, 'end')

# ---------------------------- UI SETUP ------------------------------- #


# Window Setup:
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas Widget:
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(107, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Website label:
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

# Website Entry:
website_entry = Entry(width=52)
# website_entry.insert(END, string="Enter website URL here! ")
website_entry.grid(row=1, column=1, columnspan=2)    #columnspan=2 is a keyword argument.
website_entry.focus() #If you want to start the blinking cursor on the first Entry text box field, then you would get ahold of the website_entry and use a Method on it called: .focus() and you would place it right after the .grid() method, of the Entry block we want it to Only apply to.


#############

# Email/Username label:
email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

# Email/Username Entry:
email_username_entry = Entry(width=52)
email_username_entry.insert(END, my_dummy_email)
email_username_entry.grid(row=2, column=1, columnspan=2)

#############

# Password label:
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Password Entry:
password_entry = Entry(width=33)
password_entry.insert(END, string="Enter your Password here, or --> ")
password_entry.grid(row=3, column=1)

# Generate Password button:
def generate_pass_action():
    print("Generate Password Button was Clicked.")

generate_password_button = Button(text="Generate Password", command=generate_pass_action, width=15)
generate_password_button.grid(row=3, column=2, columnspan=2)


# Add button:
def add_password_action():
    print("Add Password Button was Clicked.")
    # save()

add_button = Button(text="Add", command=save, width=45)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()