# Imports Selenium python module
from selenium import webdriver

class LogoTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):

        print("")

        #Find the logo picture by id
        logo = driver.find_element_by_id("logo")
        #Write logos patch
        print(logo.get_attribute("src"))
