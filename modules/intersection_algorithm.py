from modules.volume_analyzer import VolumeAnalyzer

class IntersectionAlgorithm:
    def __init__(self, camera_processors, turning_ratio_calculator):
        self.cams = camera_processors
        self.turning_ratio_calculator = turning_ratio_calculator
        self.volume_analyzer = VolumeAnalyzer()
        self.min_green = 10
        self.max_green = 60

    def run_cycle(self):
        traffic_info = {}

        for dir, cam in self.cams.items():
            cam.process_frame()
            near, far = cam.get_counts()
            volume = self.volume_analyzer.calculate_volume_change(near, far)
            turns = self.turning_ratio_calculator.get_turns_from(dir)
            traffic_info[dir] = {"volume": volume, "turns": turns}

        print("\n>>> INTERSECTION STATUS <<<")
        for dir, data in traffic_info.items():
            turns = sum(data["turns"].values())
            time = min(max(data["volume"] * 2 + turns * 1.5, self.min_green), self.max_green)
            if data["volume"] > 0:
                print(f"{dir}: Volume={data['volume']}, Turns={data['turns']}, Green Light Time={time:.1f}s")
                self.cams[dir].clear_counts()
