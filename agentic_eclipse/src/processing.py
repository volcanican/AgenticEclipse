import cv2
import os

def extract_frames(video_path, output_folder="data/frames", interval=30):
    """
    this will extract 1 frame every 1 second of the video
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    cap = cv2.VideoCapture(video_path)
    count = 0
    saved_count = 0

    print(f"starting extraction for: {video_path}")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % interval == 0:
            frame_name = f"{output_folder}/frame_{saved_count:04d}.jpg"
            cv2.imwrite(frame_name, frame)
            saved_count += 1
        count += 1

    cap.release()
   
