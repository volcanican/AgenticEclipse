import sys
import cv2
import base64
import os
from src.agents import VideoAnalysisAgent

def get_frames(video_path, num_frames=6):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames = []
    
    if total_frames == 0:
        return []

    for i in range(num_frames):
        idx = int(total_frames * (i / num_frames))
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        success, frame = cap.read()
        if success:
            frame = cv2.resize(frame, (512, 512))
            _, buffer = cv2.imencode(".jpg", frame)
            frames.append(base64.b64encode(buffer).decode("utf-8"))
    cap.release()
    return frames

def analyze_video_web(video_path, user_prompt, selected_tone):
    # Ensure this matches the key you are using for the AMD Hackathon project
    API_KEY = "fw_5gBpgY5RLEpTukByXe5WHD" 
    agent = VideoAnalysisAgent(API_KEY)
    
    frames = get_frames(video_path)
    if not frames:
        return "Error: Could not extract frames."
        
    return agent.analyze_storyboard(frames, user_prompt, selected_tone)

def main(video_path):
    # CLI functionality maintained for your testing purposes
    pass 

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])