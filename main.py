from modules.camera_processor import TrafficCamera
from modules.turning_ratio import TurningRatioCalculator
from modules.intersection_algorithm import IntersectionAlgorithm
import cv2

if __name__ == "__main__":
    dummy_frame = cv2.imread("assets/dummy.jpg")

    turning_ratio_calculator = TurningRatioCalculator(frame_shape=dummy_frame.shape)

    camera_processors = {
        'N': TrafficCamera('assets/north_near.mp4', 'assets/north_far.mp4'),
        'E': TrafficCamera('assets/east_near.mp4', 'assets/east_far.mp4'),
        'S': TrafficCamera('assets/south_near.mp4', 'assets/south_far.mp4'),
        'W': TrafficCamera('assets/west_near.mp4', 'assets/west_far.mp4'),
    }

    intersection = IntersectionAlgorithm(camera_processors, turning_ratio_calculator)

    while True:
        intersection.run_cycle()
