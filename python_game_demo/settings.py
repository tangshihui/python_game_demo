class Settings():
    """setting"""
    def __init__(self):
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(230,230,230)
        self.ship_speed_factor=1.5
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        #fleet_direction 1:to right -1:to left
        self.fleet_direction=1

        #子弹设置
        self.bullet_speed_factor=3
        self.bullet_width=5
        self.bullet_height=15
        self.bullet_color=255,0,0
        self.bullets_allowed=3