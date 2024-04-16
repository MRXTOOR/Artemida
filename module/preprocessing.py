import cv2

class Preprocessor:
    @staticmethod
    def preprocess_image(img):
        print("Image shape:", img.shape)
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        if not (hsv_img[:, :, 1] > 0).any():
            raise ValueError("Input image is grayscale. Please provide a color image.")
        return img
