import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pytube
from tqdm import tqdm
from pytube import Playlist

def download_audio(link):
    yt = YouTube(link)
    title = yt.title
    print(f'Downloading {title}...')

    stream = yt.streams.get_audio_only()
    download_dir = output_dir.get()

    if not os.path.isdir(download_dir):
        os.mkdir(download_dir)

    output_file = f'{title}.mp3'

    file = stream.download(output_path=download_dir, filename=output_file)

    print(f'{title} downloaded successfully!')
    messagebox.showinfo("Download complete", f"{title} has been downloaded successfully!")


def download_video(link, quality='highest'):
    yt = pytube.YouTube(link)
    title = yt.title
    stream = None
    if quality == 'highest':
        stream = yt.streams.get_highest_resolution()
    elif quality == 'lowest':
        stream = yt.streams.get_lowest_resolution()
    else:
        stream = yt.streams.filter(resolution=quality).first()
    download_dir = output_dir.get()

    if not os.path.isdir(download_dir):
        os.mkdir(download_dir)

    output_file = f'{title}-{stream.resolution}.mp4'

    file = stream.download(output_path=download_dir, filename=output_file)

    print(f'{title} downloaded successfully!')
    messagebox.showinfo("Download complete", f"{title} has been downloaded successfully!")


def browse_output_dir():
    dir_path = filedialog.askdirectory()
    output_dir.set(dir_path)


def start_download():
    link = link_entry.get()
    file_type = file_type_var.get()
    quality = quality_var.get()

    if file_type == 'mp4':
        download_video(link, quality=quality)
    elif file_type == 'mp3':
        download_audio(link)

    choice = messagebox.askquestion("Download more?", "Do you want to download another file?")
    if choice == 'no':
        root.destroy()


root = tk.Tk()
root.title("YouTube Downloader")

link_label = tk.Label(root, text="YouTube link:")
link_label.grid(row=0, column=0)
link_entry = tk.Entry(root, width=50)
link_entry.grid(row=0, column=1)

file_type_label = tk.Label(root, text="File type:")
file_type_label.grid(row=1, column=0)
file_type_var = tk.StringVar()
file_type_var.set('mp4')
mp4_radio = tk.Radiobutton(root, text="MP4", variable=file_type_var, value='mp4')
mp4_radio.grid(row=1, column=1)
mp3_radio = tk.Radiobutton(root, text="MP3", variable=file_type_var, value='mp3')
mp3_radio.grid(row=1, column=2)

output_dir_label = tk.Label(root, text="Output directory:")
output_dir_label.grid(row=2, column=0)
output_dir = tk.StringVar()
output_dir.set(os.path.join(os.path.expanduser('~'), 'Downloads'))
output_dir_entry = tk.Entry(root, textvariable=output_dir, width=50)
output_dir_entry.grid(row=2, column=1)
tk.Button(root, text="Browse", command=browse_output_dir).grid(row=2, column=2)

tk.Button(root, text="Download", command=start_download).grid(row=3, column=1)

root.mainloop()