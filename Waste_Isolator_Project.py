import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import ttk as tkttk
from tkinter import messagebox
import requests
import os
import csv
import matplotlib.pyplot as plt

waste_categories = {
    "Electronics": {
        "phone": "Recyclable",
        "laptop": "Recyclable",
        "battery": "Non-Recyclable",
        "headphones": "Recyclable",
        "charger": "Recyclable",
        "keyboard": "Recyclable",
        "mouse": "Recyclable",
        "tablet": "Recyclable",
        "monitor": "Recyclable",
        "printer": "Recyclable",
        "router": "Recyclable",
        "television": "Recyclable",
        "camera": "Recyclable",
        "projector": "Recyclable",
        "smartwatch": "Recyclable",
        "game console": "Recyclable",
        "e-reader": "Recyclable",
        "speaker": "Recyclable",
        "GPS device": "Recyclable",
        "power bank": "Recyclable",
    },
    "Food Items": {
        "banana peel": "Compostable",
        "apple core": "Compostable",
        "bread": "Compostable",
        "egg shells": "Compostable",
        "leftover pasta": "Compostable",
        "potato peels": "Compostable",
        "orange peel": "Compostable",
        "vegetable scraps": "Compostable",
        "fruit skins": "Compostable",
        "coffee grounds": "Compostable",
        "tea bags": "Compostable",
        "chicken bones": "Compostable",
        "fish bones": "Compostable",
        "grains": "Compostable",
        "salad leftovers": "Compostable",
        "citrus peels": "Compostable",
        "pits from fruits": "Compostable",
        "cheese rinds": "Compostable",
        "leftover rice": "Compostable",
        "leftover bread": "Compostable",
    },
    "Household": {
        "plastic bottle": "Recyclable",
        "paper": "Recyclable",
        "glass bottle": "Recyclable",
        "tin can": "Recyclable",
        "styrofoam": "Non-Recyclable",
        "plastic bag": "Non-Recyclable",
        "detergent container": "Recyclable",
        "toilet paper roll": "Recyclable",
        "cardboard box": "Recyclable",
        "old furniture": "Recyclable",
        "newspaper": "Recyclable",
        "magazines": "Recyclable",
        "old toys": "Recyclable",
        "old shoes": "Recyclable",
        "light bulbs": "Non-Recyclable",
        "pesticide containers": "Non-Recyclable",
        "cooking oil": "Non-Recyclable",
        "old mattresses": "Recyclable",
        "batteries": "Non-Recyclable",
        "glass jars": "Recyclable",
    },
    "Medical": {
        "syringe": "Non-Recyclable",
        "mask": "Non-Recyclable",
        "bandages": "Non-Recyclable",
        "gloves": "Non-Recyclable",
        "medicine bottle": "Recyclable",
        "pill blister pack": "Recyclable",
        "thermometer": "Non-Recyclable",
        "IV bags": "Non-Recyclable",
        "adhesive tape": "Non-Recyclable",
        "catheters": "Non-Recyclable",
        "empty inhalers": "Non-Recyclable",
        "used gauze": "Non-Recyclable",
        "used needles": "Non-Recyclable",
        "sample containers": "Non-Recyclable",
        "contact lenses": "Non-Recyclable",
        "antiseptic wipes": "Non-Recyclable",
        "prescription bottles": "Recyclable",
        "unused medications": "Non-Recyclable",
        "old medical equipment": "Non-Recyclable",
        "band-aids": "Non-Recyclable",
    },
    "Office": {
        "paper": "Recyclable",
        "pen": "Non-Recyclable",
        "staples": "Non-Recyclable",
        "printer cartridge": "Recyclable",
        "notebook": "Recyclable",
        "folders": "Recyclable",
        "clipboard": "Recyclable",
        "paper clips": "Recyclable",
        "sticky notes": "Non-Recyclable",
        "post-it notes": "Non-Recyclable",
        "envelopes": "Recyclable",
        "wrapping paper": "Recyclable",
        "old calendars": "Recyclable",
        "used white-out": "Non-Recyclable",
        "cables": "Non-Recyclable",
        "old computers": "Recyclable",
        "old monitors": "Recyclable",
        "used notebooks": "Recyclable",
        "used envelopes": "Recyclable",
        "business cards": "Recyclable",
    },
    "Textiles": {
        "old clothes": "Recyclable",
        "shoes": "Recyclable",
        "towels": "Recyclable",
        "bed sheets": "Recyclable",
        "curtains": "Recyclable",
        "hats": "Recyclable",
        "scarves": "Recyclable",
        "socks": "Recyclable",
        "underwear": "Recyclable",
        "handkerchiefs": "Recyclable",
        "backpacks": "Recyclable",
        "old blankets": "Recyclable",
        "tablecloths": "Recyclable",
        "rugs": "Recyclable",
        "fabric scraps": "Recyclable",
        "old belts": "Recyclable",
        "old pillows": "Recyclable",
        "used linens": "Recyclable",
        "fabric softener sheets": "Non-Recyclable",
        "old furniture upholstery": "Recyclable",
    },
    "Garden Waste": {
        "grass clippings": "Compostable",
        "leaves": "Compostable",
        "branches": "Compostable",
        "weeds": "Compostable",
        "flowers": "Compostable",
        "shrub trimmings": "Compostable",
        "fruit and vegetable scraps": "Compostable",
        "plant pots": "Recyclable",
        "wood chips": "Compostable",
        "soil": "Compostable",
        "stems": "Compostable",
        "hedge clippings": "Compostable",
        "corn stalks": "Compostable",
        "pumpkin guts": "Compostable",
        "straw": "Compostable",
        "cuttings from bushes": "Compostable",
        "bark mulch": "Compostable",
        "compost bags": "Compostable",
        "coconut husks": "Compostable",
        "pine needles": "Compostable",
    },
    "Batteries": {
        "AA batteries": "Non-Recyclable",
        "AAA batteries": "Non-Recyclable",
        "9V batteries": "Non-Recyclable",
        "laptop batteries": "Non-Recyclable",
        "car batteries": "Non-Recyclable",
        "phone batteries": "Non-Recyclable",
        "camera batteries": "Non-Recyclable",
        "watch batteries": "Non-Recyclable",
        "hearing aid batteries": "Non-Recyclable",
        "solar batteries": "Non-Recyclable",
        "drone batteries": "Non-Recyclable",
        "power tool batteries": "Non-Recyclable",
        "lithium batteries": "Non-Recyclable",
        "rechargeable batteries": "Non-Recyclable",
        "gel batteries": "Non-Recyclable",
        "alkaline batteries": "Non-Recyclable",
        "lead-acid batteries": "Non-Recyclable",
        "battery packs": "Non-Recyclable",
        "button cell batteries": "Non-Recyclable",
        "electric scooter batteries": "Non-Recyclable",
    },
    "Construction Waste": {
        "bricks": "Recyclable",
        "concrete": "Recyclable",
        "tiles": "Recyclable",
        "wooden beams": "Recyclable",
        "drywall": "Recyclable",
        "metal scraps": "Recyclable",
        "glass panels": "Recyclable",
        "old doors": "Recyclable",
        "old windows": "Recyclable",
        "insulation materials": "Non-Recyclable",
        "paint containers": "Non-Recyclable",
        "roofing materials": "Recyclable",
        "cabinets": "Recyclable",
        "flooring": "Recyclable",
        "plumbing fixtures": "Non-Recyclable",
        "electrical wires": "Recyclable",
        "furniture scraps": "Recyclable",
        "nails": "Recyclable",
        "screws": "Recyclable",
        "lumber": "Recyclable",
    },
    "Hazardous Waste": {
        "paint": "Non-Recyclable",
        "solvents": "Non-Recyclable",
        "pesticides": "Non-Recyclable",
        "chemicals": "Non-Recyclable",
        "oil": "Non-Recyclable",
        "batteries": "Non-Recyclable",
        "cleaning products": "Non-Recyclable",
        "fluorescent bulbs": "Non-Recyclable",
        "medical waste": "Non-Recyclable",
        "asbestos": "Non-Recyclable",
        "old thermometers": "Non-Recyclable",
        "electronic waste": "Non-Recyclable",
        "gasoline containers": "Non-Recyclable",
        "old paint thinner": "Non-Recyclable",
        "pool chemicals": "Non-Recyclable",
        "car wax": "Non-Recyclable",
        "fire extinguishers": "Non-Recyclable",
        "aerosol cans": "Non-Recyclable",
        "lead-based products": "Non-Recyclable",
        "unknown chemicals": "Non-Recyclable",
    },
    "Personal Care": {
        "shampoo bottles": "Recyclable",
        "conditioner bottles": "Recyclable",
        "toothpaste tubes": "Non-Recyclable",
        "makeup containers": "Non-Recyclable",
        "razors": "Non-Recyclable",
        "cotton swabs": "Non-Recyclable",
        "face masks": "Non-Recyclable",
        "deodorant containers": "Non-Recyclable",
        "lotion bottles": "Recyclable",
        "perfume bottles": "Recyclable",
        "hair dye tubes": "Non-Recyclable",
        "nail polish bottles": "Non-Recyclable",
        "hairbrushes": "Non-Recyclable",
        "toilet paper": "Compostable",
        "facial tissues": "Compostable",
        "bath towels": "Recyclable",
        "shower curtains": "Non-Recyclable",
        "wet wipes": "Non-Recyclable",
        "diapers": "Non-Recyclable",
        "sunscreen bottles": "Recyclable",
    },
    "Sports Equipment": {
        "tennis balls": "Non-Recyclable",
        "baseball gloves": "Recyclable",
        "bicycles": "Recyclable",
        "helmets": "Recyclable",
        "exercise mats": "Recyclable",
        "yoga blocks": "Recyclable",
        "weights": "Recyclable",
        "golf clubs": "Recyclable",
        "skateboards": "Recyclable",
        "soccer balls": "Non-Recyclable",
        "footballs": "Non-Recyclable",
        "basketballs": "Non-Recyclable",
        "swimming goggles": "Recyclable",
        "wrestling mats": "Recyclable",
        "boxing gloves": "Recyclable",
        "surfboards": "Recyclable",
        "fishing rods": "Recyclable",
        "hockey sticks": "Recyclable",
        "rollerblades": "Recyclable",
        "kayaks": "Recyclable",
    },
    "Furniture": {
        "sofa": "Recyclable",
        "table": "Recyclable",
        "chair": "Recyclable",
        "bookshelf": "Recyclable",
        "cabinet": "Recyclable",
        "bed frame": "Recyclable",
        "mattress": "Recyclable",
        "desk": "Recyclable",
        "dresser": "Recyclable",
        "nightstand": "Recyclable",
        "armchair": "Recyclable",
        "bench": "Recyclable",
        "entertainment center": "Recyclable",
        "bar stools": "Recyclable",
        "futon": "Recyclable",
        "outdoor furniture": "Recyclable",
        "patio chairs": "Recyclable",
        "bean bag chair": "Recyclable",
        "rocking chair": "Recyclable",
        "glider chair": "Recyclable",
    },
    "Toys": {
        "action figures": "Recyclable",
        "dolls": "Recyclable",
        "puzzles": "Recyclable",
        "board games": "Recyclable",
        "building blocks": "Recyclable",
        "toy cars": "Recyclable",
        "stuffed animals": "Recyclable",
        "toy guns": "Recyclable",
        "video games": "Recyclable",
        "remote-controlled cars": "Recyclable",
        "craft supplies": "Recyclable",
        "educational toys": "Recyclable",
        "musical instruments": "Recyclable",
        "play dough": "Non-Recyclable",
        "marbles": "Non-Recyclable",
        "toy trains": "Recyclable",
        "hobby kits": "Recyclable",
        "toy toolsets": "Recyclable",
        "kites": "Recyclable",
        "remote-controlled drones": "Recyclable",
    },
    "Media": {
        "CDs": "Non-Recyclable",
        "DVDs": "Non-Recyclable",
        "video tapes": "Non-Recyclable",
        "books": "Recyclable",
        "magazines": "Recyclable",
        "newspapers": "Recyclable",
        "comic books": "Recyclable",
        "photographs": "Recyclable",
        "brochures": "Recyclable",
        "posters": "Recyclable",
        "maps": "Recyclable",
        "old notebooks": "Recyclable",
        "stationery": "Recyclable",
        "coloring books": "Recyclable",
        "fliers": "Recyclable",
        "prints": "Recyclable",
        "sheet music": "Recyclable",
        "catalogs": "Recyclable",
        "manuals": "Recyclable",
        "letters": "Recyclable",
    },
    "Plastic Waste": {
        "plastic straws": "Non-Recyclable",
        "plastic cutlery": "Non-Recyclable",
        "plastic wrap": "Non-Recyclable",
        "takeout containers": "Non-Recyclable",
        "plastic food packaging": "Non-Recyclable",
        "plastic cups": "Non-Recyclable",
        "plastic trays": "Non-Recyclable",
        "plastic bottles": "Recyclable",
        "plastic bags": "Non-Recyclable",
        "plastic containers": "Recyclable",
        "plastic lids": "Recyclable",
        "plastic toys": "Non-Recyclable",
        "plastic furniture": "Non-Recyclable",
        "plastic ropes": "Non-Recyclable",
        "plastic nets": "Non-Recyclable",
        "plastic garden pots": "Recyclable",
        "plastic pipelines": "Non-Recyclable",
        "plastic tarps": "Non-Recyclable",
        "plastic sheets": "Non-Recyclable",
        "plastic mesh": "Non-Recyclable",
    },
    "Wood Waste": {
        "wooden pallets": "Recyclable",
        "wood scraps": "Recyclable",
        "wood shavings": "Compostable",
        "old furniture": "Recyclable",
        "wooden crates": "Recyclable",
        "tree branches": "Compostable",
        "wood chips": "Compostable",
        "wood planks": "Recyclable",
        "wooden toys": "Recyclable",
        "wooden dowels": "Recyclable",
        "old fences": "Recyclable",
        "wooden frames": "Recyclable",
        "wooden shingles": "Recyclable",
        "old cabinets": "Recyclable",
        "wooden boxes": "Recyclable",
        "wooden posts": "Recyclable",
        "wooden benches": "Recyclable",
        "wooden stakes": "Recyclable",
        "wooden decking": "Recyclable",
        "old flooring": "Recyclable",
    }
}

