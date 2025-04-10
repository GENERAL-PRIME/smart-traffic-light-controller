# 🧠 Smart Traffic Controller 🚦

An intelligent traffic monitoring and light control system using **YOLOv8**, **OpenCV**, and **Python**. It dynamically calculates **vehicle volume**, **turning ratios**, and adjusts **traffic light durations** in real-time. It allows **multiple green lights** simultaneously based on directional vehicle flows.

---

## 📁 Project Structure

```
intelligent_traffic_system/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── camera_processor.py          # Handles vehicle detection from near/far cameras using YOLOv8
│   ├── volume_analyzer.py           # Calculates change in traffic volume
│   ├── turning_ratio.py             # Calculates turning directions from a 360 camera using object tracking
│   ├── intelligent_intersection.py  # Central logic to control traffic light timings
└── utils/
    └── __init__.py
```

---

## 📦 Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**

```
ultralytics>=8.0.0
opencv-python
numpy
```

---

## 🧠 Key Features

- ✅ Uses YOLOv8 to detect and track vehicles
- ✅ Real-time turning ratio detection using 360 camera
- ✅ Detects increasing/decreasing vehicle volume
- ✅ Adjusts signal durations dynamically based on actual traffic
- ✅ Supports multiple green lights when turning flows allow it

---

## 🖼️ Camera Setup

- Each lane (North, East, South, West) has:
  - One camera near the intersection
  - One camera 100m behind it
- A 360-degree camera at the center of the intersection detects vehicle turning patterns

Replace `assets/*.mp4` with RTSP streams or real-time camera feeds as needed.

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📸 Sample Inputs

- Place video files or use live camera feeds:
  - `assets/north_near.mp4`, `assets/north_far.mp4`
  - `assets/east_near.mp4`, `assets/east_far.mp4`
  - `assets/south_near.mp4`, `assets/south_far.mp4`
  - `assets/west_near.mp4`, `assets/west_far.mp4`

---

## ⚙️ What Happens in Each Cycle

1. Each direction's near and far cameras process frames and detect vehicle counts.
2. The volume analyzer calculates the change in traffic volume.
3. The 360 camera identifies turning directions between lanes.
4. Green light durations are dynamically determined based on both metrics.
5. Multiple green lights may be given simultaneously if turning flows don't conflict.

---

## 📌 Future Improvements

- Real-time dashboard for visualization
- Export logs to CSV or database
- Integrate with smart traffic lights hardware
- Emergency vehicle prioritization and override logic

---

## 🧠 Credits

- **YOLOv8** by [Ultralytics](https://github.com/ultralytics/ultralytics)
- Built with ❤️ using Python + OpenCV
