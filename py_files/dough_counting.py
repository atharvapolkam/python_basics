import cv2
import numpy as np

video_path = "/home/atharva/vct/commands/dough_counting.mp4"
cap = cv2.VideoCapture(video_path)

# Background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=40, detectShadows=False)

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)


# Counting variables
count = 0
line_y = 560  # Adjust based on your belt area
prev_centroids = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1280, 720))  # Resize for performance (optional)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7,7), 0)

    fgmask = fgbg.apply(blurred)

    # Remove noise and fill holes
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, kernel, iterations=2)

    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    current_centroids = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 200:  # ignore noise
            continue

        x, y, w, h = cv2.boundingRect(cnt)
        cx, cy = x + w//2, y + h//2
        current_centroids.append((cx, cy))

        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Count if crosses the line going downwards
        if cy > line_y and not any(abs(cx - pcx) < 40 and abs(cy - pcy) < 40 
                                   for pcx, pcy in prev_centroids):
            count += 1

    prev_centroids = current_centroids.copy()

    # Draw counting line
    cv2.line(frame, (0, line_y), (1280, line_y), (0, 255, 0), 3)
    
    # Display count
    cv2.putText(frame, f"Count: {count}", (50, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3)

    cv2.imshow("Dough Ball Counting", frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Final Count:", count)
