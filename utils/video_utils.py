import cv2

def read_video(video_path):
    print("Reading:", video_path)
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    print("Total frames read:", len(frames))
    return frames

def save_video(output_video_frames, output_video_path):
    if len(output_video_frames) == 0:
        raise ValueError("save_video() ERROR: No frames to save. output_video_frames is EMPTY.")

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    h, w = output_video_frames[0].shape[:2]
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (w, h))

    for frame in output_video_frames:
        out.write(frame)

    out.release()