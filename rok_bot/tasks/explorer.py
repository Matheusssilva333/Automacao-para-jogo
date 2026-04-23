class ExplorerTask:
    def __init__(self, bot):
        self.bot = bot

    def run(self):
        self.check_fog()
        self.check_scouts()
        self.check_caves_and_villages()

    def check_fog(self):
        # Find foggy areas and send scouts
        pass

    def check_scouts(self):
        # Check if scouts are idle and send them to explore
        pass

    def check_caves_and_villages(self):
        # Collect rewards from found caves/villages
        pass
