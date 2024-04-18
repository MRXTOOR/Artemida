import cv2
import numpy as np

class AnnotationVisualizer:
    @staticmethod
    def annotate_regions(heatmap_image, depth_threshold=100, min_contour_area=500):
        gray_heatmap = cv2.cvtColor(heatmap_image, cv2.COLOR_BGR2GRAY)

        _, binary_heatmap = cv2.threshold(gray_heatmap, depth_threshold, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(binary_heatmap, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        markers = np.zeros_like(gray_heatmap, dtype=np.int32)

        for i, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > min_contour_area:
                cv2.drawContours(markers, [contour], -1, (i + 1), -1)

        markers = cv2.watershed(heatmap_image, markers)

        red_regions = np.zeros_like(heatmap_image, dtype=np.uint8)
        red_regions[markers == -1] = (0, 0, 255)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > min_contour_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(red_regions, (x, y), (x + w, y + h), (0, 255, 0), 2)

        annotated_image = red_regions.copy()  # Создание копии красных областей

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > min_contour_area:
                x, y, w, h = cv2.boundingRect(contour)
                text_x = x + w // 2 - 50
                text_y = y + h + 30
                cv2.putText(annotated_image, "MATERIAL", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        annotated_image = cv2.addWeighted(heatmap_image, 0.5, annotated_image, 0.5, 0)

        return annotated_image