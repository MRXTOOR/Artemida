import cv2

class DepthEstimator:
    @staticmethod
    def estimate_depth(image):
        depth_map = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        depth_map = cv2.convertScaleAbs(depth_map)
        return depth_map