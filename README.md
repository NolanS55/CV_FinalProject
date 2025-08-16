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

## The Approach

- **Course Research**: Started by sourcing through course curriculum to find information that could be of assistance.
- **Online Research**: Conducted further online research for sports video analysis and motion detecting.
- **Meetings**: Scheduled meetings together and planned outside of them as well to split work and aim for dates to be finished.
- **Coding**: Using prior research, implemented coding solutions while communicating with eachother about how to approach and implement them.
- **Video sourcing**: Sourced some videos through online stock footage platforms that would be suitable for the use case of a sports motion detector.
- **Testing**: Tested and made necessary changes where needed.
- **Cleanup**: Cleaned up code to have similar variabl name formats along all files and follow same practices in structure.

## Key Decisions

- Setting the frame rate to 5 fps. We chose this frame rate as to limit the processing it would need to take to scan through the video with minimal gains overall.
- 5 fps also allowed for fast but accurate training.
- Setting a default viewport size 720x480 (4:3 or 16:9) to handle modern aspect videos.
- Used gaussian blur for preprocessing to improve accuracy of motion detection.

## Challenges

- Finding time to work together, scheduling meetup times.
- Planning the work, ex: communicating approaches and solutions to the project.
- Finding documentation to aid with solutions through course content and online sources.

## Improvements

- Could use some tweaking to adjust sensitvity of motion, as background objects are being detected a lot in some videos.
- Higher quality video processing, maybe 1920x1080 or 2560x1440 to preserve detail.
- Better zoom in/out for viewport tracking.
- Possible real time preview of the content instead of just saving to the device.
