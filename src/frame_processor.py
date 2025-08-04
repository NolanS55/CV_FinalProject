# frame_processor.py
"""
Frame processing functions for the motion detection project.
"""

import cv2
import numpy as np


def process_video(video_path, target_fps=5, resize_dim=(1280, 720)):
    """
    Extract frames from a video at a specified frame rate.

    Args:
        video_path: Path to the video file
        target_fps: Target frames per second to extract
        resize_dim: Dimensions to resize frames to (width, height)

    Returns:
        List of extracted frames
    """

    cap = cv2.VideoCapture(video_path)

    original_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(original_fps / target_fps)

    frames = []
    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:

            cap.release()
            break

        if frame_count % frame_interval == 0:

            frame = cv2.resize(frame, resize_dim)
            frames.append(frame)

        frame_count += 1

    cap.release()
    return frames