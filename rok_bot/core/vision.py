import cv2
import numpy as np
from PIL import Image

class Vision:
    def __init__(self):
        pass

    def _pil_to_bgr(self, screenshot):
        """Convert a PIL Image to BGR ndarray for OpenCV."""
        if screenshot is None:
            return None
        arr = np.asarray(screenshot)
        if arr.size == 0:
            return None
        if arr.ndim == 2:
            return cv2.cvtColor(arr, cv2.COLOR_GRAY2BGR)
        if arr.shape[2] == 4:
            return cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)
        return cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)

    def find_template(self, screenshot, template_path, threshold=0.8):
        """
        Finds a template in a screenshot.
        :param screenshot: PIL Image object
        :param template_path: Path to the template image
        :param threshold: Matching threshold
        :return: (x, y) coordinates of the match center, or None
        """
        screen_cv = self._pil_to_bgr(screenshot)
        if screen_cv is None:
            return None
        template = cv2.imread(template_path)
        
        if template is None:
            print(f"Error: Template not found at {template_path}")
            return None

        h, w = template.shape[:2]
        sh, sw = screen_cv.shape[:2]
        if h > sh or w > sw:
            return None
        res = cv2.matchTemplate(screen_cv, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val >= threshold:
            # Return center coordinates
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2
            return (center_x, center_y)
        
        return None

    def find_multiple_templates(self, screenshot, template_path, threshold=0.8):
        """
        Finds all occurrences of a template.
        """
        screen_cv = self._pil_to_bgr(screenshot)
        if screen_cv is None:
            return []
        template = cv2.imread(template_path)
        
        if template is None:
            return []

        h, w = template.shape[:2]
        sh, sw = screen_cv.shape[:2]
        if h > sh or w > sw:
            return []
        res = cv2.matchTemplate(screen_cv, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        
        points = []
        for pt in zip(*loc[::-1]):
            points.append((pt[0] + w // 2, pt[1] + h // 2))
        
        # Deduplicate points that are too close
        return self.deduplicate_points(points)

    def deduplicate_points(self, points, distance=20):
        if not points:
            return []
        
        unique_points = [points[0]]
        for p in points[1:]:
            is_new = True
            for up in unique_points:
                if np.sqrt((p[0]-up[0])**2 + (p[1]-up[1])**2) < distance:
                    is_new = False
                    break
            if is_new:
                unique_points.append(p)
        return unique_points
