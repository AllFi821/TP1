from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"
        self.USERNAME_FIELD = (By.ID, "username")
        self.PASSWORD_FIELD = (By.ID, "password")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
        self.FLASH_MESSAGE = (By.ID, "flash")

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_flash_message(self):
        return self.driver.find_element(*self.FLASH_MESSAGE).text