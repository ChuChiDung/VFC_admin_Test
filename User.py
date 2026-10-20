from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class User:
    def __init__(self, driver):
        self.driver = driver

    def User_AdminVFC (self):
        element = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"button.user-chip"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element)
        self.driver.execute_script("arguments[0].click();",element)

    def Setting_CaNhan (self):
        element = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"a.account-dropdown-link[href='/account/settings']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element)
        self.driver.execute_script("arguments[0].click();",element)

    def LOG_OUT (self):
        element = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"form.account-dropdown-logout button[type='submit']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element)
        self.driver.execute_script("arguments[0].click();",element)
