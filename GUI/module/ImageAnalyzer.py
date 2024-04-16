import os
import cv2
from Artemida import main

def analyze_image(selected_image):
    selected_image_path = os.path.join("../../images-test", selected_image)
    if not os.path.isfile(selected_image_path):
        print(f"Error: Image file '{selected_image}' not found.")
        return
    try:
        processed_image = cv2.imread(selected_image_path)
        if processed_image is None:
            print(f"Error: Failed to load image '{selected_image}'.")
            return
        main.analyze_selected_image(processed_image)
    except Exception as e:
        print(f"Error analyzing image '{selected_image}': {e}")
