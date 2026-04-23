class CityMgmtTask:
    def __init__(self, bot):
        self.bot = bot

    def run(self):
        self.check_shield()
        self.train_troops()
        self.upgrade_buildings()

    def check_shield(self):
        """
        Critical: Detect incoming attack (red screen) and apply shield.
        """
        if self.bot.vision.find_template(self.bot.get_screenshot(), "assets/red_screen_indicator.png"):
            print("ALERT: City under attack! Applying Peace Shield...")
            self.apply_shield()

    def apply_shield(self):
        # 1. Open Items menu
        if not self.bot.click_image("buttons/items"):
            return False
            
        # 2. Go to 'Others' or 'Buffs' tab
        self.bot.click_image("tabs/items_buffs")
        
        # 3. Find and use 8h Peace Shield
        if self.bot.click_image("items/peace_shield_8h"):
            self.bot.click_image("buttons/use_item")
            print("Peace Shield applied!")
            return True
        return False

    def train_troops(self):
        # Check barracks, stables, archery, etc.
        buildings = ["barracks", "stables", "archery_range", "siege_workshop"]
        for building in buildings:
            if self.bot.click_image(f"buildings/{building}_icon"):
                # Click 'Train' button
                if self.bot.click_image("buttons/train"):
                    # Select max and confirm
                    self.bot.click_image("buttons/train_confirm")
                    print(f"Started training in {building}.")

    def upgrade_buildings(self):
        # Check if building queue is free
        if self.bot.image_exists("ui/builder_idle"):
            # Click an upgradeable building (indicated by a green arrow)
            if self.bot.click_image("ui/upgrade_arrow"):
                if self.bot.click_image("buttons/upgrade"):
                    self.bot.click_image("buttons/upgrade_confirm")
                    print("Started building upgrade.")
