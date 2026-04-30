
from playwright.sync_api import Page, expect

def test_login_exitoso(page: Page):
    # 1. Navegamos a la página de pruebas
    page.goto("https://www.saucedemo.com/")
    
    # 2. Llenamos el formulario (Buscamos por el 'id' del elemento)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    
    # 3. Hacemos clic en el botón de login
    page.click("#login-button")
    
    # 4. ASERCIÓN: Validamos que pasamos al dashboard buscando el título "Products"
    expect(page.locator(".title")).to_have_text("Products")
    
    print("\n¡Login automatizado exitosamente! El robot controló el navegador.")