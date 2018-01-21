class Settings():
# A class to store all settings for alien invasion.

    def __init__(self):
        # screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 7.5

        # bullet settings
        self.bullet_speed_factor = 7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3