for category, items in waste_categories.items():
    print(f"Category: {category}")
    for item, classification in items.items():
        print(f"  {item}: {classification}")

# Data file
data_file = 'waste_data.csv'

# Create the file if it doesn't exist
if not os.path.exists(data_file):
    with open(data_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Waste Type", "Category", "Parent Category"])

# Function to add waste to the data file
def add_waste_to_file(waste, category, parent_category):
    with open(data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([waste, category, parent_category])

# Function to show waste statistics as a pie chart
def show_stats():
    counts = {"Recyclable": 0, "Compostable": 0, "Non-Recyclable": 0}
    try:
        with open(data_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Category"] in counts:
                    counts[row["Category"]] += 1
    except Exception as e:
        messagebox.showerror("Error", f"Error reading data: {e}")
        return

    labels = list(counts.keys())
    sizes = list(counts.values())

    plt.figure(figsize=(7, 7))
    plt.pie(
        sizes, labels=labels, autopct='%1.1f%%', startangle=140,
        colors=["#66c2a5", "#fc8d62", "#8da0cb"]
    )
    plt.title("Waste Categories Distribution", fontsize=14)
    plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
    plt.show()

# Function to clear all data
def clear_data():
    os.remove(data_file)
    with open(data_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Waste Type", "Category", "Parent Category"])
    messagebox.showinfo("Data Cleared", "All waste data has been cleared!")
    update_table()

# Function to update the table with categorized waste data
def update_table():
    for row in table.get_children():
        table.delete(row)
    try:
        with open(data_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.insert(
                    "", "end", values=(
                        row.get("Waste Type", "Unknown"),
                        row.get("Category", "Unknown"),
                        row.get("Parent Category", "Unknown")
                    )
                )
    except Exception as e:
        print(f"Error updating table: {e}")

# Function to update sub-items based on category
# Function to update sub-items based on category
def update_subitems(*args):
    selected_category = category_var.get()
    
    # Clear current sub-items in the dropdown
    subitem_menu['values'] = []
    
    if selected_category in waste_categories:
        # Update sub-items with the category's subcategories
        subcategories = list(waste_categories[selected_category].keys())
        subitem_menu['values'] = subcategories
        if subcategories:
            subitem_var.set(subcategories[0])  # Set the first subcategory as default
    else:
        subitem_menu['values'] = ["No items available"]
        subitem_var.set("No items available")


# Main function to classify waste
def classify_waste():
    waste = subitem_var.get().lower()
    category = "Unknown"
    parent_category = None

    selected_category = category_var.get()
    if selected_category in waste_categories and waste in waste_categories[selected_category]:
        category = waste_categories[selected_category][waste]
        parent_category = selected_category

    if category == "Unknown":
        messagebox.showerror("Error", f"'{waste}' is not recognized. Try another item from the suggestions.")
    else:
        result_label.config(text=f"'{waste}' is classified as: {category}")
        add_waste_to_file(waste, category, parent_category)
        update_table()

def fetch_global_waste_stats():
    try:
        # Replace this with your API call
        data = {
            "Recyclable": 12000,
            "Compostable": 8000,
            "Non-Recyclable": 5000,
        }

        # Extract keys (categories) and values (amounts)
        categories = list(data.keys())
        values = list(data.values())

        # Create a figure with two subplots: one for the bar chart and one for the pie chart
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))  # Two side-by-side plots

        # Bar Chart
        axes[0].bar(categories, values, color=['#66c2a5', '#fc8d62', '#8da0cb'])
        axes[0].set_title("Global Waste Statistics (Bar Chart)", fontsize=14)
        axes[0].set_xlabel("Waste Type", fontsize=12)
        axes[0].set_ylabel("Amount (tons)", fontsize=12)
        axes[0].tick_params(axis='x', labelsize=10)
        axes[0].tick_params(axis='y', labelsize=10)

        # Pie Chart
        axes[1].pie(values, labels=categories, autopct='%1.1f%%', startangle=140,
                    colors=["#66c2a5", "#fc8d62", "#8da0cb"])
        axes[1].set_title("Global Waste Statistics (Pie Chart)", fontsize=14)

        # Adjust layout and show the plots
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch statistics: {e}")

# Function to show recycling tips
def show_recycling_tips():
    # Create a new window for the tips
    tips_window = tk.Toplevel(app)
    tips_window.title("Common Recycling Practices")
    tips_window.geometry("400x400")
    tips_window.configure(bg="#f0f8ff")

    # Add a header
    tk.Label(
        tips_window, 
        text="Common Ways to Recycle Waste", 
        font=("Arial", 16, "bold"), 
        bg="#f0f8ff", 
        fg="#4682b4"
    ).pack(pady=10)

    # Add a list of recycling tips
    tips = [
        "1. Sort waste into categories: paper, plastic, metal, glass, etc.",
        "2. Rinse food containers before recycling to avoid contamination.",
        "3. Flatten cardboard boxes to save space.",
        "4. Avoid mixing non-recyclable items with recyclables.",
        "5. Check local recycling guidelines for accepted materials.",
        "6. Reuse items like jars, bags, and containers whenever possible.",
        "7. Donate or recycle old electronics at e-waste collection centers.",
        "8. Compost organic waste like food scraps and yard waste."
    ]

    # Display each tip in the window
    for tip in tips:
        tk.Label(
            tips_window, 
            text=tip, 
            font=("Arial", 12), 
            bg="#f0f8ff", 
            fg="#333", 
            wraplength=350, 
            justify="left"
        ).pack(anchor="w", padx=10, pady=5)

    # Add a close button
    tk.Button(
        tips_window, 
        text="Close", 
        command=tips_window.destroy, 
        font=("Arial", 12, "bold"), 
        bg="#fc8d62", 
        fg="white"
    ).pack(pady=20)

# Initialize the app
app = ttk.Window(themename="flatly")
app.title("Waste Segregation Helper")
app.geometry("800x600")

# Header
header_label = ttk.Label(app, text="Waste Segregation Helper", font=("Helvetica", 24, "bold"), bootstyle=PRIMARY)
header_label.pack(pady=20)

# Dropdown Frame
dropdown_frame = ttk.Frame(app, padding=10)
dropdown_frame.pack(fill=X)

category_var = ttk.StringVar()
ttk.Label(dropdown_frame, text="Select a Category:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
category_menu = ttk.Combobox(dropdown_frame, textvariable=category_var, values=list(waste_categories.keys()))
category_menu.grid(row=0, column=1, padx=5, pady=5)
category_menu.current(0)
category_menu.bind('<<ComboboxSelected>>', update_subitems)  

subitem_var = ttk.StringVar()
ttk.Label(dropdown_frame, text="Select an Item:", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5)
subitem_menu = ttk.Combobox(dropdown_frame, textvariable=subitem_var)
subitem_menu.grid(row=1, column=1, padx=5, pady=5)


# Buttons
button_frame = ttk.Frame(app, padding=10)
button_frame.pack(fill=X)

ttk.Button(button_frame, text="Global Waste Stats", command=fetch_global_waste_stats, bootstyle=WARNING).grid(row=0, column=4, padx=10)

ttk.Button(button_frame, text="Classify Waste", command=classify_waste, bootstyle=SUCCESS).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Show Statistics", command=show_stats, bootstyle=INFO).grid(row=0, column=1, padx=10)
ttk.Button(button_frame, text="Recycling Tips", command=show_recycling_tips, bootstyle=SECONDARY).grid(row=0, column=2, padx=10)
ttk.Button(button_frame, text="Clear Data", command=clear_data, bootstyle=DANGER).grid(row=0, column=3, padx=10)

# Result
result_label = ttk.Label(app, text="", font=("Helvetica", 12, "bold"), bootstyle=PRIMARY)
result_label.pack(pady=10)

# Table
columns = ("Waste Type", "Category", "Parent Category")
table = ttk.Treeview(app, columns=columns, show="headings", height=10)
table.heading("Waste Type", text="Waste Type")
table.heading("Category", text="Category")
table.heading("Parent Category", text="Parent Category")
table.pack(pady=20, padx=10, fill=X)

# Footer
footer_label = ttk.Label(app, text="Help segregate waste properly!", font=("Helvetica", 10), bootstyle="light")
footer_label.pack(pady=10)

# Initialize table with existing data
update_table()

app.mainloop()
