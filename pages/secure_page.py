from selenium.webdriver.common.by import By

class SecurePage:
    def __init__(self, driver):
        self.driver = driver
        self.LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary")

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def is_logout_button_present(self):
        return len(self.driver.find_elements(*self.LOGOUT_BUTTON)) > 0