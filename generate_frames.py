import cv2
import os

# Load the video
video_path = "Garden Video.mp4"
cap = cv2.VideoCapture(video_path)

# Variables for frame extraction
current_frame = 0
frame_skip = 20  # Adjust the frame skip value as per your needs

# Create a directory to store the frames
frames_dir = "frames"
os.makedirs(frames_dir, exist_ok=True)

while cap.isOpened():
    # Read a frame from the video
    for _ in range(frame_skip):
        ret, frame = cap.read()

    if not ret:
        break

    # Resize the frame to a desired resolution
    frame = cv2.resize(frame, (800, 1000))  # Adjust the resolution as per your needs

    # Compress the image using JPEG compression with adjustable quality
    _, encoded_frame = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])  # Adjust the quality value (0-100) as per your needs

    # Save the compressed frame as a file
    frame_filename = f"frame_{current_frame}.jpg"
    frame_path = os.path.join(frames_dir, frame_filename)
    with open(frame_path, 'wb') as f:
        f.write(encoded_frame.tobytes())

    current_frame += 1

cap.release()
cv2.destroyAllWindows()