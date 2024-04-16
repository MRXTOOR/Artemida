import os
import cv2

def preprocess_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    print("Image shape:", img.shape)

    # Convert to HSV color space
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Check if the image is grayscale (saturation channel all zeros)
    if not (hsv_img[:, :, 1] > 0).any():
        raise ValueError("Input image is grayscale. Please provide a color image.")

    return img


def estimate_depth(image):
    # Example: using the Sobel algorithm for depth estimation
    depth_map = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    depth_map = cv2.convertScaleAbs(depth_map)
    return depth_map


def integrate_depth_and_spectral(image, depth_map):
    # Example: simple combination of image and depth map
    combined_image = cv2.addWeighted(image, 0.5, depth_map, 0.5, 0)
    return combined_image


def detect_minerals(image):
    # Convert the image to grayscale (single-channel image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect contours on the single-channel image
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw bounding boxes around detected contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image


def visualize_images(original_image, processed_image):
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Processed Image", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # Step 1: Image preprocessing
    image_folder = "images-test"
    image_files = os.listdir(image_folder)
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        try:
            processed_image = preprocess_image(image_path)
        except ValueError as e:
            print(f"Error processing image '{image_file}': {e}")
            continue

        # Step 2: Depth estimation for the image
        depth_map = estimate_depth(processed_image)

        # Step 3: Integration of depth and spectral information
        combined_image = integrate_depth_and_spectral(processed_image, depth_map)

        # Step 4: Mineral detection and bounding box
        image_with_minerals = detect_minerals(combined_image)

        # Step 5: Output and visualization
        visualize_images(processed_image, image_with_minerals)


if __name__ == "__main__":
    main()
