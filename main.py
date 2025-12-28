import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

# -------------------- DATABASE CONNECTION --------------------
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="car_showroom"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"{err}")
        return None

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Porsche Car Showroom Billing System")
root.geometry("900x700")

heading = tk.Label(
    root,
    text="Welcome to Porsche Car Showroom",
    font=("Arial", 16, "bold")
)
heading.pack(pady=10)

selected_car_details = None
bill_label = None

# -------------------- FETCH CAR DATA --------------------
def fetch_car_data():
    conn = connect_db()
    if not conn:
        return []

    cursor = conn.cursor()
    cursor.execute("SELECT model_name, image_path FROM cars")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data

# -------------------- DISPLAY SELECTED CAR DETAILS --------------------
def display_car_details(car_details):
    global bill_label
    model_name, price, engine_hp, top_speed, year, image_path = car_details

    bill_text = f"""
Porsche Car Showroom
-------------------------
Model: {model_name}
Price: ₹{price}
Engine: {engine_hp} HP
Top Speed: {top_speed} km/h
Year: {year}

Total Price: ₹{price}
"""

    bill_label.config(text=bill_text)

# -------------------- SELECT CAR --------------------
def select_car(model_name):
    global selected_car_details

    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor()
    cursor.execute(
        "SELECT model_name, price, engine_hp, top_speed, year_released, image_path FROM cars WHERE model_name=%s",
        (model_name,)
    )
    car_details = cursor.fetchone()

    cursor.close()
    conn.close()

    if car_details:
        selected_car_details = car_details
        display_car_details(car_details)
    else:
        messagebox.showerror("Error", "Car details not found")

# -------------------- DISPLAY CARS WITH IMAGES --------------------
def display_car_images():
    car_data = fetch_car_data()

    if not car_data:
        messagebox.showerror("Error", "No car data found in database")
        return

    car_frame = tk.Frame(root)
    car_frame.pack(pady=20)

    for index, (model_name, image_path) in enumerate(car_data):
        try:
            img = Image.open(image_path)
            img = img.resize((150, 150))
            img = ImageTk.PhotoImage(img)
        except:
            continue

        btn = tk.Button(
            car_frame,
            image=img,
            text=model_name,
            compound="top",
            command=lambda name=model_name: select_car(name)
        )
        btn.image = img
        btn.grid(row=0, column=index, padx=10)

# -------------------- CUSTOMER SECTION --------------------
def show_customer_section():
    tk.Label(root, text="Enter Customer Information", font=("Helvetica", 12)).pack(pady=10)

    global customer_name_entry, customer_contact_entry
    global customer_city_entry, customer_email_entry

    tk.Label(root, text="Enter Your Name").pack()
    customer_name_entry = tk.Entry(root, width=30)
    customer_name_entry.pack(pady=5)

    tk.Label(root, text="Enter Contact No").pack()
    customer_contact_entry = tk.Entry(root, width=30)
    customer_contact_entry.pack(pady=5)

    tk.Label(root, text="Enter City Name").pack()
    customer_city_entry = tk.Entry(root, width=30)
    customer_city_entry.pack(pady=5)

    tk.Label(root, text="Enter Email ID").pack()
    customer_email_entry = tk.Entry(root, width=30)
    customer_email_entry.pack(pady=5)

# -------------------- GENERATE BILL --------------------
def generate_bill():
    if not selected_car_details:
        messagebox.showerror("Selection Error", "Please select a car model")
        return

    name = customer_name_entry.get()
    contact = customer_contact_entry.get()

    if not name or not contact:
        messagebox.showerror("Input Error", "Please fill all fields")
        return

    messagebox.showinfo("Success", "Bill Generated Successfully")

# -------------------- BILL DISPLAY --------------------
bill_label = tk.Label(
    root,
    text="Your Bill Will Appear Here",
    font=("Helvetica", 10),
    justify="left"
)
bill_label.pack(pady=20)

generate_btn = tk.Button(
    root,
    text="Generate Bill",
    command=generate_bill,
    width=20,
    height=2,
    bg="white"
)
generate_btn.pack(pady=10)

# -------------------- START APP --------------------
show_customer_section()
display_car_images()

root.mainloop()
