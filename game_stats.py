class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_status()
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.level = 1

    def reset_status(self):
        self.ships_left = self.ai_settings.ship_limit
