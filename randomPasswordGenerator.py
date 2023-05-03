import ttkbootstrap as ttk
import ttkbootstrap.dialogs
from ttkbootstrap.constants import *
import string
import random
import pyperclip
from ttkbootstrap.tooltip import ToolTip


def generate_password():
    # Create string of characters based on selected options
    characters = ""
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if special_char_var.get():
        characters += string.punctuation
    if numbers_var.get():
        characters += string.digits

    # Determine password length based on radio button selection
    if password_length_var.get() == "easy":
        password_length = 6
    elif password_length_var.get() == "medium":
        password_length = 12
    elif password_length_var.get() == "hard":
        password_length = 18

    # Generate password and display on label
    if characters:
        password = "".join(random.choice(characters) for i in range(password_length))
        generated_password_label.config(text="Generated Password: "+password)
    else:
        generated_password_label.config(text="Please select at least one option.")


def confirm_quit():
    response  = ttkbootstrap.dialogs.Messagebox.yesno("Are you sure you want to exit?", "Exit Window", alert=True)
    if response == "Yes":
        root.destroy()


def copyPassword():
    generatedPass = generated_password_label.cget("text")
    if generatedPass:
        generatedPass = generatedPass.split(":")[1]
        try:
            pyperclip.copy(generatedPass)
        except Exception as e:
            pass
    else:
        ttkbootstrap.dialogs.Messagebox.show_error("failed to copy password", "generated password not found", alert=True)


root = ttk.Window(themename="superhero")
root.geometry("650x450+400+100")
root.title("Password Generator APP")

topLabel = ttk.Label(root, text="Generate Random Password", font=('helecia', 16))
topLabel.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

# Checkboxes for password options
uppercase_var = ttk.BooleanVar()
lowercase_var = ttk.BooleanVar()
special_char_var = ttk.BooleanVar()
numbers_var = ttk.BooleanVar()

uppercase_check = ttk.Checkbutton(root, text="Uppercase Letters", variable=uppercase_var,bootstyle="success")
lowercase_check = ttk.Checkbutton(root, text="Lowercase Letters", variable=lowercase_var,bootstyle="success")
special_char_check = ttk.Checkbutton(root, text="Special Characters", variable=special_char_var,bootstyle="success")
numbers_check = ttk.Checkbutton(root, text="Include Numbers", variable=numbers_var,bootstyle="success")

uppercase_check.grid(row=1, column=0, padx=10, pady=5, sticky=ttk.W)
lowercase_check.grid(row=1, column=1, padx=10, pady=5, sticky=ttk.W)
special_char_check.grid(row=2, column=0, padx=10, pady=5, sticky=ttk.W)
numbers_check.grid(row=2, column=1, padx=10, pady=5, sticky=ttk.W)

# Radio buttons for password length
password_length_var = ttk.StringVar(value="easy")
password_length_label = ttk.Label(root, text="Select password length", font=("helecia", 16))
password_length_label.grid(row=3, column=0, padx=10, pady=10,columnspan=3)

easy_radio = ttk.Radiobutton(root, text="Easy (6 Characters)", variable=password_length_var,
                                 value="easy",bootstyle="info")
medium_radio = ttk.Radiobutton(root, text="Medium (12 Characters)",
                                   variable=password_length_var, value="medium",bootstyle="success")
hard_radio = ttk.Radiobutton(root, text="Hard (18 Characters)", variable=password_length_var,
                                 value="hard",bootstyle="danger")

easy_radio.grid(row=4, column=0, padx=10, pady=5, sticky=ttk.W)
medium_radio.grid(row=4, column=1, padx=10, pady=5, sticky=ttk.W)
hard_radio.grid(row=5, column=0, padx=10, pady=5, sticky=ttk.W)

# Generated password label
generated_password_label = ttk.Label(root, text="", font=("Arial", 14), width=40,anchor=ttk.CENTER,bootstyle="danger")
generated_password_label.grid(row=6, column=0, padx=5, pady=30,columnspan=4)

# copy button
copyButton = ttk.Button(root, text="Copy Password",bootstyle=("info","outline"),command=copyPassword)
copyButton.grid(row=7, column=1, padx=10, pady=20,columnspan=1)
ToolTip(copyButton, text="Copy Password to Clipboard",bootstyle=("warning","inverse"))

# Buttons to generate or cancel password
generate_button = ttk.Button(root, text="Generate",command=generate_password,bootstyle=(SUCCESS, OUTLINE))
cancel_button = ttk.Button(root, text="Cancel", command=confirm_quit,bootstyle=(DANGER, OUTLINE))

generate_button.grid(row=7, column=0, padx=5, pady=10)
cancel_button.grid(row=7, column=2, padx=15, pady=10,columnspan=1)


root.mainloop()
