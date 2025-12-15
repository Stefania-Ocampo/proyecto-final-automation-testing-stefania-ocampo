from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def ingresar_usuario(self, user):
        self.driver.find_element(*self.USERNAME).send_keys(user)
        return self

    def ingresar_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def obtener_error(self):
        return self.driver.find_element(*self.ERROR_MSG).text
