import cv2
import numpy as np

class AnnotationVisualizer:
    @staticmethod
    def annotate_regions(heatmap_image, depth_threshold=100, min_contour_area=500):
        # Преобразование изображения в оттенки серого
        gray_heatmap = cv2.cvtColor(heatmap_image, cv2.COLOR_BGR2GRAY)

        # Бинаризация изображения с использованием порога
        _, binary_heatmap = cv2.threshold(gray_heatmap, depth_threshold, 255, cv2.THRESH_BINARY)

        # Нахождение контуров на бинарном изображении
        contours, _ = cv2.findContours(binary_heatmap, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Создание маски для водораздела
        markers = np.zeros_like(gray_heatmap, dtype=np.int32)

        # Нумерация областей контуров
        for i, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > min_contour_area:
                cv2.drawContours(markers, [contour], -1, (i + 1), -1)

        # Применение водораздела
        markers = cv2.watershed(heatmap_image, markers)

        # Выделение областей красного цвета
        red_regions = np.zeros_like(heatmap_image, dtype=np.uint8)
        red_regions[markers == -1] = (0, 0, 255)  # Красный цвет для областей с отрицательными маркерами

        # Нахождение ограничивающих прямоугольников для каждой области
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > min_contour_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(red_regions, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Обводим в квадрат

        # Объединение исходного изображения с выделенными областями красного цвета
        annotated_image = cv2.addWeighted(heatmap_image, 0.5, red_regions, 0.5, 0)

        return annotated_image
