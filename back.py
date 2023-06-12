# Creating a YouTube video downloader using python

"""Importing pytube library which is used for downloading YouTube videos using python
and ssl library which is used to create an unverified context for downloading the videos."""

# from tkinter import *
import ssl
import tkinter as tk
from tkinter.ttk import Progressbar
from pytube import YouTube
import requests

ssl._create_default_https_context = ssl._create_unverified_context


def download_video(URL):
    try:
        yt = YouTube(URL)
        title = yt.title
        views = yt.views
        length = yt.length
        rating = yt.rating
        description = yt.description
        thumbnail = yt.thumbnail_url
        video = yt.streams.get_highest_resolution()

        # Create a progress bar window
        progress_window = tk.Toplevel()
        progress_window.geometry("462x319")
        progress_window.configure(bg="white")
        progress_window.title("Downloading Video")
        canvas = tk.Canvas(
            progress_window, bg="#FFFFFF", height=519, width=862,
            bd=0, highlightthickness=0, relief="ridge")

        canvas.create_text(
            0.0, 0.0, text=title,
            fill="#515486", font=("Arial-BoldMT", int(13.0)), anchor="w")

        progress_label = tk.Label(progress_window, text="Downloading Video:")
        progress_label.pack()
        progress_bar = Progressbar(progress_window, length=300)
        progress_bar.pack()

        def update_progress(total_size, downloaded_size, _):
            # Calculate the download progress
            progress = int((downloaded_size / total_size) * 100)

            # Update the progress bar
            progress_bar["value"] = progress
            progress_window.update_idletasks()

        # Get the video file URL
        video_url = video.url

        # Send a GET request to download the video file
        response = requests.get(video_url, stream=True)

        # Get the total file size
        total_size = int(response.headers.get("Content-Length", 0))

        # Open a file to save the video
        with open("video.mp4", "wb") as file:
            downloaded_size = 0

            # Iterate over the response content in chunks and write to the file
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                downloaded_size += len(chunk)

                # Call the progress callback to update the progress bar
                update_progress(total_size, downloaded_size, None)

        # Show the video data in the console when download is complete
        print(f"Title: {title}\nViews: {views}\nLength: {length} seconds")

        # Close the progress bar window
        progress_window.destroy()
    except Exception as e:
        print(f"Error: {str(e)}")