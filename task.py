import tkinter as tk
from tkinter import messagebox

# Sample in-memory database (lists of dictionaries)
products = [
    {"ProductID": 1, "ProductName": "ProductA", "Price": 100},
    {"ProductID": 2, "ProductName": "ProductB", "Price": 150},
    {"ProductID": 3, "ProductName": "ProductC", "Price": 200}
]

# Initialize the main application window
root = tk.Tk()
root.title("Billing Software")
root.geometry("600x500")

# Customer details
customer_name_label = tk.Label(root, text="Customer Name")
customer_name_label.pack()
customer_name_entry = tk.Entry(root)
customer_name_entry.pack()

customer_contact_label = tk.Label(root, text="Customer Contact")
customer_contact_label.pack()
customer_contact_entry = tk.Entry(root)
customer_contact_entry.pack()

# Product selection
product_label = tk.Label(root, text="Select Product")
product_label.pack()

product_names = [product["ProductName"] for product in products]
product_combobox = tk.StringVar(root)
product_combobox.set(product_names[0])  # Default value
product_menu = tk.OptionMenu(root, product_combobox, *product_names)
product_menu.pack()

quantity_label = tk.Label(root, text="Enter Quantity")
quantity_label.pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

# List to hold the bill items
bill_items = []

# Function to add products to the bill
def add_product():
    product_name = product_combobox.get()
    quantity = int(quantity_entry.get())
    product_info = next(product for product in products if product["ProductName"] == product_name)
    total_price = product_info["Price"] * quantity
    bill_list.insert(tk.END, f"{product_name}\t{quantity}\t{total_price}")
    bill_items.append({"Product": product_name, "Quantity": quantity, "TotalPrice": total_price})
    total_bill.set(total_bill.get() + total_price)

# Button to add products to the bill
add_button = tk.Button(root, text="Add to Bill", command=add_product)
add_button.pack()

# Display the bill and total
bill_list = tk.Listbox(root)
bill_list.pack()

total_bill = tk.IntVar()
total_label = tk.Label(root, text="Total: ")
total_label.pack()
total_value_label = tk.Label(root, textvariable=total_bill)
total_value_label.pack()

# Function to generate the invoice
def generate_invoice():
    customer_name = customer_name_entry.get()
    customer_contact = customer_contact_entry.get()
    invoice_text = f"Customer: {customer_name}\nContact: {customer_contact}\n\n"
    invoice_text += "\n".join([f"{item['Product']}\t{item['Quantity']}\t{item['TotalPrice']}" for item in bill_items])
    invoice_text += f"\n\nTotal: {total_bill.get()}"
    messagebox.showinfo("Invoice", invoice_text)

# Button to generate the invoice
invoice_button = tk.Button(root, text="Generate Invoice", command=generate_invoice)
invoice_button.pack()

# Run the application
root.mainloop()
