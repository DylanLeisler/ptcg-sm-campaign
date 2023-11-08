import pygame.image, pygame.transform


class Draw_Map():
    
    index_of_tiles = {
    "OBJECTS": ["chair" , "game_table"],
    "WALLS": [
        "side_center", "top_center",
        "bottom_center", "bottom_left", "bottom_right", "bottom_shadow", "bottom_floor", 
        "door_sideways_bottom", "door_sideways", 
        "top_left", "top_right"
        ],
    "FLOORS": ["floor"]
}
    
    PATH_TO_TILESETS = ""
    
    # TILES: {
    #     "LAB": {
    #         "OBJECTS": [],
    #         "WALLS": {
    #             "BOTTOM": {
    #                 "LEFT": [],
    #                 "RIGHT": [],
    #                 "GENERIC": []
    #             },
    #             "TOP": {
    #                 "LEFT": [],
    #                 "RIGHT": []
    #             },
    #             "DOORWAY": {
    #                 "SIDEWAYS": [],
    #                 "FORWARD": []
    #             },
    #             "GENERIC": {
    #                 "WALL": []
    #             }
    #         },
    #         "FLOOR": {}
    #     }
    # }
    
    TILES = {}
    
    def __init__(self, PATH_TO_TILESETS="./data/tilesets/16x16"):
        self.PATH_TO_TILESETS = PATH_TO_TILESETS
        
    def draw(self):
        pass
    
    def load_tile(self, location: str, component: str, tile_name: str):
        path = self.PATH_TO_TILESETS + "/" + location.upper() + "/" + component.upper() + "/" + tile_name
        path = path if path.endswith(".png") else path + ".png"
        return pygame.image.load(path).convert_alpha()
    
    def load_tiles_by_location(self, location: str):
        indexes = {}
        for key in self.index_of_tiles.keys():
            for tile in self.index_of_tiles[key]:
                if not indexes.get(key):
                    indexes[key] = {}
                indexes[key][tile] = pygame.transform.scale_by(self.load_tile(location, key, tile), 4)
        self.TILES = indexes
        


        
        
