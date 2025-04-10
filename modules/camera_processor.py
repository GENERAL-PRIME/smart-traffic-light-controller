from ultralytics import YOLO
import cv2

class TrafficCamera:
    def __init__(self, near_cam_src, far_cam_src):
        self.near_cap = cv2.VideoCapture(near_cam_src)
        self.far_cap = cv2.VideoCapture(far_cam_src)
        self.model = YOLO("yolov8n.pt")
        self.vehicle_classes = [2, 3, 5, 7]
        self.near_count = 0
        self.far_count = 0

    def _process_frame(self, frame):
        results = self.model.track(frame, persist=True)[0]
        return sum(int(box.cls) in self.vehicle_classes for box in results.boxes)

    def process_frame(self):
        ret_near, near_frame = self.near_cap.read()
        ret_far, far_frame = self.far_cap.read()

        if ret_near:
            self.near_count = self._process_frame(near_frame)
        if ret_far:
            self.far_count = self._process_frame(far_frame)

    def get_counts(self):
        return self.near_count, self.far_count

    def clear_counts(self):
        self.near_count = 0
        self.far_count = 0
