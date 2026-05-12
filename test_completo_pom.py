from playwright.sync_api import Page, expect
from pages.login_page import LoginPage       # Importamos Molde 1
from pages.inventory_page import InventoryPage # Importamos Molde 2

def test_flujo_completo_con_pom(page: Page):
    # --- FASE 1: LOGIN ---
    login = LoginPage(page)
    login.navegar()
    login.realizar_login("standard_user", "secret_sauce")

    # --- FASE 2: INVENTARIO (La estafeta pasa a la siguiente página) ---
    # No necesitamos abrir otro navegador, usamos la misma 'page'
    inventario = InventoryPage(page)
    
    # Validamos que llegamos bien
    expect(inventario.titulo_pagina).to_have_text("Products")
    
    # Agregamos el producto
    inventario.agregar_mochila()

    # --- FASE 3: VALIDACIÓN FINAL ---
    # Verificamos que el carrito marcó el número 1
    expect(inventario.obtener_badge_carrito()).to_have_text("1")
    
    print("\n¡Flujo POM completo exitoso! Login -> Inventario -> Carrito")