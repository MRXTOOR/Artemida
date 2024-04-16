import cv2


class AnnotationVisualizer:
    @staticmethod
    def annotate_regions(image):
        # Sample code for adding text annotation to the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottom_left_corner = (10, 30)
        font_scale = 1
        font_color = (255, 255, 255)
        line_type = 2
        cv2.putText(image, 'Natural Resource Area', bottom_left_corner, font, font_scale, font_color, line_type)
        return image
