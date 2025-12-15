from selenium.webdriver.common.by import By

class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def titulo_visible(self):
        return self.driver.find_element(*self.TITLE).is_displayed()

    def agregar_producto(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def ir_al_carrito(self):
        self.driver.find_element(*self.CART).click()
