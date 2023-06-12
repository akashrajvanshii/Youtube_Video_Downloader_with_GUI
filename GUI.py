import threading
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.messagebox as tk1

from pathlib import Path
from back import download_video

ASSETS_PATH = Path(__file__).resolve().parent / "assets"


def btn_clicked():
    URL = URL_entry.get()
    if not URL:
        messagebox.showerror(title="Empty Fields!", message="Please enter URL.")
        return
    else:
        # Create a new thread to download the video
        threading.Thread(target=download_video, args=(URL,), daemon=True).start()

window = tk.Tk()
window.title("YouTube Video Downloader")

window.geometry("1100x666")
window.configure(bg="black")
canvas = tk.Canvas(
    window, height=666, width=445,
    bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

canvas2 = tk.Canvas(
    window, bg="white", height=666, width=655,
    bd=0, highlightthickness=0, relief="ridge")
canvas2.place(x=446, y=0)

# Load the background image
background_image = tk.PhotoImage(file="assets/Image.png")

# Create a background image item on the canvas
background = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

text_box_bg = tk.PhotoImage(file=ASSETS_PATH / "TextBox_Bg.png")
URL_entry_img = canvas2.create_image(320, 342, image=text_box_bg)

URL_entry = tk.Entry(bd=0, bg="#F6F7F9", fg="#515486", highlightthickness=0, font=("INTER-Light", int(15.0)))
URL_entry.place(x=483.0, y=328.5, width=568.0, height=52)

intro_img = tk.PhotoImage(file=ASSETS_PATH / "intro.png")
intro = canvas2.create_image(320, 160, image=intro_img)

canvas2.create_text(
    40.0, 317.0, text="Enter Youtube URL : ", fill="black",
    font=("INTER-Light", int(20.0)), anchor="w")


Download_img_bg = tk.PhotoImage(file=ASSETS_PATH / "Download.png")
generate_btn = tk.Button(
    image=Download_img_bg, borderwidth=0, highlightthickness=0,
    command=btn_clicked, bg="#FFFFFF", cursor="hand2")
generate_btn.place(x=850, y=420)


# Download_img = canvas2.create_image(520, 480, image=Download_img_bg,)
window.mainloop()
