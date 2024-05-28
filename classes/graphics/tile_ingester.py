import json
import pygame.transform, pygame.image

class Tile_Ingester():
    """
    Pulls json from from path during init to load Map_Ingester.instructions
    Call build_index to pull tiles specified in instructions to self.index
    """
    
    instructions = None
     
     
    def __init__(self, scale=4, path="./data/tilesets/ingest_list.json") -> None:
        self.path = path
        self._ingest_instructions()
        self.scale = scale
    
    def _ingest_instructions(self) -> None:
        """Uses self.path to find and load them to self.instructions
        """
        try:
            with open(self.path, 'r') as instructions:
                self.instructions = json.load(instructions)
                
        except FileNotFoundError:
            print(f"The file {self.path} does not exist.")
        except json.JSONDecodeError:
            print(f"File {self.path} is not valid JSON.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def build_index(self) -> 'Tile_Ingester':
        """Uses self.instructions to create index of tile properties/specs for each location/directory and
        stores it in self.index. Also appends file path and pygame image object to each tile spec.
        """
        self.index = {}
        # An example of an area would be 'lab'
        for area in self.instructions["LOCATIONS"].keys():
            
            # Make index["LAB"] = {'LAB': {'TILES':[...],[...]}}
            # Omits LOCATIONS key from index
            self.index[area] = self.instructions["LOCATIONS"][area]
            
            for name,tile_spec in self.index[area]["TILES"].items():
                path = f"./data/tilesets/16x16/{area}/{name}{tile_spec['EXT']}"
                self.index[area]["TILES"][name]["PATH"] = path
                self.index[area]["TILES"][name]["TILEMAP"] = pygame.transform.scale_by(
                    pygame.image.load(path).convert_alpha(), 
                    self.scale
                )
        return self
    
    def _isIndex(self, no_build=False) -> None:
        """Checks for the existence of self.index. Attemps to build if not found.
        Make into decorator if this sees a lot of usage
        
        Args:
            no_build (bool, optional): Prevents build from being attempted if index isn't found. Defaults to False.

        Returns:
            _type_: 
        """
        if not hasattr(self, 'index'):
            print("NO INDEX FOUND.")
            if no_build:
                print("TODO: Throw error")
            else:
                print("Attempting build_index....")
                self.build_index()
    
    def get_index(self) -> dict:
        """Returns self.index if it is found.

        Returns:
            _type_: Dict{}
        """
        self._isIndex()
        return self.index
    
    def print_index(self) -> 'Tile_Ingester':
        """Prints self.index to the console if it is found.
        """
        self._isIndex()
            
        for area in self.index:
            print("")
            for tile in self.index[area]["TILES"]:
                print(f"\t{area}.{tile}")
        
        return self
    
                
        
    
    