from selenium import webdriver
import unittest
from discoutSoes.NavBar.Nav_Bar import NavigtionBar
from discoutSoes.NavBar.serchResalt import SerchResalt
from discoutSoes.NavBar.Produkt.produkt import MensSizes
import time




class SercheTest (unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.6pm.com/adidas-ultraboost")
        self.navigtionBarObj = NavigtionBar(self.driver)
        self.serchResaltObj = SerchResalt(self.driver)
        self.produktObj = MensSizes(self.driver)
        


    def test_sercheResalt(self):
        self.navigtionBarObj.fill_serch_field('adidas ultraboost')
        self.navigtionBarObj.click_to_serch_botton()
        self.serchResaltObj.click_to_gender_botton()
        self.serchResaltObj.click_to_produkt_button()
        time.sleep(3)
        self.produktObj.click_to_size()
        self.produktObj.add_to_cart_button()
        time.sleep(3)
        self.navigtionBarObj.go_to_home_page()






    def tearDown(self) -> None:
            self.driver.close()
