import tkinter as tk
from tkinter import ttk

# Function to submit the form
def submit_form():
    # Retrieve the values from the GUI widgets
    # Add your processing logic here
    pass

# Create the main window
root = tk.Tk()
root.title("User Information Form")

# Configure a dark theme
root.tk_setPalette(background='#2E2E2E', foreground='#FFFFFF', activeBackground='#004080', activeForeground='#FFFFFF')

# Age
tk.Label(root, text="Age:", background='#2E2E2E', foreground='#FFFFFF').pack()
age_entry = tk.Entry(root, background='#4D4D4D', foreground='#FFFFFF')
age_entry.pack()

# Educational Qualification
tk.Label(root, text="Educational Qualification:", background='#2E2E2E', foreground='#FFFFFF').pack()
qualification_var = tk.StringVar()
qualification_var.set("Select")
qualification_menu = tk.OptionMenu(root, qualification_var, "10th", "12th", "Graduation", "Post-Graduation", "Others")
qualification_menu.config(bg='#4D4D4D', fg='#FFFFFF', highlightbackground='#2E2E2E', activebackground='#0066cc', activeforeground='#FFFFFF')
qualification_menu.pack()

# Employment Status
tk.Label(root, text="Employment Status:", background='#2E2E2E', foreground='#FFFFFF').pack()
employment_status_var = tk.StringVar()
employment_status_var.set("Select")
employment_status_menu = tk.OptionMenu(root, employment_status_var, "Employed", "Unemployed")
employment_status_menu.config(bg='#4D4D4D', fg='#FFFFFF', highlightbackground='#2E2E2E', activebackground='#0066cc', activeforeground='#FFFFFF')
employment_status_menu.pack()

# Occupation and Monthly Income (if employed)
occupation_entry = tk.Entry(root, background='#4D4D4D', foreground='#FFFFFF')
income_entry = tk.Entry(root, background='#4D4D4D', foreground='#FFFFFF')
tk.Label(root, text="Occupation:", background='#2E2E2E', foreground='#FFFFFF').pack()
occupation_entry.pack()
tk.Label(root, text="Monthly Income:", background='#2E2E2E', foreground='#FFFFFF').pack()
income_entry.pack()

# Monthly Expenses, Outstanding Debt, Spending Habits
expenses_entry = tk.Entry(root, background='#4D4D4D', foreground='#FFFFFF')
debt_entry = tk.Entry(root, background='#4D4D4D', foreground='#FFFFFF')
habits_entry = tk.Entry(root, background='#4D4D4D', foreground='#FFFFFF')
tk.Label(root, text="Monthly Expenses:", background='#2E2E2E', foreground='#FFFFFF').pack()
expenses_entry.pack()
tk.Label(root, text="Outstanding Debts:", background='#2E2E2E', foreground='#FFFFFF').pack()
debt_entry.pack()
tk.Label(root, text="Spending Habits/Categories:", background='#2E2E2E', foreground='#FFFFFF').pack()
habits_entry.pack()

# Additional Source of Income
additional_income_var = tk.StringVar()
additional_income_var.set("Select")
additional_income_menu = tk.OptionMenu(root, additional_income_var, "Yes", "No")
additional_income_menu.config(bg='#4D4D4D', fg='#FFFFFF', highlightbackground='#2E2E2E', activebackground='#0066cc', activeforeground='#FFFFFF')
tk.Label(root, text="Additional Source of Income:", background='#2E2E2E', foreground='#FFFFFF').pack()
additional_income_menu.pack()

# Financial Goals
short_term_goal_entry = tk.Entry(root, background='#4D4D4D', foreground='#FFFFFF')
long_term_goal_entry = tk.Entry(root, background='#4D4D4D', foreground='#FFFFFF')
tk.Label(root, text="Short Term Financial Goals:", background='#2E2E2E', foreground='#FFFFFF').pack()
short_term_goal_entry.pack()
tk.Label(root, text="Long Term Financial Goals:", background='#2E2E2E', foreground='#FFFFFF').pack()
long_term_goal_entry.pack()

# Credit History
credit_history_var = tk.StringVar()
credit_history_var.set("Select")
credit_history_menu = tk.OptionMenu(root, credit_history_var, "Yes", "No")
credit_history_menu.config(bg='#4D4D4D', fg='#FFFFFF', highlightbackground='#2E2E2E', activebackground='#0066cc', activeforeground='#FFFFFF')

credit_cards_var = tk.StringVar()
credit_cards_var.set("Select")
credit_cards_menu = tk.OptionMenu(root, credit_cards_var, "Yes", "No")
credit_cards_menu.config(bg='#4D4D4D', fg='#FFFFFF', highlightbackground='#2E2E2E', activebackground='#0066cc', activeforeground='#FFFFFF')

credit_score_entry = tk.Entry(root, background='#4D4D4D', foreground='#FFFFFF')
tk.Label(root, text="Credit History:", background='#2E2E2E', foreground='#FFFFFF').pack()
credit_history_menu.pack()
tk.Label(root, text="Possession of Credit Cards:", background='#2E2E2E', foreground='#FFFFFF').pack()
credit_cards_menu.pack()
tk.Label(root, text="Credit Score:", background='#2E2E2E', foreground='#FFFFFF').pack()
credit_score_entry.pack()

# Investment
investment_var = tk.StringVar()
investment_var.set("Select")
investment_menu = tk.OptionMenu(root, investment_var, "Yes", "No")
investment_menu.config(bg='#4D4D4D', fg='#FFFFFF', highlightbackground='#2E2E2E', activebackground='#0066cc', activeforeground='#FFFFFF')
tk.Label(root, text="Are you investing?", background='#2E2E2E', foreground='#FFFFFF').pack()
investment_menu.pack()

# Emergency Fund
emergency_fund_var = tk.StringVar()
emergency_fund_var.set("Select")
emergency_fund_menu = tk.OptionMenu(root, emergency_fund_var, "Yes", "No")
emergency_fund_menu.config(bg='#4D4D4D', fg='#FFFFFF', highlightbackground='#2E2E2E', activebackground='#0066cc', activeforeground='#FFFFFF')
tk.Label(root, text="Emergency Fund:", background='#2E2E2E', foreground='#FFFFFF').pack()
emergency_fund_menu.pack()

# Money in Savings
saving_entry = tk.Entry(root, background='#4D4D4D', foreground='#FFFFFF')
tk.Label(root, text="Money in Savings:", background='#2E2E2E', foreground='#FFFFFF').pack()
saving_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form, bg='#0066cc', fg='#FFFFFF', activebackground='#005299', activeforeground='#FFFFFF')
submit_button.pack()

# Run the GUI
root.mainloop()
