# Video Converter

A simple GUI application to convert MOV files to MP4 or MKV format while maintaining video quality.

## Features

- Convert MOV files to MP4 or MKV format
- Maintain original video quality
- Simple and intuitive user interface
- Dark mode support
- Progress tracking
- Error handling

## Requirements

- Python 3.x
- FFmpeg
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Constant0605/mov-to-mp4-video-converter
cd video-converter
```

2. Install FFmpeg:
   - Download FFmpeg from [official website](https://ffmpeg.org/download.html)
   - Extract to `C:\ffmpeg`
   - Add `C:\ffmpeg\bin` to your system's PATH

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python video_converter.py
```

2. Click "Browse" to select a MOV file
3. Choose output format (MP4 or MKV)
4. Click "Convert" to start the conversion
5. The converted file will be saved in the same directory as the input file

## Configuration

The application uses the following FFmpeg settings for optimal quality:
- Video codec: H.264 (libx264)
- Audio codec: AAC
- Preset: medium (good balance between quality and speed)
- CRF: 23 (good quality, lower is better)
- Audio bitrate: 192k

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Constant

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 