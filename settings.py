class Settings():
    
    def __init__(self):
        self.window_width = 1000
        self.window_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3

        #Bullets settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Alien settings
        self.fleet_drop_speed = 20
        self.aliens_points = 50
   
        #Level speed
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.aliens_points = int(self.aliens_points * self.score_scale)
