# Sports Motion Detection & Tracking

This project implements a system for detecting motion in sports videos and visualizes a viewport that follows the action. It is useful for automating analysis or focusing on the most interesting parts (ROI) of sport videos.

## How to Run

**1. Clone this Repository**

```
git clone https://github.com/NolanS55/CV_FinalProject.git
```

**2. Prepare your video**
- Create a `data` folder in the project root.
- Place any sports video with motion inside. (ex. sample_video_clip.mp4)
   
**4. Navigate to the `src` directory**

```
cd src
```

**4. Run the Script**

```
python main.py --video ../data/video_file.mp4
```
- Replace video_file.mp4 with the file you have placed inside of the data folder.

## Contributions
- **Nolan Smith** - motion_detector.py & visualizer.py  
- **Christian Duarte** - viewport_tracker.py  
- **Christian Ricci** - frame_processor.py & README.md 
