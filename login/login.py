import customtkinter as ctk 

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("green") 

root = ctk.CTk() 
root.geometry("400x400") 
root.title("Login System") 

def login(): 
    new_window = ctk.CTkToplevel(root)
    new_window.title("New Window") 
    new_window.geometry("350x150") 

    label = ctk.CTkLabel(new_window, text = "Welcome to Kritika's coding world!!!")
    label.pack(pady = 20, padx = 20)

label = ctk.CTkLabel(root, text = "Login Page") 
label.pack(pady = 20) 

frame = ctk.CTkFrame(master = root) 
frame.pack(pady = 20, padx = 40, fill = 'both', expand = True) 

label = ctk.CTkLabel(master = frame, text = 'Login System') 
label.pack(pady = 12, padx = 10) 

user_entry = ctk.CTkEntry(master = frame, placeholder_text = "Username") 
user_entry.pack(pady = 12, padx = 10) 

user_pass = ctk.CTkEntry(master = frame, placeholder_text = "Password", show = "*") 
user_pass.pack(pady = 12, padx = 10) 

button = ctk.CTkButton(master = frame, text = 'Login', command = login) 
button.pack(pady = 12, padx = 10) 

checkbox = ctk.CTkCheckBox(master = frame, text = 'Remember Me') 
checkbox.pack(pady = 12, padx = 10) 

root.mainloop()