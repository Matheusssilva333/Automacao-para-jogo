class ExplorerTask:
    def __init__(self, bot):
        self.bot = bot

    def run(self):
        self.check_fog()
        self.check_scouts()
        self.check_caves_and_villages()

    def check_fog(self):
        # Find foggy areas and send scouts
        if self.bot.image_exists("ui/scout_idle"):
            if self.bot.click_image("buttons/explore_fog"):
                self.bot.click_image("buttons/send_scout")
                print("Sent scout to explore fog.")

    def check_scouts(self):
        # Check if scouts are idle and send them to explore
        if self.bot.click_image("buttons/scout_camp"):
            if self.bot.click_image("buttons/explore_random"):
                self.bot.click_image("buttons/march_confirm")
                print("Sent scout to explore randomly.")

    def check_caves_and_villages(self):
        # Collect rewards from found caves/villages
        # Look for cave icons on screen
        if self.bot.click_image("world/tribal_village", threshold=0.7):
            self.bot.click_image("buttons/claim_reward")
        elif self.bot.click_image("world/mysterious_cave", threshold=0.7):
            self.bot.click_image("buttons/investigate")
            self.bot.click_image("buttons/send_scout")
