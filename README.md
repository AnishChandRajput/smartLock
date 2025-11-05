# 🔒 SmartLock AI

**SmartLock AI** is an intelligent facial recognition–based security system that automatically locks or unlocks your computer based on user presence.  
It uses **Python**, **OpenCV**, and **DeepFace** to detect faces in real time, enhancing both security and convenience.

---

## 🚀 Features

- 👁️ **Real-Time Face Detection** — Uses your webcam to continuously monitor the user.
- 🤖 **AI-Based Verification** — Detects and verifies the authorized user using DeepFace.
- 🔐 **Auto Lock Mechanism** — Automatically locks the screen when the user is not detected.
- 🔊 **Audio Alert System** — Beeps or triggers alerts if an unauthorized face appears.
- ⚙️ **Customizable Settings** — Configure check intervals, lock delays, and more.

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|----------------|
| Programming Language | Python |
| Libraries | OpenCV, DeepFace, time, os, winsound |
| Platform | Windows |
| IDE | PyCharm |

---

## 🧠 How It Works

1. The program loads a reference image (`anish.jpg`) of the authorized user.  
2. It continuously captures webcam frames.  
3. If the detected face matches the stored reference:
   - The system stays **unlocked**.  
4. If the face is not detected or mismatched:
   - A countdown starts.  
   - After a short delay, the system **locks automatically**.

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AnishChandRajput/smartLock.git
