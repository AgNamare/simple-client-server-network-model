import vlc
import time
import cv2

def save_frames(media_path, output_dir):
    Instance = vlc.Instance("--no-xlib")  # Create a VLC instance

    # Create a MediaPlayer with the given media
    player = Instance.media_player_new()
    Media = Instance.media_new(media_path)
    Media.get_mrl()
    player.set_media(Media)

    player.play()

    # Wait for the video to start playing
    time.sleep(2)

    # Set up the video capture using OpenCV
    cap = cv2.VideoCapture()
    cap.open('vlc://quit')

    # Save each frame with a unique name
    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_name = f"frame_{frame_number}.png"
        cv2.imwrite(f"{output_dir}/{frame_name}", frame)

        frame_number += 1

    # Release resources
    cap.release()

if __name__ == "__main__":
    video_path = "C:/Users/AG/Downloads/videoplayback.mp4"
    output_directory = "C:/Users/AG/Downloads/frames"

    save_frames(video_path, output_directory)
    
