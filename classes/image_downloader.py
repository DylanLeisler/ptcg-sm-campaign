import os
import urllib.request
from time import sleep
from django.utils.text import slugify
from PIL import Image

default_headers = {'User-Agent': 'PTCG Script'}


class Image_Downloader():
    
    
    def __init__(self, headers=default_headers):
        """This needs to be expanded to take a list

        Args:
            headers (_type_, optional): _description_. Defaults to default_headers.
        """
        self.generic_headers = headers
        
    def download_image(self, url: str, card_set: str, file_name: str, headers="", save_to="./data/images/", overwrite=False) -> int:
        """_summary_

        Args:
            url (str): _description_
            file_name (str): Name of the saved image file. INCLUDE EXT.
            headers (str): _description_. Defaults to self.generic_headers
            save_to (str, optional): Directory to save file. Defaults to "./data/images/".
        """
        res = "small"
        file_dir = save_to + card_set + "/" + res + "/" + file_name
        
        is_remote = self.is_remote(url)
        headers = self.generic_headers if headers == "" else headers
        
        if self.is_existing_file(file_dir) and overwrite == False:
            print("File already exists and overwrite is not enabled.")
            return -1
        if not os.path.exists(save_to + card_set + "/" + res):
            os.makedirs(save_to + card_set + "/" + res)
            print(f"Making dir: {save_to + card_set + '/' + res}")
        
        
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        img = Image.open(response)
        img.save(file_dir, quality="keep")
        
        print(file_dir + " saved!")
        return os.path.getsize(file_dir)
        
    def download_images(self, cards: list, ext=".png"):
        for card in cards:
            url = card.image
            card_set = card.card_id[0:card.card_id.find("-")]
            name = slugify(card.card_id.replace(card_set + "-", "") + "-" + card.name) + ext
            file_size = self.download_image(url, card_set, name)
            sleep_time = file_size / (80000 + (file_size**(1/1.2)))
            sleep(sleep_time.real if sleep_time.real > 0 else 1)
            exit()
        
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