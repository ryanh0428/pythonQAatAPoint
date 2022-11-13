from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


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


class CardsDetailMap():
    def __init__(self,driver):
        self._driver = driver

    @property
    def get_name(self)->WebElement:
        return self._driver.find_element(By.CLASS_NAME,"card__cardName")

    def get_rarity(self)->WebElement:
        return self._driver.find_element(By.CSS_SELECTOR,"[class*='rarityCaption']").text.split('\n')[1]

    def get_type(self)->WebElement:
        return self._driver.find_element(By.CLASS_NAME, "card__rarity").text.split(", ")[0]

    def get_arena(self)->WebElement:
        return self._driver.find_element(By.CLASS_NAME, "card__rarity").text.split(", ")[1]