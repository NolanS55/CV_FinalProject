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
    if frame_idx < 1 or frame_idx >= len(frames):
        return []

    currFrame = frames[frame_idx]
    prevFrame = frames[frame_idx - 1]

    grayCurr = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    grayPrev = cv2.cvtColor(prevFrame, cv2.COLOR_BGR2GRAY)

    blurCurr = cv2.GaussianBlur(grayCurr, (21, 21), 0)
    blurPrev = cv2.GaussianBlur(grayPrev, (21, 21), 0)

    diff = cv2.absdiff(blurPrev, blurCurr)
    _, threshImg = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(threshImg, None, iterations=2)

    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motionBoxes = []
    for cnt in contours:
        if cv2.contourArea(cnt) < min_area:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        motionBoxes.append((x, y, w, h))

    return motionBoxes