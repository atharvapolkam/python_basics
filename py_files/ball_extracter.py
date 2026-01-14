import cv2
import os

video_path = "/home/atharva/vct/commands/dough_counting.mp4"
output_dir = "./dough_dataset"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_id % 50 == 0:  # Save every 5th frame (adjust if needed)
        cv2.imwrite(os.path.join(output_dir, f"frame_{frame_id}.jpg"), frame)

    frame_id += 1

cap.release()
print("Done extracting frames:", frame_id)
