from selenium.webdriver.common.by import By
import time

class AddRemovePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/add_remove_elements/"
        
        # On cible précisément le bouton grâce à l'attribut vu sur ton image
        self.ADD_BUTTON = (By.CSS_SELECTOR, "button[onclick='addElement()']")
        
        # Les boutons Delete qui apparaissent ont la classe 'added-manually'
        self.DELETE_BUTTONS = (By.CLASS_NAME, "added-manually")

    def load(self):
        self.driver.get(self.url)

    def add_element(self, times=1):
        for _ in range(times):
            # On s'assure de bien recliquer sur le bouton à chaque itération
            self.driver.find_element(*self.ADD_BUTTON).click()
            time.sleep(0.5)

    def get_delete_buttons_count(self):
        # Renvoie le nombre actuel de boutons Delete présents dans le DOM
        return len(self.driver.find_elements(*self.DELETE_BUTTONS))

    def delete_element(self):
        # Clique sur le premier bouton Delete disponible
        self.driver.find_element(*self.DELETE_BUTTONS).click()