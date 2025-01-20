# 👤 Face Recognition System for Attendance 📊

## Overview
This **Face Recognition System** is built using Python and the **LBPHFaceRecognizer** (Local Binary Patterns Histogram) to automate attendance management. It is designed to recognize individuals accurately and efficiently, making manual attendance processes obsolete. 🏢🕒

---

## Key Features
- **Face Detection**: Identifies faces in real-time using OpenCV. 🔍  
- **Face Recognition**: Matches detected faces with the database using LBPHFaceRecognizer. 🔒  
- **Attendance Logging**: Automatically marks attendance in a CSV file. ✅  
- **User-Friendly Interface**: Simple and intuitive interface for managing face data. 🔄  

---

## 🛠️ System Architecture
1. **Face Detection**: Utilizes Haar cascades from OpenCV for real-time face detection.
2. **Face Recognition**: Trains a recognizer using LBPH to identify individuals from pre-labeled data.
3. **Attendance Management**: Logs the attendance of recognized individuals with a timestamp in a CSV file.
4. **Database**: Stores face data (images) for training and recognition.

---

## 🚀 Installation

### Prerequisites
- Python 3.7+
- OpenCV 4.5+
- NumPy
- Pandas

---

## 🔧 Usage
1. **Adding New Faces**:
   - Run `AI PROJECT.py` to capture and label new images.
   

2. **Real-Time Attendance**:
   - Recognized individuals will be logged in `attendance.csv`.

---

## ⚙️ Customization
- **Thresholds**: Adjust confidence thresholds for recognition.
- **Camera Source**: Modify the camera index for external cameras.
- **CSV File**: Change the output file name or location.

---

## 📊 Results
- Achieved **high accuracy** in face recognition under varied lighting conditions.
- Successfully logged attendance for multiple individuals in real-time. 🚀

---

## 🛡️ Security and Privacy
The system stores only the features (histograms) extracted from face images, ensuring user privacy. Raw images can be removed post-training. 🔒

---

## 💬 Feedback
Feel free to report issues or suggest features by creating a GitHub issue. Contributions are welcome! 🛠️

---

## 🏆 Credits
- **Face Recognition**: LBPHFaceRecognizer (OpenCV)
- **Frameworks**: OpenCV, Pandas, NumPy
