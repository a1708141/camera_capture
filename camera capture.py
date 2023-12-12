import cv2
import time
import os

def record_and_save_video(output_folder, duration_seconds=10, capture_device=0, fps=30):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(capture_device)

    # Set the video width and height
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video = cv2.VideoWriter('output_video.avi', fourcc, fps, (width, height))

    # Calculate the number of frames to capture based on duration and fps
    num_frames = int(duration_seconds * fps)

    # Record video for the specified duration
    for _ in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            break

        # Generate a unique filename based on the current timestamp
        timestamp = int(time.time())
        frame_filename = f"{output_folder}/frame_{timestamp}_{_}.png"

        # Save the frame as an image
        cv2.imwrite(frame_filename, frame)

        # Write the frame to the output video file
        output_video.write(frame)

    # Release the VideoCapture and VideoWriter objects
    cap.release()
    output_video.release()

    print(f"Video recorded and frames saved to {output_folder}")

if __name__ == "__main__":
    output_folder = r"C:\Users\viper\Documents\Intership documentation\camera_feed"
    duration_seconds = 0.5
    capture_device = 0  # Change this if using a different camera
    fps = 10

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    record_and_save_video(output_folder, duration_seconds, capture_device, fps)
