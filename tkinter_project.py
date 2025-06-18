from tkinter import *
import mysql.connector
from PIL import Image, ImageTk  # Import PIL for image handling
from tkinter import messagebox  # For pop-up messages

# Main Tkinter Window
root = Tk()
root.title("Event Registration Portal")
root.geometry("800x700")

root.configure(bg="lightblue")


root.option_add("*Label.Background", "lightblue")
root.option_add("*Button.Background", "lightblue")

# Function to clear the window for navigation
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Function to display the Home Page
def home_page():
    clear_window()

    Label(root, text="Welcome to the Event Registration Portal!", font=("Arial", 28), bg="lightblue", fg="blue").pack(pady=30)

    # Load Image
    img = Image.open(r"C:\GRACE_PROGRAM FILES\PYTHON CLS\pexels-nemuel-6424590.jpg")  # Replace with your image file path
    img = img.resize((800, 500))  # Resize image (optional)
    img_tk = ImageTk.PhotoImage(img)  # Convert to Tkinter-compatible format

    # Display Image
    Label(root, image=img_tk).pack(pady=15)
    
    # Keep a reference to avoid garbage collection issues
    root.img = img_tk  

    # Buttons
    Button(root, text="About", command=about_page, bg="lightgreen", font=("Arial", 14), width=12).pack(pady=15)
    Button(root, text="Register", command=login_register_page, bg="lightblue", font=("Arial", 14), width=15).pack(pady=15)

# Function to display the About Page
def about_page():
    clear_window()
    
    Label(root, text="About the Python Full Stack Webinar", font=("Arial", 26), fg="red").pack(pady=20)
    
    Label(root, text="Master Python Full Stack Development and build real-world web applications!", font=("Arial", 16)).pack(pady=20)
    
     # Load Image
    img = Image.open(r"C:\GRACE_PROGRAM FILES\PYTHON CLS\pexels-realtoughcandy-11035474.jpg ")  # Replace with your image file path
    img = img.resize((300, 200))  # Resize image (optional)
    img_tk = ImageTk.PhotoImage(img)  # Convert to Tkinter-compatible format

    # Display Image
    Label(root, image=img_tk).pack(pady=15)
    
    # Keep a reference to avoid garbage collection issues
    root.img = img_tk  

    Label(root, text=' 🚀 This webinar is designed for beginners and aspiring developers who want to learn frontend, backend, and database management using Python-based technologies', font=("arial", 13)).pack(pady=25)
    
    Label(root, text="🔹 Frontend: HTML, CSS, JavaScript, React.js", font=("Arial", 12)).pack()
    Label(root, text="🔹 Backend: Python, Flask/Django", font=("Arial", 12)).pack()
    Label(root, text="🔹 Database: MySQL, MongoDB", font=("Arial", 12)).pack()
    Label(root, text="🔹 APIs & Deployment: REST APIs, Hosting", font=("Arial", 12)).pack()
    
    Label(root, text="📅 Date: 26-03-2025  ⏰ Time: 10.00 a.m - 12.00 p.m", font=("Arial", 12), fg="green").pack(pady=20)
    Label(root, text="📍 Online Event - 🖥️Register Now and take your first step towards becoming a Python Full Stack Developer!", font=("Arial", 14), fg="blue").pack(pady=20)
    
    Button(root, text="Back to Home", command=home_page, bg="black",fg='white', font=("Arial", 12), width=18, height=2).pack(padx=20,pady=15)



# Function to display the Login/Register Page


def login_register_page():
    clear_window()  # Clears the window before adding new elements

    Label(root, text="Register Form :", font=("Arial", 20), fg="blue").pack(pady=(20,10))
 
    form_frame = Frame(root, width=400, height=300)
    form_frame.place(relx=0.5, rely=0.35, anchor="center")  # Moves form up


    Label(form_frame, text="Name", height=2, width=12, font=("arial",12)).grid(row=0, padx=20, pady=10, sticky="e")
    Label(form_frame, text="Phone_num", height=2, width=12, font=("Arial", 12)).grid(row=1, padx=20, pady=10, sticky="e")
    Label(form_frame, text="Email", height=2, width=12,font=("arial",12)).grid(row=2, padx=20, pady=10, sticky="e")
    Label(form_frame, text="Password", height=2, width=12,font=("arial",12)).grid(row=3, padx=20, pady=10, sticky="e")

    e1 = Entry(form_frame, width=40, font=("arial",14))
    e2 = Entry(form_frame, width=40,font=("Arial", 14))
    e3 = Entry(form_frame, width=40,font=("Arial", 14))
    e4 = Entry(form_frame, width=40, show="*",font=("Arial", 14))  # Hide password input

    e1.grid(row=0, column=1, padx=15, pady=15)
    e2.grid(row=1, column=1, padx=15, pady=15)
    e3.grid(row=2, column=1, padx=15, pady=15)
    e4.grid(row=3, column=1, padx=15, pady=15)

    def register_user():
        name = e1.get().strip()
        phone_num = e2.get().strip()
        email = e3.get().strip()
        password = e4.get().strip()

        if not name or not phone_num or not email or not password:
            messagebox.showerror("Error","All fields are required!")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",        # Replace with your MySQL server host
                user="root",             # Replace with your MySQL username
                password="12345@7",# Replace with your MySQL password
                database="sample123"  # The database you created
            )
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),phone_num VARCHAR(15), email VARCHAR(255) UNIQUE, password VARCHAR(255))")
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                messagebox.showerror("Error","Email already registered!")
                conn.close()
                return

            cursor.execute("INSERT INTO users (name, phone_num, email, password) VALUES (%s, %s, %s, %s)", (name, phone_num, email, password))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Registration successful!")
            thank_you_page()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    Button(form_frame, text="Register", command=register_user,
           bg="purple", fg="white", height=2, width=12, font=("Arial", 13)).grid(row=4, column=1, pady=20)


    Button(root, text="Back to Home", command=home_page, bg="black",fg='white', font=("Arial", 12), width=18,height=2 ).place(relx=0.5, rely=0.65, anchor="center")

# Function to display the Thank You Page
def thank_you_page():
    clear_window()
    Label(root, text="Thank You  for Registering!", font=("Arial", 22, "bold"), fg="blue").pack(pady=20)
    Label(root, text="You have successfully registered for the Python Full Stack Webinar.", font=("Arial", 14)).pack(pady=10)
    
    Label(root, text="📍 Online Event - Check your email for the webinar link!", font=("Arial", 12)).pack(pady=5)
    
    Label(root, text="💡 'Learning never exhausts the mind.' - Leonardo da Vinci", font=("Arial", 12, "italic"), fg="gray").pack(pady=15)
    
    Button(root, text="Back to Home", command=home_page, bg="black",fg="white" ,font=("Arial", 12), width=18,height=2).pack(pady=10)

home_page()

root.mainloop()
