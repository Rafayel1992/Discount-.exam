from selenium.webdriver.common.by import By
from discoutSoes.BasePage.basePage import BasePage

class NavigtionBarLocator():
    serchFieldLocator = (By.ID,"searchAll")
    clickSerchBottonLocator = (By.XPATH,"//button[@type = 'submit']")


class NavigtionBar(NavigtionBarLocator,BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def fill_serch_field(self,txet):
        serchFieldElement =self.find_element(*(self.serchFieldLocator))
        serchFieldElement.clear()
        serchFieldElement.send_keys(txet)

    def click_to_serch_botton(self):
        searchBottomElement = self.find_element(*(self.serchFieldLocator))
        searchBottomElement.click()


