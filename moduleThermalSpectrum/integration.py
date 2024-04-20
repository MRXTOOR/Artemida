import cv2


class Integrator:
    @staticmethod
    def integrate_depth_and_spectral(image, depth_map):
        combined_image = cv2.addWeighted(image, 0.5, depth_map, 0.5, 0)
        return combined_image
