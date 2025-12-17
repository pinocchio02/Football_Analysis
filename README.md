⚽ Football Match Analysis Using Computer Vision
📌 Overview

Football (soccer) generates massive amounts of video data during matches, but extracting meaningful insights from this footage remains a challenge. Analysts and coaches require accurate and automated tools to evaluate player performance, team strategies, ball control, and movement patterns.

This project presents a computer vision–based football match analysis system that automatically processes match footage to extract performance metrics and tactical insights.
The system integrates detection, tracking, and analysis modules to produce an annotated output video highlighting key events and statistics.

This project is developed as a portfolio-focused computer vision project, demonstrating practical application of deep learning and video analytics in sports.

🎯 Key Features

🧍‍♂️ Player & Referee Detection and Tracking

⚽ Ball Detection and Tracking

🟡 Marker on Player Possessing the Ball

🔢 Player Number Identification

🎽 Team Assignment

📊 Team-wise Ball Possession Analysis

🎥 Camera Movement Estimation

📏 Player Speed and Distance Estimation

🎬 Annotated Output Video with Visual Overlays

🛠️ Tech Stack

Python 3.10.11

OpenCV – Video processing and visualization

YOLOv8 (Ultralytics) – Object detection (players, ball, referees)

NumPy – Numerical computations

Pandas – Data handling (metrics/statistics)

📁 Project Structure

Football_Analysis/
│
├── main.py
│   # Entry point for running football video analysis
│
├── yolo_inference.py
│   # YOLOv8 inference logic for player, referee, and ball detection
│
├── camera_movement_estimator/
│   └── camera_movement_estimator.py
│      # Estimates camera motion between frames to normalize player movement
│
├── player_ball_assigner/
│   └── player_ball_assigner.py
│      # Assigns ball possession to the closest player
│
├── speed_and_distance_estimator/
│   └── speed_and_distance_estimator.py
│      # Computes player speed and total distance traveled
│
├── team_assigner/
│   └── team_assigner.py
│      # Assigns players to teams based on visual features
│
├── trackers/
│   └── tracker.py
│      # Multi-object tracking logic for players and ball
│
├── utils/
│   └── video_utils.py
│      # Utility functions for reading, writing, and processing videos
│
├── view_transformer/
│   └── view_transformer.py
│      # Performs view normalization / perspective transformation
│
├── development_and_analysis/
│   └── code_assignment.ipynb
│      # Experimental analysis and development notebook (not required for execution)
│
├── training/
│   # Dataset and YOLO training files (ignored in version control)
│
├── output_videos/
│   # Generated output videos with visual overlays
│
├── .gitignore
│   # Excludes models, videos, datasets, and cache files
│
├── .gitattributes
│   # Git configuration for repository consistency
│
└── README.md
   # Project documentation

🚀 How to Run the Project
1️⃣ Train the YOLO Model

First, train the player detection model using YOLO (example command):

yolo task=detect mode=train model=yolov5x.pt \
data="path/to/data.yaml" \
epochs=100 imgsz=640


After training, YOLO will generate:

best.pt

last.pt

2️⃣ Set Up the Model

Copy best.pt into the models/ directory

Update the model path inside the tracker:

tracker = Tracker("models/best.pt")

3️⃣ Provide Input Video

In main.py, set the path of the input football match video:

input_video_path = "input_videos/your_video.mp4"

4️⃣ Run the Analysis

Execute:

python main.py

5️⃣ Output

The system generates an annotated output video

Displays:

Player & ball tracking

Team assignment

Ball possession

Speed & distance traveled

Camera motion compensation

📌 Notes

Large files (.pt, .mp4, datasets, cache files) are excluded using .gitignore

The project focuses on end-to-end video analysis, not real-time deployment

Designed for learning, experimentation, and portfolio demonstration

🎓 Use Case

Sports analytics

Performance evaluation

Tactical analysis

Computer vision learning project

Portfolio demonstration for CV / ML roles

🔮 Future Improvements

Real-time inference optimization

Improved jersey number recognition

Advanced tactical heatmaps

Player role classification

Multi-camera support

👤 Author

Om Ramani
Master’s Student in Computer Science
Portfolio Project – Computer Vision & Deep Learning

📄 License

This project is intended for educational and portfolio purposes.
