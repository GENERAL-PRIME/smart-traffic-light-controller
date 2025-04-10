from ultralytics import YOLO
import numpy as np
import cv2

class TurningRatioCalculator:
    def __init__(self, frame_shape):
        self.model = YOLO("yolov8n.pt")
        self.h, self.w = frame_shape[:2]
        self.track_history = {}
        self.entry_exit_recorded = {}
        self.turn_matrix = {
            'N': {'E': 0, 'S': 0, 'W': 0},
            'E': {'N': 0, 'S': 0, 'W': 0},
            'S': {'N': 0, 'E': 0, 'W': 0},
            'W': {'N': 0, 'E': 0, 'S': 0}
        }
        self.zones = self._define_zones()

    def _define_zones(self):
        return {
            'N': np.array([[0, 0], [self.w, 0], [self.w, self.h//3], [0, self.h//3]]),
            'S': np.array([[0, self.h*2//3], [self.w, self.h*2//3], [self.w, self.h], [0, self.h]]),
            'E': np.array([[self.w*2//3, 0], [self.w, 0], [self.w, self.h], [self.w*2//3, self.h]]),
            'W': np.array([[0, 0], [self.w//3, 0], [self.w//3, self.h], [0, self.h]])
        }

    def _point_to_zone(self, x, y):
        for direction, poly in self.zones.items():
            if cv2.pointPolygonTest(poly, (x, y), False) >= 0:
                return direction
        return None

    def process_frame(self, frame):
        results = self.model.track(frame, persist=True)[0]
        for box in results.boxes:
            if box.id is None:
                continue
            track_id = int(box.id)
            x1, y1, x2, y2 = box.xyxy[0]
            cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)

            if track_id not in self.track_history:
                self.track_history[track_id] = []

            self.track_history[track_id].append((cx, cy))

            if track_id not in self.entry_exit_recorded and len(self.track_history[track_id]) >= 2:
                entry = self._point_to_zone(*self.track_history[track_id][0])
                exit = self._point_to_zone(cx, cy)
                if entry and exit and entry != exit:
                    self.turn_matrix[entry][exit] += 1
                    self.entry_exit_recorded[track_id] = (entry, exit)

    def get_turns_from(self, direction):
        return self.turn_matrix.get(direction, {})
