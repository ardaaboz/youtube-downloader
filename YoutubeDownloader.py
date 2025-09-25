import os
import pytube
import tqdm

def download_video(link):
    yt = pytube.YouTube(link)
    title = yt.title
    print(f'Downloading {title}...')
    
    streams = yt.streams.filter(progressive=True, file_extension='mp4')
    stream = streams.order_by('resolution').desc().first()
    
    download_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'Python', 'Projects', 'YoutubeDownloader', 'Downloaded Files')
    output_file = f'{title}.mp4'
    
    file = stream.download(output_path=download_dir, filename=output_file)
    
    with tqdm.tqdm(total=stream.filesize, unit='B', unit_scale=True, desc=output_file, ascii=True) as bar:
        with open(file, 'rb') as f:
            while True:
                buffer = f.read(4096)
                if not buffer:
                    break
                bar.update(len(buffer))
    
    print(f'{title} downloaded successfully!')

if __name__ == '__main__':
    while True:
        link = input('Enter the YouTube link: ')
        file_type = input("Enter 'mp3' to download as an audio file or 'mp4' to download as a video file: ")
        
        if file_type == 'mp4':
            download_video(link)
        elif file_type == 'mp3':
            # Implement mp3 download logic here
            pass
        
        choice = input('Do you want to download another file? (y/n): ')
        if choice.lower() != 'y':
            break

print("Program terminated.")
