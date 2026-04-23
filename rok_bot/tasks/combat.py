import time

class CombatTask:
    def __init__(self, bot):
        self.bot = bot

    def run(self):
        """
        Main loop for Barbarian Forts.
        """
        if self.bot.ap < 140: # Cost of a rally usually
            # Check if we should recall a march or use it for gathering
            return

        print("Checking for Barbarian Fort rallies...")
        if self.should_start_rally():
            self.start_fort_rally()
        elif self.should_join_rally():
            self.join_fort_rally()

    def should_start_rally(self):
        # Logic to check if we have enough AP and a free march
        return self.bot.ap >= 140 and self.bot.get_idle_march_count() > 0

    def start_fort_rally(self):
        print("Starting a new Barbarian Fort rally...")
        # 1. Open search menu
        if not self.bot.click_image("buttons/search"):
            return False
        
        # 2. Select Fort tab
        if not self.bot.click_image("tabs/barbarian_fort"):
            return False
            
        # 3. Search and click 'Search' button
        self.bot.click_image("buttons/search_confirm")
        time.sleep(2)
        
        # 4. Click the Fort on screen
        if not self.bot.click_image("world/barbarian_fort", threshold=0.7):
            return False
            
        # 5. Click Attack/Rally
        if not self.bot.click_image("buttons/rally"):
            return False
            
        # 6. Choose time (e.g. 5 min)
        self.bot.click_image("buttons/rally_5min")
        
        # 7. Send march
        if self.bot.click_image("buttons/march_confirm", timeout=5):
            print("Rally started successfully.")
            return True
        
        return False

    def join_fort_rally(self):
        print("Joining an existing rally...")
        # 1. Open Alliance menu
        if not self.bot.click_image("buttons/alliance"):
            return False
            
        # 2. Open War tab
        if not self.bot.click_image("buttons/alliance_war", timeout=2):
            return False
            
        # 3. Find and click 'Join' on available rally
        if self.bot.click_image("buttons/join_rally", threshold=0.8):
            time.sleep(1)
            # 4. Confirm march
            if self.bot.click_image("buttons/march_confirm", timeout=5):
                print("Joined rally successfully.")
                return True
        
        # Close menu if no rally found
        self.bot.adb.tap(50, 50) # Click outside
        return False
