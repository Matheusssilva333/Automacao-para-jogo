import time
import random

class GatheringTask:
    def __init__(self, bot):
        self.bot = bot
        # Tab assets: tabs/rss_<name>.png (see assets/README_ASSETS.md)
        self.rss_types = ["food", "wood", "stone", "gold"]

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
        if not self.bot.click_image("buttons/march_list"):
            return False
            
        # 2. Find a gathering march and Click 'Return'
        if self.bot.click_image("buttons/recall_gathering"):
            print("Successfully recalled a gathering march.")
            return True
        
        return False

    def send_to_gather(self):
        print("Searching for resource node...")
        # 1. Open search menu
        if not self.bot.click_image("buttons/search"):
            return False
            
        # 2. Select resource type (randomly or based on priority)
        rss_to_find = random.choice(self.rss_types)
        if not self.bot.click_image(f"tabs/rss_{rss_to_find}"):
            # Fallback to food if specific one fails
            self.bot.click_image("tabs/rss_food")
            
        # 3. Search and click result
        self.bot.click_image("buttons/search_confirm")
        time.sleep(2)
        
        # 4. Click the resource node on screen
        if not self.bot.click_image("world/resource_node", threshold=0.7):
            return False
            
        # 5. Click 'Gather'
        if not self.bot.click_image("buttons/gather"):
            return False
            
        # 6. Select march and send
        if self.bot.click_image("buttons/march_confirm", timeout=5):
            print(f"Sent march to gather {rss_to_find}.")
            return True
        
        return False
