from selenium.webdriver.common.by import By

class SerchResaltLocator():
  clickGenderBottonLocator = (By.XPATH,"//ul[@aria-labelledby='txAttrFacet_Gender']/li[2]")
  clicToProdukt = (By.XPATH, "//a[@data-style-id= '5811252']")

class SerchResalt(SerchResaltLocator):
    def __init__(self,driver):
        self.driver = driver


    def click_to_gender_botton(self):
       searchBottomElement = self.driver.find_element(*(self.clickGenderBottonLocator))
       searchBottomElement.click()

    def click_to_produkt_button(self):
        addCartElement = self.driver.find_element(*(self.clicToProdukt))
        addCartElement.click()