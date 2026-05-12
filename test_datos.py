import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage  

lista_de_usuarios = [
    ("standard_user", "secret_sauce", True),    
    ("locked_out_user", "secret_sauce", False), 
    ("problem_user", "secret_sauce", True)      
]

@pytest.mark.parametrize("usuario, password, deberia_entrar", lista_de_usuarios)
def test_login_masivo(page: Page, usuario, password, deberia_entrar):
    
    login = LoginPage(page)
    login.navegar()
    login.realizar_login(usuario, password)
    
    if deberia_entrar:
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        mensaje_error = page.locator("[data-test=\"error\"]")
        expect(mensaje_error).to_be_visible()