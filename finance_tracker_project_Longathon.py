# Project Name: "Personal Finance Tracker with Visualization" 

"""
Problem Statement:
Many people struggle with tracking their daily expenses, budgeting, and understanding their spending patterns. 
This project will provide a simple, Python-based solution to help users track their finances and visualize their spending habits using basic Python libraries.

"""

"""
Solution:
Create a command-line Personal Finance Tracker where users can :
input daily expenses, categorize them, and get insights like total spending, savings, and category-wise breakdowns.
It will also include basic data visualization (e.g., pie charts) to help users see where most of their money is going.

"""

"""
Key Features:

1)  Expense Tracking: Users can input their daily expenses, including categories (e.g., food, travel, utilities).

2)  Budget Monitoring: Allow users to set a monthly budget and check if they are overspending.

3)  Summary Reports: The program generates daily, weekly, or monthly expense reports.

4)  Data Visualization: Use Python’s matplotlib or seaborn to create simple bar charts and pie charts to visualize spending patterns.

5)  File Storage: Save and load user data in a text file or CSV so that users can track their expenses over time.

"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

# Global variables
expenses = []
budget = 0
budget_period = "Daily"  # Default period
data_file = 'expenses.csv'  # CSV file for saving expenses

# Load expenses from CSV
def load_expenses():
    global expenses
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expenses.append({
                        "date": datetime.strptime(row["Date"], "%Y-%m-%d"),
                        "category": row["Category"],
                        "amount": float(row["Amount"])
                    })
                except ValueError:
                    print(f"Skipping invalid entry: {row}")  # Log the invalid entry
    view_expenses()

# Save expenses to CSV
def save_expenses():
    with open(data_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])
        for expense in expenses:
            writer.writerow([expense["date"].strftime("%Y-%m-%d"), expense["category"], expense["amount"]])
    messagebox.showinfo("Saved", "Expenses saved to expenses.csv")

# Wipe all data
def wipe_all_data():
    global expenses
    expenses.clear()
    if os.path.exists(data_file):
        os.remove(data_file)
    messagebox.showinfo("Wiped", "All data has been wiped.")

# Add an expense
def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    if not date or not category or not amount:
        messagebox.showerror("Error", "All fields are required")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount")
        return

    expenses.append({
        "date": datetime.strptime(date, "%Y-%m-%d"),
        "category": category,
        "amount": amount
    })
    
    messagebox.showinfo("Success", f"Expense of {amount} added to {category} on {date}.")
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    view_expenses()

# View expenses based on selected period (daily, weekly, monthly)
def view_expenses():
    period = period_var.get()
    filter_expenses(period)

# Filter expenses by period
def filter_expenses(period):
    today = datetime.today()
    filtered_expenses = []

    if period == "Daily":
        filtered_expenses = [expense for expense in expenses if expense['date'].date() == today.date()]
    elif period == "Weekly":
        start_of_week = today - timedelta(days=today.weekday())
        filtered_expenses = [expense for expense in expenses if start_of_week <= expense['date'] <= today]
    elif period == "Monthly":
        filtered_expenses = [expense for expense in expenses if expense['date'].month == today.month and expense['date'].year == today.year]

    for row in tree.get_children():
        tree.delete(row)

    for expense in filtered_expenses:
        tree.insert('', tk.END, values=(expense['date'].strftime("%Y-%m-%d"), expense['category'], expense['amount']))

# Set a budget
def set_budget():
    global budget, budget_period
    try:
        budget = float(budget_entry.get())
        budget_period = budget_period_var.get()
        messagebox.showinfo("Success", f"{budget_period} budget of {budget} set successfully.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid budget amount")

# Check budget status based on selected period
def check_budget():
    total = calculate_total_expenses()
    if total > budget:
        messagebox.showwarning("Budget Exceeded", f"You've exceeded your {budget_period.lower()} budget by {total - budget}!")
    else:
        messagebox.showinfo("Within Budget", f"You have {budget - total} remaining for this {budget_period.lower()}.")

# Calculate total expenses based on the selected period
def calculate_total_expenses():
    period = period_var.get()
    today = datetime.today()
    total = 0

    if period == "Daily":
        total = sum(expense['amount'] for expense in expenses if expense['date'].date() == today.date())
    elif period == "Weekly":
        start_of_week = today - timedelta(days=today.weekday())
        total = sum(expense['amount'] for expense in expenses if start_of_week <= expense['date'] <= today)
    elif period == "Monthly":
        total = sum(expense['amount'] for expense in expenses if expense['date'].month == today.month and expense['date'].year == today.year)

    return total

# Generate a summary report
def summary_report():
    total = calculate_total_expenses()
    report_text = f"Total Expenses: {total}\n"

    categories = {}
    for expense in expenses:
        category = expense['category']
        if category not in categories:
            categories[category] = 0
        categories[category] += expense['amount']

    report_text += "\n--- Category Breakdown ---\n"
    for category, amount in categories.items():
        report_text += f"{category}: {amount}\n"

    messagebox.showinfo("Summary Report", report_text)

# Visualize expenses using matplotlib based on the selected period
def plot_expenses():
    period = period_var.get()
    today = datetime.today()
    filtered_expenses = []

    if period == "Daily":
        filtered_expenses = [expense for expense in expenses if expense['date'].date() == today.date()]
    elif period == "Weekly":
        start_of_week = today - timedelta(days=today.weekday())
        filtered_expenses = [expense for expense in expenses if start_of_week <= expense['date'] <= today]
    elif period == "Monthly":
        filtered_expenses = [expense for expense in expenses if expense['date'].month == today.month and expense['date'].year == today.year]

    categories = {}
    for expense in filtered_expenses:
        category = expense['category']
        if category not in categories:
            categories[category] = 0
        categories[category] += expense['amount']

    if not categories:
        messagebox.showinfo("No Data", "No expenses found for the selected period.")
        return

    labels = categories.keys()
    sizes = categories.values()

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title(f'Expenses by Category ({period})')
    plt.show()

# Main GUI
root = tk.Tk()
root.title("Personal Finance Tracker")

# Set window size and background color
root.geometry('600x600')
root.configure(bg='#f0f0f0')

# Create frames for better organization
frame_top = tk.Frame(root, bg='#e0e0e0', pady=10)
frame_top.pack(fill='x')

frame_bottom = tk.Frame(root, bg='#f0f0f0', pady=20)
frame_bottom.pack(fill='x')

# Title label with styling
title_label = tk.Label(frame_top, text="Personal Finance Tracker", font=('Helvetica', 18, 'bold'), bg='#e0e0e0', fg='#333')
title_label.pack()

# Input section for adding expenses
input_frame = tk.Frame(root, bg='#f0f0f0', pady=10)
input_frame.pack(padx=10, pady=10)

tk.Label(input_frame, text="Date (YYYY-MM-DD):", font=('Helvetica', 12), bg='#f0f0f0').grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
date_entry = tk.Entry(input_frame, font=('Helvetica', 12), width=20)
date_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Category:", font=('Helvetica', 12), bg='#f0f0f0').grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
category_entry = tk.Entry(input_frame, font=('Helvetica', 12), width=20)
category_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Amount:", font=('Helvetica', 12), bg='#f0f0f0').grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
amount_entry = tk.Entry(input_frame, font=('Helvetica', 12), width=20)
amount_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(input_frame, text="Add Expense", font=('Helvetica', 12), bg='#4caf50', fg='white', command=add_expense).grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)

# Budget Input Section
tk.Label(input_frame, text="Set Budget:", font=('Helvetica', 12), bg='#f0f0f0').grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
budget_entry = tk.Entry(input_frame, font=('Helvetica', 12), width=20)
budget_entry.grid(row=4, column=1, padx=10, pady=5)

# Budget Period Selection
tk.Label(input_frame, text="Budget Period:", font=('Helvetica', 12), bg='#f0f0f0').grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
budget_period_var = tk.StringVar(value="Daily")
tk.Radiobutton(input_frame, text="Daily", variable=budget_period_var, value="Daily", bg='#f0f0f0').grid(row=5, column=1, sticky=tk.W)
tk.Radiobutton(input_frame, text="Weekly", variable=budget_period_var, value="Weekly", bg='#f0f0f0').grid(row=5, column=1, sticky=tk.E)

tk.Button(input_frame, text="Set Budget", font=('Helvetica', 12), bg='#4caf50', fg='white', command=set_budget).grid(row=6, column=1, padx=10, pady=10, sticky=tk.E)

# Period Selection for Viewing Expenses
tk.Label(input_frame, text="View Expenses:", font=('Helvetica', 12), bg='#f0f0f0').grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
period_var = tk.StringVar(value="Daily")
tk.Radiobutton(input_frame, text="Daily", variable=period_var, value="Daily", bg='#f0f0f0').grid(row=7, column=1, sticky=tk.W)
tk.Radiobutton(input_frame, text="Weekly", variable=period_var, value="Weekly", bg='#f0f0f0').grid(row=7, column=1, sticky=tk.E)
tk.Radiobutton(input_frame, text="Monthly", variable=period_var, value="Monthly", bg='#f0f0f0').grid(row=7, column=1, sticky=tk.E)

tk.Button(input_frame, text="View Expenses", font=('Helvetica', 12), bg='#4caf50', fg='white', command=view_expenses).grid(row=8, column=1, padx=10, pady=10, sticky=tk.E)
tk.Button(input_frame, text="Check Budget", font=('Helvetica', 12), bg='#4caf50', fg='white', command=check_budget).grid(row=9, column=1, padx=10, pady=10, sticky=tk.E)

# Create Treeview for displaying expenses
tree = ttk.Treeview(root, columns=("Date", "Category", "Amount"), show='headings', height=10)
tree.heading("Date", text="Date")
tree.heading("Category", text="Category")
tree.heading("Amount", text="Amount")
tree.pack(padx=10, pady=10)

# Create buttons for summary and plotting
tk.Button(frame_bottom, text="Summary Report", font=('Helvetica', 12), bg='#2196f3', fg='white', command=summary_report).pack(side=tk.LEFT, padx=10)
tk.Button(frame_bottom, text="Plot Expenses", font=('Helvetica', 12), bg='#2196f3', fg='white', command=plot_expenses).pack(side=tk.LEFT, padx=10)

# Create buttons for saving, loading expenses, and wiping data
tk.Button(frame_bottom, text="Save Expenses", font=('Helvetica', 12), bg='#f44336', fg='white', command=save_expenses).pack(side=tk.LEFT, padx=10)
tk.Button(frame_bottom, text="Load Expenses", font=('Helvetica', 12), bg='#f44336', fg='white', command=load_expenses).pack(side=tk.LEFT, padx=10)
tk.Button(frame_bottom, text="Wipe All Data", font=('Helvetica', 12), bg='#f44336', fg='white', command=wipe_all_data).pack(side=tk.LEFT, padx=10)

# Load existing expenses when the program starts
load_expenses()

# Run the main loop
root.mainloop()
