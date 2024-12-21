import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk  
import subprocess

def on_go_button_click(event=None):
    user_name = name_entry.get()
    root.withdraw()
    subprocess.Popen(['python', 'test-2-after.py', user_name])
root = tk.Tk()
root.title("Eyes Tracking App")
root.geometry("1000x500")

background_image = Image.open("background.png")  
background_image = background_image.resize((1000, 500), Image.Resampling.LANCZOS)  
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  

title_font = font.Font(family="Helvetica", size=20, weight="bold")
text_font = font.Font(family="Helvetica", size=10)
entry_font = font.Font(family="Helvetica", size=12)

title_label = tk.Label(root, text="Eyes Tracking App", bg='#1E2440', fg='#D4B0FF', font=title_font)
title_label.pack(pady=10)

description_text = ("An eyes tracking application utilizes advanced\n"
                    "technology to record and analyze eye movements of\n"
                    "users. It can enhance user experience across various\n"
                    "fields such as market research, education, and\n"
                    "healthcare.\n\n"
                    "In education, it offers educators tools to assess student\n"
                    "engagement and optimize learning materials. In\n"
                    "healthcare, it can assist in diagnosing and treating\n"
                    "visual and cognitive disorders by analyzing how\n"
                    "patients interact with their environment.\n\n"
                    "Overall, this technology not only improves usability and\n"
                    "effectiveness but also opens new avenues for research\n"
                    "and innovation in numerous domains.")
description_label = tk.Label(root, text=description_text, bg='#1E2440', fg='white', justify="left", font=text_font)
description_label.pack(pady=10)

form_frame = tk.Frame(root, bg='#1E2440')
form_frame.pack(pady=10)

name_label = tk.Label(form_frame, text="NAME", bg='#1E2440', fg='white', font=text_font)
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(form_frame, font=entry_font)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(form_frame, text="PHONE", bg='#1E2440', fg='white', font=text_font)
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
phone_entry = tk.Entry(form_frame, font=entry_font)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

# def on_go_button_click():
#     user_name = name_entry.get()
#     open_camera_interface(user_name)
    
go_button = tk.Button(root, text="GO", font=entry_font, bg="#3D5279", fg="white", width=10, command=on_go_button_click)
go_button.pack(pady=10)
root.bind('<Return>', on_go_button_click)
root.mainloop()

