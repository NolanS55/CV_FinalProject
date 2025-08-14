import os
import cv2
import numpy as np

def visualize_results(frames, motion_results, viewport_positions, viewport_size,output_dir):
    """
    Create visualization of motion detection and viewport tracking results.

    Args:
        frames: List of video frames
        motion_results: List of motion detection results for each frame
        viewport_positions: List of viewport center positions for each frame
        viewport_size: Tuple (width, height) of the viewport
        output_dir: Directory to save visualization results
    """


    frames_dir = os.path.join(output_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)

    viewport_dir = os.path.join(output_dir, "viewport")
    os.makedirs(viewport_dir, exist_ok=True)

    height, width = frames[0].shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_path = os.path.join(output_dir, "motion_detection.mp4")
    video_writer = cv2.VideoWriter(video_path, fourcc, 5, (width, height))

    viewport_video_path = os.path.join(output_dir, "viewport_tracking.mp4")
    vp_width, vp_height = viewport_size
    viewport_writer = cv2.VideoWriter(
        viewport_video_path, fourcc, 5, (vp_width, vp_height)
    )

    viewport_writer = cv2.VideoWriter(viewport_video_path, fourcc, 5, (vp_width, vp_height))


    #Implementation of visualization 
    for i, frame in enumerate(frames):
        visFrame = frame.copy()

        motionBoxes = motion_results[i] if i < len(motion_results) else []
        for x, y, w, h in motionBoxes:
            topLeft = (x, y)
            bottomRight = (x + w, y + h)
            cv2.rectangle(visFrame, topLeft, bottomRight, (0, 255, 0), 2)

        centerX, centerY = viewport_positions[i] if i < len(viewport_positions) else (width // 2, height // 2)
        topLeft = (max(centerX - vp_width // 2, 0), max(centerY - vp_height // 2, 0))
        bottomRight = (min(centerX + vp_width // 2, width), min(centerY + vp_height // 2, height))
        cv2.rectangle(visFrame, topLeft, bottomRight, (255, 0, 0), 2)

        viewportFrame = visFrame[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]]

        cv2.putText(visFrame, f"Frame {i+1}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        framePath = os.path.join(frames_dir, f"frame_{i+1:04d}.png")
        viewportPath = os.path.join(viewport_dir, f"viewport_{i+1:04d}.png")
        cv2.imwrite(framePath, visFrame)
        cv2.imwrite(viewportPath, viewportFrame)

        video_writer.write(visFrame)
        viewport_writer.write(viewportFrame)

    video_writer.release()
    viewport_writer.release()

    print(f"Visualization saved to {video_path}")
    print(f"Viewport video saved to {viewport_video_path}")
    print(f"Individual frames saved to {frames_dir} and {viewport_dir}")