import time
import random

class GatheringTask:
    def __init__(self, bot):
        self.bot = bot
        self.rss_types = ["food", "wood", "stone", "gold", "gems"]

    def run(self):
        """
        Main loop for gathering.
        Check idle marches and send them to gather.
        """
        self.check_for_recall()
        
        idle_marches = self.bot.get_idle_march_count()
        if idle_marches <= 0:
            return

        # Special case for the reserved fort march
        # If AP is low, use all marches for gathering
        # If AP > 30, keep at least 1 march free (unless it's already busy with a rally)
        if self.bot.ap >= 30 and idle_marches == 1:
            if not self.bot.is_fort_rally_active():
                print("Keeping 1 march for Fort Rallies.")
                return

        print(f"Sending {idle_marches} marches to gather...")
        for _ in range(idle_marches):
            self.send_to_gather()
            time.sleep(random.uniform(2, 5))

    def check_for_recall(self):
        """
        If AP is high and we don't have a free march for forts, recall the closest gathering march.
        """
        if self.bot.ap >= 140 and self.bot.get_idle_march_count() == 0:
            if not self.bot.is_fort_rally_active():
                print("AP is high. Recalling a march for Fort Rallies...")
                self.recall_gathering_march()

    def recall_gathering_march(self):
        # 1. Open March List
        # 2. Find a gathering march
        # 3. Click 'Return'
        pass

    def send_to_gather(self):
        # 1. Open search menu
        # 2. Select resource type
        # 3. Search and click result
        # 4. Click 'Gather'
        # 5. Select march and send
        print("Searching for resource node...")
        # Placeholder for vision-based interaction
        pass
