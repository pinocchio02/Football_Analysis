# ⚽ Football Match Analysis Using Computer Vision

An end-to-end computer vision–based football (soccer) video analysis system that automatically extracts player-level and team-level insights from match footage using deep learning and video analytics.

This project is designed as a **portfolio project** to demonstrate applied skills in object detection, tracking, spatial analysis, and video processing.

---

## 🧠 Problem Statement

Football matches generate large volumes of video data, but manually extracting insights such as player movement, ball possession, and team performance is time-consuming and subjective.

This project aims to build an **automated football match analysis pipeline** that integrates detection, tracking, and analytical modules to produce performance metrics and tactical insights from raw match footage.

---

## ✨ Features

- 🧍 Player and referee detection & tracking  
- ⚽ Ball detection with possession assignment  
- 🎯 Marker on player currently possessing the ball  
- 🔢 Player number identification  
- 🎽 Automatic team assignment  
- 📊 Team-wise ball possession calculation  
- 🎥 Camera movement estimation  
- 📏 Player speed and distance estimation  
- 🎬 Annotated output video with visual overlays  

---

## 🛠️ Tech Stack

- Python 3.10.11  
- OpenCV  
- YOLOv8 (Ultralytics)  
- NumPy  
- Pandas  
- Matplotlib (used where applicable)  

---

## 📁 Project Structure

```text
Football_Analysis/
│
├── main.py
│   Entry point for running the football analysis pipeline
│
├── yolo_inference.py
│   YOLOv8 inference logic for players, referees, and ball detection
│
├── camera_movement_estimator/
│   └── camera_movement_estimator.py
│      Camera motion estimation between frames
│
├── player_ball_assigner/
│   └── player_ball_assigner.py
│      Assigns ball possession to players
│
├── speed_and_distance_estimator/
│   └── speed_and_distance_estimator.py
│      Computes player speed and total distance traveled
│
├── team_assigner/
│   └── team_assigner.py
│      Assigns players to teams
│
├── trackers/
│   └── tracker.py
│      Multi-object tracking logic
│
├── utils/
│   └── video_utils.py
│      Video read/write and utility functions
│
├── view_transformer/
│   └── view_transformer.py
│      Perspective and view normalization
│
├── development_and_analysis/
│   └── code_assignment.ipynb
│      Experimental analysis notebook (not required to run project)
│
├── training/
│   Dataset and YOLO training files (ignored in version control)
│
├── output_videos/
│   Generated output videos with visual annotations
│
├── .gitignore
├── .gitattributes
└── README.md

## 🚀 How to Run the Project

### 🔹 Step 1: Train the YOLO Model

Train the YOLO model on the football dataset:

```bash
yolo task=detect mode=train model=yolov5x.pt \
data="path/to/data.yaml" epochs=100 imgsz=640
After training, the following files are generated:

best.pt

last.pt

🔹 Step 2: Configure the Model Path
Place best.pt inside a local models/ directory and update the tracker initialization in the code:

python
Copy code
tracker = Tracker("models/best.pt")
🔹 Step 3: Provide Input Video
Specify the path of the football match video inside main.py.

🔹 Step 4: Run the Analysis
Execute the main script:

bash
Copy code
python main.py
🔹 Step 5: Output
An annotated output video is generated in the output_videos/ directory.

The output includes:

Player and ball tracking

Team assignment

Ball possession statistics

Speed and distance estimation

📌 Notes
Large files such as videos, datasets, trained models, and cache files are excluded using .gitignore

This project focuses on offline video analysis

Intended for learning, experimentation, and portfolio demonstration

👤 Author
Om Ramani
Master’s Student in Computer Science
Portfolio Project – Computer Vision & Deep Learning

📄 License
This project is intended for educational and portfolio purposes only.
