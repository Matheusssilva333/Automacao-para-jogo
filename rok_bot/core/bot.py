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

    def get_idle_march_count(self):
        # OCR/Vision logic to read march status
        return 5 # Placeholder

    def is_fort_rally_active(self):
        """
        Returns True if the bot has an active rally in progress.
        """
        # Logic to check Alliance -> War or march list
        return False

    def update_stats(self):
        # Update AP and other stats from screen
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
                time.sleep(10)
            except Exception as e:
                print(f"Error in main loop: {e}")
                time.sleep(5)

if __name__ == "__main__":
    bot = RoKBot()
    bot.start()
