# Video to Text Conversion Script

## Description
This script converts videos to text using OpenAI Whisper for transcription. Each video is processed to extract audio and transcribe it into text files saved in a directory named after the video file.

## Requirements
- Python 3.x
- Required Python packages (listed in `requirements.txt`)
- `ffmpeg` (must be installed on your system)

## Installation
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Ensure `ffmpeg` is installed on your system:
    ```sh
    # On Ubuntu/Debian
    sudo apt update && sudo apt install ffmpeg

    # On MacOS
    brew install ffmpeg

    # On Windows
    choco install ffmpeg
    ```

## Usage
1. Create a `video_paths.txt` file with paths to your video files, one per line.
2. Run the script:
    ```sh
    python asr_whisper.py
    ```
3. The output text files will be saved in the `output` directory, each in a subdirectory named after the corresponding video file.

## Example `video_paths.txt`
```plaintext
/path/to/your/video1.mp4
/path/to/your/video2.mp4
```

## Developer Details 
Name : Varad Khonde<br>
Email : varadkhonde@gmail.com<br>
Profile : https://www.fiverr.com/varadkhonde

