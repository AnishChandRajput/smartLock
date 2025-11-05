import cv2
import os
import time
from deepface import DeepFace
import winsound

# === CONFIGURATION ===
KNOWN_FACE = os.path.join(os.getcwd(), "faces", "anish.jpg")  # Full path to your face image
CHECK_INTERVAL = 5          # Seconds between checks
LOCK_DELAY = 15             # Seconds before lock after no detection

# === INITIAL SETUP ===
last_seen = time.time()
print("🎥 SmartLock AI started — monitoring your presence...\n")

def lock_pc():
    print("🔒 Face not detected — locking PC.")
    winsound.Beep(600, 400)
    os.system("rundll32.exe user32.dll,LockWorkStation")

# === MAIN LOOP ===
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cam.isOpened():
    print("❌ Cannot access camera. Exiting...")
    exit()

while True:
    ret, frame = cam.read()

    if not ret:
        print("⚠️ Camera read error. Retrying...")
        time.sleep(CHECK_INTERVAL)
        continue

    temp_frame_path = "current_frame.jpg"
    cv2.imwrite(temp_frame_path, frame)

    try:
        result = DeepFace.verify(
            img1_path=KNOWN_FACE,
            img2_path=temp_frame_path,
            model_name="VGG-Face",
            enforce_detection=False
        )

        if result["verified"]:
            print("✅ Face recognized — system remains unlocked.")
            last_seen = time.time()
        else:
            print("⚠️ Unknown face detected — monitoring...")

    except Exception as e:
        print(f"⚠️ Detection error: {e}")

    if time.time() - last_seen > LOCK_DELAY:
        lock_pc()
        last_seen = time.time() + 60  # Avoid multiple locks back-to-back

    time.sleep(CHECK_INTERVAL)

cam.release()
cv2.destroyAllWindows()
