import cv2
import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
import shutil  

def extract_frames(video_path, output_folder, frame_interval=30):
    cap = cv2.VideoCapture(video_path)
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if count % frame_interval == 0:
            frame_path = os.path.join(output_folder, f'frame_{count}.jpg')
            cv2.imwrite(frame_path, frame)
        count += 1
    cap.release()

def is_image_file(file_path):
    # Check if the file has a valid image extension
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
    return any(file_path.lower().endswith(ext) for ext in image_extensions)

def resize_image(image_path):
    if not is_image_file(image_path):
        print(f"Skipping non-image file: {image_path}")
        return
    try:
        with Image.open(image_path) as img:
            img = img.resize((256, 256))  # Resize image
            img.save(image_path)  # Save the resized image
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def normalize_image(image_path):
    if not is_image_file(image_path):
        print(f"Skipping non-image file: {image_path}")
        return
    try:
        with Image.open(image_path) as img:
            img_array = np.array(img) / 255.0  # Normalize pixel values
            img = Image.fromarray((img_array * 255).astype(np.uint8))  # Convert back to image
            img.save(image_path)  # Save the normalized image
    except Exception as e:
        print(f"Error normalizing {image_path}: {e}")

def split_dataset(dataset_dir, output_dirs, split_ratio=(0.8, 0.1, 0.1)):
    all_files = []
    for gesture_dir in os.listdir(dataset_dir):
        gesture_path = os.path.join(dataset_dir, gesture_dir)
        if os.path.isdir(gesture_path):
            files = [os.path.join(gesture_path, f) for f in os.listdir(gesture_path) if is_image_file(os.path.join(gesture_path, f))]
            all_files.extend(files)
    
    train_files, test_files = train_test_split(all_files, test_size=(1 - split_ratio[0]))
    val_files, test_files = train_test_split(test_files, test_size=(split_ratio[2] / (split_ratio[1] + split_ratio[2])))

    for file_set, output_dir in zip([train_files, val_files, test_files], output_dirs):
        os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist
        for file in file_set:
            shutil.copy(file, os.path.join(output_dir, os.path.basename(file)))

def process_videos_in_folder(videos_folder, output_base_folder, frame_interval=30):
    for video_file in os.listdir(videos_folder):
        if video_file.endswith(('.mp4', '.avi', '.mov', '.mkv')):  
            video_path = os.path.join(videos_folder, video_file)
            video_name = os.path.splitext(video_file)[0]  
            output_folder = os.path.join(output_base_folder, video_name)  # Create a subfolder for each video
            os.makedirs(output_folder, exist_ok=True)  # Create the subfolder if it doesn't exist
            
            # Extract frames from the video and save them in the subfolder
            extract_frames(video_path, output_folder, frame_interval)

            # Process each image (resize and normalize)
            image_files = [f for f in os.listdir(output_folder) if is_image_file(os.path.join(output_folder, f))]
            for image_file in image_files:
                image_path = os.path.join(output_folder, image_file)
                resize_image(image_path)
                normalize_image(image_path)

if __name__ == "__main__":
    videos_folder = "downloads"  # Folder containing multiple video files
    output_base_folder = "processed_videos"  # Folder where all frames will be stored
    frame_interval = 10  # Set the interval for frame extraction
    
    process_videos_in_folder(videos_folder, output_base_folder, frame_interval)
