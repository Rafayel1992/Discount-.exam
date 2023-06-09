from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class BasePage():
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,by:By, value: str):
        try:
               elemnt = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((by,value)))
        except:
            print(f"Error 1 : Elemnt ({by}, {value})not visible")
        return elemnt

