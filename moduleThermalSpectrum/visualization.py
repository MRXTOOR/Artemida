import cv2


class Visualizer:
    @staticmethod
    def visualize_images(original_image, processed_image):
        cv2.imshow("The original image", original_image)
        cv2.imshow("The analyzed image", processed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
