import cv2
import numpy as np

def calculate_region_of_interest(motion_boxes, frame_shape):
    """
    Calculate the primary region of interest based on motion boxes.

    Args:
        motion_boxes: List of motion detection bounding boxes
        frame_shape: Shape of the video frame (height, width)

    Returns:
        Tuple (x, y, w, h) representing the region of interest center point and dimensions
    """

    if not motion_boxes:
        frame_height, frame_width = frame_shape[:2]
        return (frame_width // 2, frame_height // 2, 0, 0)
    
    center_X_list = [x + w // 2 for x, y, w, h in motion_boxes]
    center_Y_list = [y + h // 2 for x, y, w, h in motion_boxes]
    width_list = [w for x, y, w, h in motion_boxes]
    height_list = [h for x, y, w, h in motion_boxes]

    roi_center_X = int(np.mean(center_X_list))
    roi_center_Y = int(np.mean(center_Y_list))
    roi_width = int(max(width_list))
    roi_height = int(max(height_list))

    frame_height, frame_width = frame_shape[:2]
    roi_center_X = max(roi_width // 2, min(frame_width - roi_width // 2, roi_center_X))
    roi_center_Y = max(roi_height // 2, min(frame_height - roi_height // 2, roi_center_Y))

    return (roi_center_X, roi_center_Y, roi_width, roi_height)

def track_viewport(frames, motion_results, viewport_size, smoothing_factor=0.3):
    """
    Track viewport position across frames with smoothing.

    Args:
        frames: List of video frames
        motion_results: List of motion detection results for each frame
        viewport_size: Tuple (width, height) of the viewport
        smoothing_factor: Factor for smoothing viewport movement (0-1)
                          Lower values create smoother movement

    Returns:
        List of viewport positions for each frame as (x, y) center coordinates
    """

    viewport_positions = []

    if not frames:
        return viewport_positions

    frame_height, frame_width = frames[0].shape[:2]
    prev_center_X, prev_center_Y = frame_width // 2, frame_height // 2
    viewport_width, viewport_height = viewport_size

    for i, frame in enumerate(frames):
        motion_boxes = motion_results[i] if i < len(motion_results) else []
        roi_center_X, roi_center_Y, roi_width, roi_height = calculate_region_of_interest(motion_boxes, frame.shape)

        smoothed_center_X = int(prev_center_X * (1 - smoothing_factor) + roi_center_X * smoothing_factor)
        smoothed_center_Y = int(prev_center_Y * (1 - smoothing_factor) + roi_center_Y * smoothing_factor)

        smoothed_center_X = max(viewport_width // 2, min(frame_width - viewport_width // 2, smoothed_center_X))
        smoothed_center_Y = max(viewport_height // 2, min(frame_height - viewport_height // 2, smoothed_center_Y))

        viewport_positions.append((smoothed_center_X, smoothed_center_Y))
        prev_center_X, prev_center_Y = smoothed_center_X, smoothed_center_Y

    return viewport_positions
