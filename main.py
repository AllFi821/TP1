import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from pages.dropdown_page import DropdownPage
from pages.add_remove_page import AddRemovePage

# Configuration
driver = webdriver.Chrome()
driver.implicitly_wait(5)

def run_tp1():
    try:
        # --- PARTIE 1 : AUTHENTIFICATION ---
        print("\n--- Phase 1: Authentification ---")
        login_pg = LoginPage(driver)
        secure_pg = SecurePage(driver)
        
        login_pg.load()
        assert "Login Page" in driver.page_source
        print("[OK] Page de login chargée.")

        login_pg.login("tomsmith", "SuperSecretPassword!")
        assert "You logged into a secure area!" in login_pg.get_flash_message()
        assert secure_pg.is_logout_button_present()
        print("[OK] Connexion réussie et message validé.")

        secure_pg.logout()
        assert "You logged out of the secure area!" in login_pg.get_flash_message()
        print("[OK] Logout réussi, retour à la page de login.")


        # --- PARTIE 2 : DROPDOWN ---
        print("\n--- Phase 2: Liste Déroulante ---")
        dropdown_pg = DropdownPage(driver)
        dropdown_pg.load()

        for option in ["Option 1", "Option 2"]:
            dropdown_pg.select_by_text(option)
            assert dropdown_pg.get_selected_text() == option
            print(f"[OK] {option} sélectionnée et vérifiée.")


        # --- PARTIE 3 : ADD/REMOVE ELEMENTS ---
        print("\n--- Phase 3: Éléments Dynamiques ---")
        add_remove_pg = AddRemovePage(driver)
        add_remove_pg.load()

        add_remove_pg.add_element(3)
        time.sleep(1)
        assert add_remove_pg.get_delete_buttons_count() == 3
        print("[OK] 3 éléments ajoutés.")

        add_remove_pg.delete_element()
        assert add_remove_pg.get_delete_buttons_count() == 2
        print("[OK] 1 élément supprimé, il en reste 2.")

        # Supprimer les restants
        while add_remove_pg.get_delete_buttons_count() > 0:
            add_remove_pg.delete_element()
        
        assert add_remove_pg.get_delete_buttons_count() == 0
        print("[OK] Tous les éléments supprimés.")

        print("\n==============================")
        print("   TOUS LES TESTS ONT RÉUSSI  ")
        print("==============================")

    except Exception as e:
        print(f"\n[ERREUR] Le test a échoué : {e}")
        driver.save_screenshot("erreur_tp1.png")
        print("Capture d'écran 'erreur_tp1.png' enregistrée.")

    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    run_tp1()