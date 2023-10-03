import os
from pytube import Playlist, exceptions
from rich import print

def download(playlist_link: str, skip: int = 0):
    try:
        p = Playlist(playlist_link)
        playlist_name = p.title
        total_videos = len(p.videos)
        
        print(
            f"[bold yellow]Downloading playlist ({total_videos} videos):[/bold yellow][green]{playlist_name}[/green]"
        )
        
        os.makedirs(playlist_name, exist_ok=True)
        
        if skip < 0 or skip > total_videos:
            print(f"[bold red]Error: Invalid 'skip' value. It should be a positive integer not exceeding the total number of videos.[/bold red]")
            return
        
        for i, video in enumerate(p.videos, start=1):
            if i <= skip:
                print(
                    f"[bold blue]Skipping video {i} of {total_videos}:[/bold blue][green]{video.title}[/green]"
                )
                continue
            print(
                f"[bold yellow]Downloading video {i} of {total_videos}:[/bold yellow][green]{video.title}[/green]"
            )
            
            stream = (
                video.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
            filename = stream.default_filename
            filepath = os.path.join(playlist_name, filename)
            if os.path.exists(filepath):
                print(
                    f"[bold blue]Downloaded {filename} already, skipped\n[/bold blue]"
                )
            else:
                stream.download(output_path=playlist_name)
                print(f"[bold green]Downloaded {filename}, next\n[/bold green]")
        
        print(f"[bold green]All videos from the playlist downloaded.\n[/bold green]")
    
    except exceptions.PytubeError as e:
        print(f"[bold red]Error:[/bold red][green]{e}[/green]")

if __name__ == "__main__":
    playlist_link = input("Enter the playlist URL: ")
    # skip = input("Enter the number of videos to skip (default is 0): ")

    playlist_link="https://www.youtube.com/playlist?list=PL4867FBE3AD9BBD69"


    skip = input("Enter the number of videos to skip (default is 0): ")

    if skip:
        skip = int(skip)
    else:
        skip = 0

    
    
    download(playlist_link, skip)
