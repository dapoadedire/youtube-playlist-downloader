# YouTube Playlist Downloader

A simple command-line tool to download YouTube playlists.



![Screenshot from 2024-04-20 17-09-52](https://github.com/dapoadedire/youtube-playlist-downloader/assets/95668340/68992d4b-909c-4c98-9395-6ae23a4f97b8)


## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [License](#license)

## Requirements

- Python 3.6 or higher
- `pytube` library
- `rich` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dapoadedire/youtube-playlist-downloader.git
```
2. Change to the project directory:
```bash
cd youtube-playlist-downloader
```
3. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
```
4. Activate the virtual environment:
```bash
source venv/bin/activate  # On macOS and Linux
venv\Scripts\activate  # On Windows
```
5. Install the required libraries:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python downloader.py
```
2. Enter the YouTube playlist URL when prompted.
3. Enter the number of videos to skip (default is 0).

The script will download the videos in the playlist to the "Downloads" folder in your home directory. If a video with the same name already exists in the destination folder, it will be skipped.

## License

This project is licensed under the terms of the MIT License.
