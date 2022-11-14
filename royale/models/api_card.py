from royale.models.card import Card


class Api_card(Card):
    def __init__(self, hash:str,id:int,icon:str,cost:int, name:str, type:str, arena:int, rarity:str):
        super().__init__(name, type, arena, rarity)
        self.id = id
        self.hash = hash
        self.icon = icon
        self.cost = cost
