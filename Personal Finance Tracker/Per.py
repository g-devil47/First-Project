import tkinter as tk
from tkinter import ttk
import os
import pandas as pd

def save_credentials():
    users_name = entry_name.get()
    username = entry_username.get()
    users_password = entry_password.get()
    users_email_id = entry_email.get()
    users_phone_number = entry_phone.get()

    result_label.config(text=f"{users_name}, Your Credentials have been Successfully Saved!")

    # Create a folder with the user's name
    folder_path = f"./{users_name}"
    os.makedirs(folder_path, exist_ok=True)

    # Create an Excel file or use an existing one
    excel_file_path = f"{folder_path}/credentials.xlsx"

    if os.path.exists(excel_file_path):
        # If the file exists, read the existing data
        existing_data = pd.read_excel(excel_file_path)
        
        # Append the new data to the existing DataFrame
        new_data = {
            "Name": [users_name],
            "Username": [username],
            "Password": [users_password],
            "Email": [users_email_id],
            "Phone Number": [users_phone_number]
        }

        df = pd.concat([existing_data, pd.DataFrame(new_data)], ignore_index=True)
    else:
        # If the file doesn't exist, create a new DataFrame
        user_data = {
            "Name": [users_name],
            "Username": [username],
            "Password": [users_password],
            "Email": [users_email_id],
            "Phone Number": [users_phone_number]
        }

        df = pd.DataFrame(user_data)

    # Write the DataFrame to an Excel sheet
    with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='User_Signed_Up', index=False)

# Create the main window
window = tk.Tk()
window.title("Credentials Form")

# Dark mode theme configuration
style = ttk.Style()
style.theme_use("clam")  # You can experiment with different themes
style.configure("TLabel", background="#282c34", foreground="white")
style.configure("TEntry", fieldbackground="#282c34", foreground="white")
style.configure("TButton", background="#61dafb", foreground="black")
style.configure("TFrame", background="#282c34")
style.map("TButton", background=[("active", "#51a0ff")])

# Set the background color for the root window
window.configure(bg="#282c34")

# Create and place widgets
questions = [
    "Please Enter your Name:",
    "Please Enter a Username:",
    "Please Enter a Password:",
    "Please provide Your Email id:",
    "Please provide Your Phone Number:"
]

entry_frames = []
entry_name = entry_username = entry_password = entry_email = entry_phone = None  # Initialize entry variables

for i, question in enumerate(questions):
    frame = ttk.Frame(window, padding=(10, 5), style="TFrame")
    frame.pack(anchor=tk.CENTER)

    label = ttk.Label(frame, text=question, style="TLabel")
    label.pack(side=tk.LEFT)

    entry = ttk.Entry(frame, style="TEntry")
    entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Assign entry variables based on the question
    if "Name" in question:
        entry_name = entry
    elif "Username" in question:
        entry_username = entry
    elif "Password" in question:
        entry_password = entry
    elif "Email" in question:
        entry_email = entry
    elif "Phone Number" in question:
        entry_phone = entry

    entry_frames.append(frame)

save_button = ttk.Button(window, text="Save Credentials", command=save_credentials)
save_button.pack(pady=10)

result_label = ttk.Label(window, text="", style="TLabel")
result_label.pack()

# Set window size and position
window_width = 1280  # 720p width
window_height = 720  # 720p height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Disable window resizing
window.resizable(False, False)

# Run the Tkinter event loop
window.mainloop()
