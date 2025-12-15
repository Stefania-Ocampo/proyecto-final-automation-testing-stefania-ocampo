import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.read_data import leer_datos_login



@pytest.mark.parametrize("usuario,password,resultado", leer_datos_login())
def test_login_saucedemo(driver, usuario, password, resultado):
    login = LoginPage(driver)
    login.ingresar_usuario(usuario)\
         .ingresar_password(password)\
         .click_login()

    if resultado == "ok":
        inventory = InventoryPage(driver)
        assert inventory.titulo_visible()
    else:
        assert "Epic sadface" in login.obtener_error()
