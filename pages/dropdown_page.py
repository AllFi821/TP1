from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropdownPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/dropdown"
        self.DROPDOWN = (By.ID, "dropdown")

    def load(self):
        self.driver.get(self.url)

    def select_by_text(self, text):
        select = Select(self.driver.find_element(*self.DROPDOWN))
        select.select_by_visible_text(text)

    def get_selected_text(self):
        select = Select(self.driver.find_element(*self.DROPDOWN))
        return select.first_selected_option.text