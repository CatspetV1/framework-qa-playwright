from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        # Guardamos la pestaña del navegador
        self.page = page
        
        # DEFINIMOS LOS LOCALIZADORES (Si algo cambia, solo se edita aquí)
        self.username_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")

    # DEFINIMOS LAS ACCIONES (Los métodos)
    def navegar(self):
        self.page.goto("https://www.saucedemo.com/")

    def realizar_login(self, usuario, password):
        self.username_input.fill(usuario)
        self.password_input.fill(password)
        self.login_button.click()