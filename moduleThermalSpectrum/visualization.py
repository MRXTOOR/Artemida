import cv2


class Visualizer:
    @staticmethod
    def visualize_images(original_image, processed_image):
        cv2.imshow("Оригинальное изображение", original_image)
        cv2.imshow("Проанализированное изображение", processed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
