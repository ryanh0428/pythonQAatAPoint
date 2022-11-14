from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from royale.models.card import Card


class Cards_Detail_Page():
    def __init__(self,driver):
        self.map = CardsDetailMap(driver)

    def get_name_text(self):
        return self.map.get_name.text

    def get_rarity_text(self):
        return self.map.get_rarity()

    def get_arena_text(self):
        return self.map.get_arena()

    def get_type_text(self):
        return self.map.get_type()

    def get_base_card(self)->Card:
        type_and_arena = self.get_card_type_and_arena()
        return Card(
            name = self.map.get_name.text,
            type = type_and_arena[0],
            arena= type_and_arena[1],
            rarity = self.map.get_rarity().text.split('\n')[-1]

        )

    def get_card_type_and_arena(self)->tuple[str, int]:
        type_and_arena = self.map.card_category().text.split(', ')
        card_type=type_and_arena[0]
        card_arena = int(type_and_arena[1].split()[-1])
        return card_type, card_arena
class CardsDetailMap():
    def __init__(self,driver):
        self._driver = driver

    @property
    def get_name(self)->WebElement:
        return self._driver.find_element(By.CLASS_NAME,"card__cardName")

    def get_rarity(self)->WebElement:
        return self._driver.find_element(By.CSS_SELECTOR,"[class*='rarityCaption']")

    def card_category(self):
        return self._driver.find_element(By.CLASS_NAME, "card__rarity")

    def get_type(self)->WebElement:
        return self._driver.find_element(By.CLASS_NAME, "card__rarity").text.split(", ")[0]

    def get_arena(self)->WebElement:
        return self._driver.find_element(By.CLASS_NAME, "card__rarity").text.split(", ")[1]