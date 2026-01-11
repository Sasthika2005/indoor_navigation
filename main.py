import cv2
import time
from camera.camera_stream import Camera
from vision.obstacle_detector import ObstacleDetector
from navigation.navigator import Navigator
from voice.speaker import Speaker

cam = Camera()
obstacle_ai = ObstacleDetector()
navigator = Navigator()
speaker = Speaker()

print("[INFO] Camera Navigation System Started")
last_speak_time = time.time()
frame_count = 0

while True:
    frame = cam.get_frame()
    if frame is None:
        break

    frame_count += 1
    
    # Process every 3rd frame for speed
    if frame_count % 3 == 0:
        obstacles = obstacle_ai.detect(frame)
        decision = navigator.decide(obstacles, frame.shape[1])
    
    # Show current decision
    cv2.putText(frame, decision if 'decision' in locals() else "Starting...", (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # Speak every 5 seconds
    current_time = time.time()
    if current_time - last_speak_time >= 5 and 'decision' in locals():
        print(f"[SPEAKING]: {decision}")
        speaker.speak(decision)
        last_speak_time = current_time
        print(f"[SPEAK ATTEMPT COMPLETED]")

    cv2.imshow("Camera Navigation", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()