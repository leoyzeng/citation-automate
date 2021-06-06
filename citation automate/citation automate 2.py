# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



class TestCitation():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def repeat(self):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"create-citations-btn\"]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"website-button\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"citation-search-input\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "html").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"citation-search-input\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"citation-search-input\"]").send_keys(
            "https://www.citationmachine.net/")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-fzoXWK > .sc-fzoMdx").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".sc-fzoMdx")
        actions = ActionChains(self.driver)
        self.driver.implicitly_wait(10)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-fzoMdx > .styled__ResultButtonText-jhqr36-14").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"submit-eval\"]").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"submit-eval\"]")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"form-next-button\"]").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".jEGbDM")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".button__SpecialButton-sc-1lt38zg-1 > .sc-fzoMdx").click()
    def start(self):
        self.driver.get("https://www.citationmachine.net/")


file1 = open("list_of_webcites.txt","r")
f1 = file1.readlines()
citation = TestCitation()
citation.setup_method(citation)
citation.start()

for lineNum in f1:

    link = lineNum
    print(lineNum)

    citation.repeat()