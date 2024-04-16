import os

from Artemida.module.preprocessing import Preprocessor
from Artemida.module.depth_estimation import DepthEstimator
from Artemida.module.integration import Integrator
from Artemida.module.mineral_detection import MineralDetector
from Artemida.module.visualization import Visualizer

def main():
    image_folder = "images-test"
    image_files = os.listdir(image_folder)

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        try:
            processed_image = Preprocessor.preprocess_image(image_path)
        except ValueError as e:
            print(f"Error processing image '{image_file}': {e}")
            continue

        depth_map = DepthEstimator.estimate_depth(processed_image)
        combined_image = Integrator.integrate_depth_and_spectral(processed_image, depth_map)
        image_with_minerals = MineralDetector.detect_minerals(combined_image)
        Visualizer.visualize_images(processed_image, image_with_minerals)

if __name__ == "__main__":
    main()
