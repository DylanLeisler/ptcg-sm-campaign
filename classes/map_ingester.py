import json
import pygame.transform, pygame.image

class Map_Ingester():
    
    instructions = ""
    
    
    def __init__(self, scale=4, path="./data/tilesets/ingest_list.json") -> None:
        self.path = path
        self._ingest_list()
        self.scale = scale
    
    def _ingest_list(self):
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
        for targ in self.instructions["TARGETS"].keys():
            self.index[targ] = self.instructions["TARGETS"][targ]
            for comp in self.index[targ]:
                for comp_index,tile_spec in enumerate(self.index[targ][comp]):
                    path = f"./data/tilesets/16x16/{targ}/{comp}/{tile_spec['NAME']}{tile_spec['EXT']}"
                    self.index[targ][comp][comp_index]["PATH"] = path
                    self.index[targ][comp][comp_index]["TILEMAP"] = pygame.transform.scale_by(
                        pygame.image.load(path).convert_alpha(), 
                        self.scale
                    )
                
        
    
    