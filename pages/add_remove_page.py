from selenium.webdriver.common.by import By
import time

class AddRemovePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/add_remove_elements/"
        
        self.ADD_BUTTON = (By.CSS_SELECTOR, "button[onclick='addElement()']")
        self.DELETE_BUTTONS = (By.CLASS_NAME, "added-manually")

    def load(self):
        self.driver.get(self.url)

    def add_element(self, times=1):
        for _ in range(times):
            button = self.driver.find_element(*self.ADD_BUTTON)
            self.driver.execute_script("arguments[0].click();", button)
            time.sleep(0.5)

    def get_delete_buttons_count(self):
        return len(self.driver.find_elements(*self.DELETE_BUTTONS))

    def delete_element(self):
        button = self.driver.find_element(*self.DELETE_BUTTONS)
        self.driver.execute_script("arguments[0].click();", button)