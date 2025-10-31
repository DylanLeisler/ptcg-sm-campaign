from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT
from .character import Character
from game_config import GameConfig as GC


class Player(Character):
    
    STARTING_POSITION = GC.PLAYER_STARTING_POSITION
    DISTANCE_PER_FRAME = GC.DEFAULT_MOVEMENT_DISTANCE_PER_FRAME
    
    def __init__(self, sprite, name, starting_position=STARTING_POSITION):
        super().__init__(sprite, name)
        self.position = starting_position

    # backward goes left and right goes down
    # dist is distance moved per frame
    def move(self, key, dt, groups, dist=None):
        if dist is None:
            dist = self.DISTANCE_PER_FRAME
            
        key_map = {
            K_DOWN: {
                "dv": (0, dist),
                "sprite_direction": "forward"},
            K_UP: {
                "dv": (0, -dist),
                "sprite_direction": "backward"},
            K_RIGHT: {
                "dv": (dist, 0),
                "sprite_direction": "right"},
            K_LEFT: {
                "dv": (-dist, 0),
                "sprite_direction": "left"},
        }
        self.direction = key_map[key]["sprite_direction"]
        dx, dy = key_map[key]["dv"]
            
        if self.will_collide(dx, dy, groups):
            self.update(dt, reset_frame=True)
            return False  
        print(dx, dy)
        self.position = (self.position[0] + dx, self.position[1] + dy)
        self.update(dt)
        return True