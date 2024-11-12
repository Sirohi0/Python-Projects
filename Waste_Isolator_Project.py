        #Project Idea: Waste Segregation Helper

""" 
Aim:
Create a Waste Segregation Helper that helps users correctly classify and dispose of their household waste into categories 
like recyclables, compostable, and non-recyclables. 
The app will suggest which type of waste belongs to which category, improving environmental sustainability.

"""

import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
import matplotlib.pyplot as plt

# Predefined waste categories with parent categories and items
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

# Example of how to access the categories and items
for category, items in waste_categories.items():
    print(f"Category: {category}")
    for item, classification in items.items():
        print(f"  {item}: {classification}")

# Data persistence file
data_file = 'waste_data.csv'

# Create the file if it doesn't exist
if not os.path.exists(data_file):
    with open(data_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Waste Type", "Category", "Parent Category"])

# Function to add waste to data file
def add_waste_to_file(waste, category, parent_category):
    with open(data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([waste, category, parent_category])

# Function to display a pie chart of waste categories
def show_stats():
    counts = {"Recyclable": 0, "Compostable": 0, "Non-Recyclable": 0}
    with open(data_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            counts[row["Category"]] += 1

    labels = list(counts.keys())
    sizes = list(counts.values())

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=["#66c2a5", "#fc8d62", "#8da0cb"])
    plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
    plt.show()

# Function to clear all saved data
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

    with open(data_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.insert("", "end", values=(row["Waste Type"], row["Category"], row["Parent Category"]))

# Function to update the sub-items dropdown based on the selected category
def update_subitems(*args):
    selected_category = category_var.get()
    if selected_category in waste_categories:
        subitem_menu.config(values=list(waste_categories[selected_category].keys()))
    subitem_menu.current(0)  # Set to the first value

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

# Initialize the Tkinter app
app = tk.Tk()
app.title("Waste Segregation Helper")
app.geometry("800x600")
app.configure(bg="#f0f8ff")  # Light blue background

# Styling for the interface
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"))
style.configure("TLabel", font=("Arial", 12))

# Header label
header_label = tk.Label(app, text="Waste Segregation Helper", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#4682b4")
header_label.pack(pady=20)

# UI components
tk.Label(app, text="Select a Category:", font=("Arial", 12), bg="#f0f8ff", fg="#333").pack(pady=10)

# Category Dropdown
category_var = tk.StringVar()
category_menu = ttk.Combobox(app, textvariable=category_var, values=list(waste_categories.keys()), font=("Arial", 12))
category_menu.pack(pady=5)
category_menu.current(0)

# Sub-item Dropdown
subitem_var = tk.StringVar()
subitem_menu = ttk.Combobox(app, textvariable=subitem_var, font=("Arial", 12))
subitem_menu.pack(pady=5)

# Bind the category menu to update sub-items on selection
category_menu.bind("<<ComboboxSelected>>", update_subitems)
update_subitems()  # Initialize sub-items for the first category

# Classify waste button
classify_btn = tk.Button(app, text="Classify Waste", command=classify_waste, font=("Arial", 12, "bold"), 
                         bg="#4682b4", fg="black", width=20)
classify_btn.pack(pady=10)

# Result display label
result_label = tk.Label(app, text="", font=("Arial", 12, "bold"), bg="#f0f8ff", fg="#4682b4")
result_label.pack(pady=10)

# Stats button
stats_btn = tk.Button(app, text="Show Waste Statistics", command=show_stats, font=("Arial", 12, "bold"), 
                      bg="#66c2a5", fg="black", width=20)
stats_btn.pack(pady=5)

# Clear data button
clear_btn = tk.Button(app, text="Clear All Waste Data", command=clear_data, font=("Arial", 12, "bold"), 
                      bg="#fc8d62", fg="black", width=20)
clear_btn.pack(pady=5)

# Table to display categorized waste data
columns = ("Waste Type", "Category", "Parent Category")
table = ttk.Treeview(app, columns=columns, show="headings", height=10)
table.heading("Waste Type", text="Waste Type")
table.heading("Category", text="Category")
table.heading("Parent Category", text="Parent Category")
table.pack(pady=20)

# Update the table with existing data on startup
update_table()

# Footer label
footer_label = tk.Label(app, text="Help segregate waste properly!", font=("Arial", 10), bg="#f0f8ff", fg="#333")
footer_label.pack(pady=20)

# Run the app
app.mainloop()
