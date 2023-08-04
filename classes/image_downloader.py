import os
import urllib.request
from PIL import Image

default_headers = {'User-Agent': 'PTCG Script'}

URL = "https://images.pokemontcg.io/base1/70.png"


class Image_Downloader():
    
    
    def __init__(self, headers=default_headers):
        """This needs to be expanded to take a list

        Args:
            headers (_type_, optional): _description_. Defaults to default_headers.
        """
        self.generic_headers = headers
        
    def download_image(self, url: str, card_set: str, file_name: str, headers="", save_to="./data/images/", overwrite=False):
        """_summary_

        Args:
            url (str): _description_
            file_name (str): Name of the saved image file. INCLUDE EXT.
            headers (str): _description_. Defaults to self.generic_headers
            save_to (str, optional): Directory to save file. Defaults to "./data/images/".
        """
        file_dir = save_to + card_set + "/" + file_name
        
        is_remote = self.is_remote(url)
        headers = self.generic_headers if headers == "" else headers
        if self.is_existing_file(file_dir) and overwrite == False:
            print("File already exists and overwrite is not enabled.")
            return -1
        
        if not os.path.exists(save_to + card_set):
            os.makedirs(save_to + card_set)
            print(f"Making dir: {save_to + card_set}")
        
        
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        img = Image.open(response)
        img.save(file_dir)
        print(file_dir + " saved!")
        
    def is_remote(self, url: str) -> bool:
        return True if url.startswith("http") else False
    
    def is_existing_file(self, file_dir: str) -> bool:
        return True if os.path.isfile(file_dir) else False
    
    def display_image(self, img: Image):
        img.show()

    
        

# is_secure = True
# SCHEME = "https" if is_secure == True else "http"
# DOMAIN = "images.pokemontcg.io"
# DIR = "base1"
# NAME = "70"
# EXT = "png"
# URL = SCHEME + "://" + "/".join([DOMAIN, DIR, NAME]) + "." + EXT

# DOMAIN = "media.geeksforgeeks.org"
# DIR = "wp-content/uploads/20210224040124"
# NAME = "JSBinCollaborativeJavaScriptDebugging6-300x160"
# EXT = "png"


# img.show()