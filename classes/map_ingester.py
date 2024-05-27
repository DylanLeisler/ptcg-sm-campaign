import json
import pygame.transform, pygame.image

class Map_Ingester():
    """
    Pulls json from from path during init to load Map_Ingester.instructions
    Call build_index to pull tiles specified in instructions to self.index
    """
    
    instructions = None
     
     
    def __init__(self, scale=4, path="./data/tilesets/ingest_list.json") -> None:
        self.path = path
        self._ingest_instructions()
        self.scale = scale
    
    def _ingest_instructions(self):
        try:
            with open(self.path, 'r') as instructions:
                self.instructions = json.load(instructions)
                
        except FileNotFoundError:
            print(f"The file {self.path} does not exist.")
        except json.JSONDecodeError:
            print(f"File {self.path} is not valid JSON.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def build_index(self):
        self.index = {}
        # An example of an area would be 'lab'
        for area in self.instructions["LOCATIONS"].keys():
            self.index[area] = self.instructions["LOCATIONS"][area]
            for tile_group in self.index[area]:
                for tile,tile_spec in enumerate(self.index[area][tile_group]):
                    path = f"./data/tilesets/16x16/{area}/{tile_group}/{tile_spec['NAME']}{tile_spec['EXT']}"
                    self.index[area][tile_group][tile]["PATH"] = path
                    self.index[area][tile_group][tile]["TILEMAP"] = pygame.transform.scale_by(
                        pygame.image.load(path).convert_alpha(), 
                        self.scale
                    )
                
        
    
    