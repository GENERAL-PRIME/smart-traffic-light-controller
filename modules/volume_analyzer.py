class VolumeAnalyzer:
    def compare_counts(self, near_count, far_count):
        diff = near_count - far_count
        if diff > 5:
            return "Increasing"
        elif diff < -5:
            return "Decreasing"
        else:
            return "Stable"
    def calculate_volume_change(self, near_count, far_count):
        return max(near_count - far_count, 0)

