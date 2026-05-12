from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # Localizadores específicos de la tienda
        self.titulo_pagina = page.locator(".title")
        self.boton_add_backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.carrito_badge = page.locator(".shopping_cart_badge")

    def agregar_mochila(self):
        self.boton_add_backpack.click()

    def obtener_badge_carrito(self):
        return self.carrito_badge
    
    