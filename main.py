import os
from pytube import Playlist, exceptions
from rich import print

# Constants
DOWNLOADING_PLAYLIST_MESSAGE = "[bold yellow]Downloading playlist ({total_videos} videos):[/bold yellow][green]{playlist_name}[/green]"
SKIPPING_VIDEO_MESSAGE = "[bold blue]Skipping video {video_num} of {total_videos}:[/bold blue][green]{video_title}[/green]"
DOWNLOADING_VIDEO_MESSAGE = "[bold yellow]Downloading video {video_num} of {total_videos}:[/bold yellow][green]{video_title}[/green]"
DOWNLOADED_ALREADY_MESSAGE = "[bold blue]Downloaded {filename} already, skipped\n[/bold blue]"
DOWNLOADED_MESSAGE = "[bold green]Downloaded {filename}, next\n[/bold green]"
ALL_VIDEOS_DOWNLOADED_MESSAGE = "[bold green]All videos from the playlist downloaded.\n[/bold green]"
ERROR_MESSAGE = "[bold red]Error:[/bold red][green]{error}[/green]"
INVALID_SKIP_MESSAGE = "[bold red]Error: Invalid 'skip' value. It should be a positive integer not exceeding the total number of videos.[/bold red]"

def download(playlist_link: str, skip: int = 0):
    """
    Download a YouTube playlist.

    Parameters:
    playlist_link (str): The URL of the playlist.
    skip (int, optional): The number of videos to skip. Default is 0.
    """
    try:
        p = Playlist(playlist_link)
        playlist_name = p.title
        total_videos = len(p.videos)

        print(DOWNLOADING_PLAYLIST_MESSAGE.format(total_videos=total_videos, playlist_name=playlist_name))

        # Create the "Downloads" folder if it doesn't exist
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        os.makedirs(downloads_folder, exist_ok=True)

        # Create the playlist folder inside the "Downloads" folder
        playlist_folder = os.path.join(downloads_folder, playlist_name)
        os.makedirs(playlist_folder, exist_ok=True)

        if skip < 0 or skip > total_videos:
            print(INVALID_SKIP_MESSAGE)
            return

        for i, video in enumerate(p.videos, start=1):
            if i <= skip:
                print(SKIPPING_VIDEO_MESSAGE.format(video_num=i, total_videos=total_videos, video_title=video.title))
                continue
            print(DOWNLOADING_VIDEO_MESSAGE.format(video_num=i, total_videos=total_videos, video_title=video.title))

            stream = (
                video.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
            filename = stream.default_filename
            filepath = os.path.join(playlist_folder, filename)
            if os.path.exists(filepath):
                print(DOWNLOADED_ALREADY_MESSAGE.format(filename=filename))
            else:
                stream.download(output_path=playlist_folder)
                print(DOWNLOADED_MESSAGE.format(filename=filename))

        print(ALL_VIDEOS_DOWNLOADED_MESSAGE)

    except exceptions.PytubeError as e:
        print(ERROR_MESSAGE.format(error=e))
    except Exception as e:
        print(ERROR_MESSAGE.format(error=e))

def get_user_input():
    """Get user input for the playlist URL and the number of videos to skip."""
    playlist_link = input("Enter the playlist URL: ")
    skip = input("Enter the number of videos to skip (default is 0): ")

    try:
        if skip:
            skip = int(skip)
        else:
            skip = 0
    except ValueError:
        print("[bold red]Error: Invalid 'skip' value. It should be a positive integer.[/bold red]")
        return None, None

    return playlist_link, skip

if __name__ == "__main__":
    playlist_link, skip = get_user_input()
    if playlist_link and skip is not None:
        download(playlist_link, skip)
