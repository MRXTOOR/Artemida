import cv2

class Visualizer:
    @staticmethod
    def visualize_images(original_image, processed_image):
        cv2.imshow("Original Image", original_image)
        cv2.imshow("Processed Image", processed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class HeatmapVisualizer:
    pass


class AnnotationVisualizer:
    pass