
import os
import moviepy.editor as mp
import whisper


ASR_MODEL_NAME = "small"                    # available models(increasing complexity): "tiny", "base", "small", "medium", "large"
INPUTS_PATHS_FILE_NAME = "video_paths.txt"  # Path to your txt file containing video paths
OUTPUTS_DIR = "outputs"                     # Directory to save the text files


def convert_video_to_audio(video_path, audio_path):
    """Converts a video file to an audio file."""
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def transcribe_audio_to_text(audio_path, model):
    """Transcribes audio to text using OpenAI Whisper."""
    result = model.transcribe(audio_path)
    return result['text']

def process_videos(video_paths_file, output_dir, model):
    """Processes each video to convert it to text."""
    with open(video_paths_file, 'r') as file:
        video_paths = [line.strip() for line in file]
    
    for video_path in video_paths:
        video_filename = os.path.basename(video_path)
        video_name, _ = os.path.splitext(video_filename)
        
        output_subdir = os.path.join(output_dir, video_name)
        os.makedirs(output_subdir, exist_ok=True)
        
        audio_path = os.path.join(output_subdir, video_name + '.wav')
        text_path = os.path.join(output_subdir, video_name + '.txt')
        
        print(f"\nProcessing video: {video_path}")
        
        # Convert video to audio
        convert_video_to_audio(video_path, audio_path)
        
        # Convert audio to text
        text = transcribe_audio_to_text(audio_path, model)
        
        # Save text to file
        with open(text_path, 'w') as text_file:
            text_file.write(text)
        
        print(f"Finished processing video: {video_path}")
        print(f"Saved the transcripts to : {text_path}")


if __name__ == "__main__":
    video_paths_file = INPUTS_PATHS_FILE_NAME  
    output_dir =  OUTPUTS_DIR
    
    print(f'\nStarting the video to text process...\n')
    
    # Load the Whisper model
    model = whisper.load_model(ASR_MODEL_NAME)
    
    process_videos(video_paths_file, output_dir, model)
