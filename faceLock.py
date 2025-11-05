from deepface import DeepFace
import cv2
import pyautogui
import time

def ai_unlock():
    print("🔓 Checking user identity...")

    known_image = "faces/anish.jpg"
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    face_recognized = False
    start_time = time.time()

    while time.time() - start_time < 10:
        ret, frame = video_capture.read()
        if not ret:
            continue

        # Save current frame
        cv2.imwrite("current.jpg", frame)

        # Compare faces using DeepFace
        try:
            result = DeepFace.verify(img1_path=known_image, img2_path="current.jpg", model_name="VGG-Face")
            if result["verified"]:
                face_recognized = True
                break
        except:
            pass

        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

    if face_recognized:
        print("✅ Verified — Unlocking PC...")
        pyautogui.typewrite("8989")
        pyautogui.press("enter")
    else:
        print("❌ Unauthorized face detected — Lock denied.")
