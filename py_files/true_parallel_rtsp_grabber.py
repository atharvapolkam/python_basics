import cv2
import os
import time
from multiprocessing import Process
from datetime import datetime

def capture_image(rtsp_url, channel_id):
    try:
        cap = cv2.VideoCapture(rtsp_url)
        success, frame = cap.read()
        cap.release()

        if success:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            os.makedirs("rtsp_snapshots", exist_ok=True)
            filename = f"rtsp_snapshots/channel_{channel_id}_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"[✓] {timestamp} - Channel {channel_id} saved")
        else:
            print(f"[x] Failed: Channel {channel_id}")
    except Exception as e:
        print(f"[!!] Error in channel {channel_id}: {e}")

def run_all_once():
    base_url = "rtsp://admin:west1%40123@115.246.37.172:554/Streaming/Channels"
    processes = []

    for ch in range(1, 9):
        rtsp_url = f"{base_url}/{ch * 100 + 1}"  # adjust this pattern if needed
        p = Process(target=capture_image, args=(rtsp_url, ch))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

def main_loop(interval_seconds=10):
    while True:
        print("\n⏱️  Starting snapshot cycle...\n")
        run_all_once()
        print(f"⏳ Waiting {interval_seconds} seconds for next cycle...\n")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main_loop(interval_seconds=1)  # Change interval as needed
