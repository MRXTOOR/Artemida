import cv2


class Preprocessor:
    @staticmethod
    def preprocess_image(img):
        print("Image shape:", img.shape)
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        if not (hsv_img[:, :, 1] > 0).any():
            raise ValueError(
                "Изображение добавленое вами, является изабраженим в черно - белом цвете, прекрепите в меню фотографию(изображение в любом формате) в меню.")
        return img
