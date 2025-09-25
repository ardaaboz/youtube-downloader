# YouTube Video Downloader

A Python utility for downloading YouTube videos and audio with both command-line and GUI interfaces.

## Features

- **Multiple Interfaces**: Command-line script and GUI application
- **Quality Selection**: Download videos in different resolutions (highest, lowest, or specific)
- **Format Options**: Download as MP4 video or MP3 audio
- **Progress Tracking**: Real-time download progress with progress bars
- **Custom Output**: Choose download directory
- **Bulk Operations**: Support for continuous downloads

## Files

- `YoutubeDownloader.py` - Command-line interface version
- `quality.py` - GUI version with Tkinter interface

## Installation

### Requirements
```bash
pip install pytube
pip install tqdm
pip install tkinter  # Usually comes with Python
```

### Dependencies
- `pytube` - YouTube video downloading
- `tqdm` - Progress bar functionality
- `tkinter` - GUI interface (included with Python)
- `os` - File system operations

## Usage

### Command-Line Version
```bash
python YoutubeDownloader.py
```

1. Enter YouTube video URL
2. Choose format (mp4 for video, mp3 for audio)
3. File downloads to default directory
4. Option to download additional videos

### GUI Version
```bash
python quality.py
```

1. **YouTube Link**: Paste video URL
2. **File Type**: Select MP4 (video) or MP3 (audio only)
3. **Output Directory**: Choose download location
4. **Quality Options**: Select video resolution for MP4 downloads
5. Click **Download** to start

## Technical Implementation

### Core Functionality
- Uses `pytube.YouTube` for video stream access
- Implements quality filtering and resolution selection
- Progress tracking with `tqdm` library
- File system management with `os` module

### Video Download Process
```python
# Get highest resolution stream
stream = yt.streams.get_highest_resolution()
# Filter by specific quality
stream = yt.streams.filter(resolution=quality).first()
```

### Audio Extraction
```python
# Extract audio-only stream
stream = yt.streams.get_audio_only()
# Save as MP3 format
```

## Features Comparison

| Feature | Command-Line | GUI |
|---------|--------------|-----|
| Video Download | ✅ | ✅ |
| Audio Download | ⚠️ (Placeholder) | ✅ |
| Quality Selection | Highest only | Multiple options |
| Progress Bar | Console | System notifications |
| Directory Choice | Fixed | User selectable |
| User Interface | Terminal | Windows/Dialogs |

## Learning Outcomes

This project demonstrates:
- **API Integration**: Working with pytube library
- **File I/O Operations**: Download and save management
- **GUI Development**: Tkinter interface design
- **Error Handling**: Download validation and user feedback
- **Progress Tracking**: Real-time download monitoring
- **User Experience**: Both CLI and GUI interfaces

## Future Enhancements

- Complete MP3 implementation in command-line version
- Playlist download support
- Download history tracking
- Batch URL processing from file
- Resume interrupted downloads