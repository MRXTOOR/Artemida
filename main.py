# main.py

import os

import pyfiglet

from Artemida.module.preprocessing import Preprocessor
from Artemida.module.depth_estimation import DepthEstimator
from Artemida.module.heatmap_visualization import HeatmapVisualizer
from Artemida.module.annatationVSLS import AnnotationVisualizer
from Artemida.module.visualization import Visualizer


def main():
    ascii_art = pyfiglet.figlet_format("Artemida")
    print(ascii_art)

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
        heatmap_image = HeatmapVisualizer.visualize_heatmap(depth_map)
        annotated_image = AnnotationVisualizer.annotate_regions(heatmap_image)
        Visualizer.visualize_images(processed_image, annotated_image)

if __name__ == "__main__":
    main()