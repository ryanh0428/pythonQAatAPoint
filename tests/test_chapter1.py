#Write a function that takes a string argument
#and return the number of vowels in it.

from selenium import webdriver

vowel = ['a','e', 'i', 'o','u']

def vowel_count(string):
    count = 0
    for character in string.lower():
        if character in vowel:
            count += 1
    return count


def longest_and_shortest_string(string):
    splitList = string.split()
    longest = splitList[0]
    shortest = splitList[0]
    for word in splitList:
        if len(word) > len(longest):
            longest = word
        if len(word) < len(shortest):
            shortest = word
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    driver.quit()
    return [shortest,longest]


def test_with_apple():
    assert vowel_count('apple') == 2

def test_with_banana():
    assert vowel_count('banana') == 3

def test_with_no_vowel():
    assert vowel_count('sdfyp') == 0

def test_with_capital():
    assert vowel_count('APPLE') == 2

def test_longest():
    assert longest_and_shortest_string("I am your boss")[1] == "your"

def test_shortest():
    assert longest_and_shortest_string("I am your boss")[0] == "I"