import json

class Map_Ingester():
    
    instructions = ""
    
    
    def __init__(self, path="./data/tilesets/ingest_list.json") -> None:
        self.path = path
        self._ingest_list()
        pass
    
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
        
    
    