import cv2


class HeatmapVisualizer:
    @staticmethod
    def visualize_heatmap(depth_map):
        normalized_depth_map = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX)
        heatmap = cv2.applyColorMap(normalized_depth_map, cv2.COLORMAP_JET)
        return heatmap
