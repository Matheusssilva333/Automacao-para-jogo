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
        # 1. Click City Hall or Items
        # 2. Find and use 8h/24h shield
        pass

    def train_troops(self):
        # Check barracks, stables, etc.
        pass

    def upgrade_buildings(self):
        # Check if building queue is free
        pass
