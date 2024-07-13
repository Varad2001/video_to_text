import os



def process_videos(video_paths_file, output_dir, model):
    """Processes each video to convert it to text."""
    with open(video_paths_file, 'r') as file:
        video_paths = [line.strip() for line in file]
        print(video_paths)
    

if __name__ == "__main__":
    process_videos("video_paths.txt", "sfds", "sfs")