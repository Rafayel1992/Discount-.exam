from selenium.webdriver.common.by import By


class MensSizesLocator():
  clicToSizes = (By.XPATH,'//label[@for="radio-2829-9593349"]')
  addToCartBotton = (By.XPATH,"//button[@form='buyBoxForm']")
  clickCloseButton = (By.XPATH,"//button[@class='yl-z on-z']")


class MensSizes( MensSizesLocator):
    def __init__(self,driver):
        self.driver = driver


    def click_to_size(self):
       searchBottomElement = self.driver.find_element(*(self.clicToSizes))
       searchBottomElement.click()

    def add_to_cart_button(self):
        addCartElement = self.driver.find_element(*(self.addToCartBotton))
        addCartElement.click()

    def click_to_close_button(self):
        clicCloseButtonElement = self.driver.find_element(*(self.clickCloseButton))
        clicCloseButtonElement.click()