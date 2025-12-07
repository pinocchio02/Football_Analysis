from ultralytics import YOLO
import cv2

model = YOLO('models/best.pt')

input_path = r'input_videos\A1606b0e6_0.mp4'
cap = cv2.VideoCapture(input_path)

# Get video info
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# MP4 writer (forces MP4 output)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("final_output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO on each frame
    results = model(frame)

    # Draw detections on frame
    annotated = results[0].plot()

    # Save to MP4
    out.write(annotated)

cap.release()
out.release()

print("✅ Output saved as final_output.mp4")
