from playwright.sync_api import Page, expect

def test_bypass_login_saucedemo(page: Page):
    # 1. Para poder inyectar una cookie, primero debemos "tocar" la puerta de la página
    # Esto es necesario para que Playwright sepa a qué dominio pertenece la cookie.
    page.goto("https://www.saucedemo.com/")
    
    # 2. EL TRUCO DE MAGIA: Inyectamos la cookie de sesión directamente.
    # En SauceDemo, la llave maestra es una cookie llamada "session-username"
    page.context.add_cookies([
        {
            "name": "session-username", 
            "value": "standard_user", 
            "url": "https://www.saucedemo.com/"
        }
    ])
    
    # 3. ¡El Gran Salto! Vamos directo a la página protegida (el inventario)
    # Fíjate que en ningún momento hicimos clics ni llenamos passwords
    page.goto("https://www.saucedemo.com/inventory.html")
    
    # 4. Validamos que efectivamente estamos adentro
    titulo = page.locator(".title")
    expect(titulo).to_have_text("Products")
    
    print("\n¡Bypass exitoso! Hackeamos la entrada sin tocar la pantalla de login.")