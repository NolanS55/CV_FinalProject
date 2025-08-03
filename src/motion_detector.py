# motion_detector.py
"""
Motion detection functions for the sports video analysis project.
"""

import cv2
import numpy as np

def detect_motion(frames, frame_idx, threshold=25, min_area=100):
    """
    Detect motion in the current frame by comparing with previous frame.

    Args:
        frames: List of video frames
        frame_idx: Index of the current frame
        threshold: Threshold for frame difference detection
        min_area: Minimum contour area to consider

    Returns:
        List of bounding boxes for detected motion regions
    """
    # We need at least 2 frames to detect motion
    if frame_idx < 1 or frame_idx >= len(frames):
        return []

    # Get current and previous frame
    current_frame = frames[frame_idx]
    prev_frame = frames[frame_idx - 1]

    # TODO: Implement motion detection
    # 1. Convert frames to grayscale
    # 2. Apply Gaussian blur to reduce noise (hint: cv2.GaussianBlur)
    # 3. Calculate absolute difference between frames (hint: cv2.absdiff)
    # 4. Apply threshold to highlight differences (hint: cv2.threshold)
    # 5. Dilate the thresholded image to fill in holes (hint: cv2.dilate)
    # 6. Find contours in the thresholded image (hint: cv2.findContours)
    # 7. Filter contours by area and extract bounding boxes

    # Example starter code:
    motion_boxes = []

    # Your implementation here

    return motion_boxes