from core.adb_client import ADBClient
from core.vision import Vision
from tasks.gathering import GatheringTask
from tasks.combat import CombatTask
from tasks.explorer import ExplorerTask
from tasks.city_mgmt import CityMgmtTask
import time

class RoKBot:
    def __init__(self):
        self.adb = ADBClient()
        self.vision = Vision()
        self.ap = 0
        self.max_marches = 5
        self.current_screenshot = None
        
        # Initialize tasks
        self.tasks = [
            CityMgmtTask(self),
            CombatTask(self),
            GatheringTask(self),
            ExplorerTask(self)
        ]

    def get_screenshot(self):
        self.current_screenshot = self.adb.screen_cap()
        return self.current_screenshot

    def click_image(self, template_name, threshold=0.8, timeout=0):
        """
        Tries to find and click an image. If timeout > 0, waits for the image.
        """
        template_path = f"assets/{template_name}.png"
        start_time = time.time()
        
        while True:
            pos = self.vision.find_template(self.get_screenshot(), template_path, threshold)
            if pos:
                self.adb.tap(pos[0], pos[1])
                return True
            
            if time.time() - start_time > timeout:
                break
            time.sleep(0.5)
        
        return False

    def image_exists(self, template_name, threshold=0.8):
        template_path = f"assets/{template_name}.png"
        return self.vision.find_template(self.get_screenshot(), template_path, threshold) is not None

    def get_idle_march_count(self):
        """
        Reads the number of idle marches from the screen.
        """
        # Logic: Look for the march list icon and count the number of 'Idle' statuses
        # For now, we will return a default if we can't find the info
        if self.image_exists("ui/march_idle_icon"):
             # This would ideally be OCR or template counting
             return 1
        return 0

    def is_fort_rally_active(self):
        """
        Returns True if the bot has an active rally in progress.
        """
        # Check if the 'War' icon in Alliance has a notification or if a march is in 'Rally' state
        return self.image_exists("ui/active_rally_icon")

    def update_stats(self):
        """
        Update AP and other stats from screen using OCR.
        """
        # Placeholder for OCR logic to read AP
        # self.ap = self.vision.read_text(region_ap)
        pass

    def start(self):
        print("Starting RoK Bot...")
        while True:
            try:
                self.get_screenshot()
                self.update_stats()
                
                for task in self.tasks:
                    task.run()
                    time.sleep(1)
                
                print("Cycle complete. Sleeping...")
                time.sleep(5)
            except Exception as e:
                print(f"Error in main loop: {e}")
                time.sleep(5)

if __name__ == "__main__":
    bot = RoKBot()
    bot.start()
