import pyfiglet

from moduleThermalSpectrum.annatationVSLS import AnnotationVisualizer
from moduleThermalSpectrum.depth_estimation import DepthEstimator
from moduleThermalSpectrum.heatmap_visualization import HeatmapVisualizer
from moduleThermalSpectrum.preprocessing import Preprocessor
from moduleThermalSpectrum.visualization import Visualizer


#from moduleThermalSpectrum.preprocessing import Preprocessor
#from moduleThermalSpectrum.depth_estimation import DepthEstimator
#from moduleThermalSpectrum.heatmap_visualization import HeatmapVisualizer
#from moduleThermalSpectrum.annatationVSLS import AnnotationVisualizer
#from moduleThermalSpectrum.visualization import Visualizer


def main():
    ascii_art = pyfiglet.figlet_format("Artemida")
    print(ascii_art)


if __name__ == "__main__":
    main()


def analyze_selected_image(image):
    try:
        processed_image = Preprocessor.preprocess_image(image)
    except ValueError as e:
        print(f"Ошибка обработки изображения: {e}")
        return

    depth_map = DepthEstimator.estimate_depth(processed_image)
    heatmap_image = HeatmapVisualizer.visualize_heatmap(depth_map)
    annotated_image = AnnotationVisualizer.annotate_regions(heatmap_image)
    Visualizer.visualize_images(processed_image, annotated_image)
