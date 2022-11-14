import requests

from royale.models.api_card import Api_card


def get_all_card() -> list[Api_card]:
    response = requests.get('https://statsroyale.com/api/cards')
    if response.ok:
        return [Api_card(**card) for card in response.json()]

    else:
        raise Exception('Response was not ok. State Code: ' + response.status_code)


def get_card_by_name(card_name:str)->Api_card:
    cards = get_all_card()
    return next(card for card in cards if card.name==card_name)