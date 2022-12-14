from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from royale.pages.card_details_page import Cards_Detail_Page
from royale.pages.cards_page import CardsPage
from royale.services import card_service

cards = card_service.get_all_card()

@pytest.mark.parametrize('api_card',cards)
def test_card_is_display(api_card):
    driver = webdriver.Chrome()
    #1. go to statsroyale.com
    driver.get("https://statsroyale.com/")
    driver.maximize_window()
    #1.1 click the reject all button in the cookie cosent form
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='SP Consent Message']")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Accept']"))).click()
    #2. click the "Cards" button on the nav bar
    driver.find_element(By.LINK_TEXT,"Cards").click()

    #4. assert the "Phoenix" card was there
    cardsPage = CardsPage(driver)
    card_on_page = cardsPage.get_card_by_name(api_card.name)
    assert card_on_page.is_displayed()

# def test_phoenix_is_a_Legendary():
#     driver = webdriver.Chrome()
#     #1 go to statroyale.com
#     driver.get("https://statsroyale.com/")
#     driver.maximize_window()
#     #1.1 click the reject all button in the cookie consent form
#     WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='SP Consent Message']")))
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"Button[title='Accept']"))).click()
#     #2. click the "Cards" button on the nav bar
#     driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
#     #3. uncheck the Legendary box
#     driver.find_element(By.ID,"legendary-cards").click()
#     assert driver.find_element(By.CSS_SELECTOR,"[href*='Phoenix']").is_displayed() == False


@pytest.mark.parametrize('api_card',cards)
def test_phoenix_detail_is_displayed(api_card):
    driver = webdriver.Chrome()
    #1 go to statroyale.com
    driver.get("https://statsroyale.com/")
    driver.maximize_window()
    #1.1 click the reject all button in the cookie consent form
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='SP Consent Message']")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"Button[title='Accept']"))).click()
    #2. click the "Cards" button on the nav bar
    cards_page = CardsPage(driver)
    # cards_page.goto()
    print("Name : " + api_card.name)
    card_on_page = cards_page.goto().get_card_by_name(api_card.name)
    assert card_on_page.is_displayed()
    #3. click the phoenix card
    card_on_page.click()
    #4. check the card details are displayed
    cardDetailPage = Cards_Detail_Page(driver)
    card = Cards_Detail_Page.get_base_card(cardDetailPage)
    assert card.name == api_card.name
    assert card.arena == api_card.arena
    assert card.rarity == api_card.rarity


# def test_mirror_detail_is_displayed():
#     driver = webdriver.Chrome()
#     #1 go to statroyale.com
#     driver.get("https://statsroyale.com/")
#     driver.maximize_window()
#     #1.1 click the reject all button in the cookie consent form
#     WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='SP Consent Message']")))
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"Button[title='Accept']"))).click()
#     #2. click the "Cards" button on the nav bar
#     cards_page = CardsPage(driver)
#     # cards_page.goto()
#     assert cards_page.goto().get_card_by_name("Mirror").is_displayed()
#     #3. click the phoenix card
#     driver.find_element(By.CSS_SELECTOR,"[href*='Phoenix']").click()
#     #4. check the card details are displayed
#     cards_detail_page = Cards_Detail_Page(driver)
#     card_name = cards_detail_page.get_name_text()
#     # card_rarity = driver.find_element(By.CLASS_NAME, "card__legendary").text
#     card_rarity = cards_detail_page.get_rarity_text()
#     card_type = cards_detail_page.get_type_text()
#     card_arena = cards_detail_page.get_arena_text()
#
#     assert card_name == 'Mirror'
#     assert card_type == 'Spell'
#     assert card_arena == 'Arena 12'
#     assert card_rarity == 'Legendary'