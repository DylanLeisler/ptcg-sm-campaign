import json

class Attack(object):


    def __init__(self, attack: dict):

        if not attack == "":
            self.name = attack["name"]
            self.damage = attack["damage"]
            self.itemized_cost = attack["cost"]
            self.total_cost = attack["convertedEnergyCost"]
            self.description = attack["text"]