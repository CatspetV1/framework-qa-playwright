import json
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# --- EL CEREBRO DE DATOS ---
def cargar_usuarios():
    with open("usuarios.json", "r") as archivo:
        return json.load(archivo)

# --- LA PRUEBA INTELIGENTE ---
@pytest.mark.parametrize("datos_usuario", cargar_usuarios())
def test_compras_y_bloqueos(page: Page, datos_usuario):
    
    # 1. Extraemos TODOS los datos del JSON
    usuario = datos_usuario["username"]
    password = datos_usuario["password"]
    espera_entrar = datos_usuario["espera_entrar"] # Esta es la clave del comportamiento
    
    # 2. Todos los usuarios intentan loguearse (Fase común)
    login = LoginPage(page)
    login.navegar()
    login.realizar_login(usuario, password)
    
    # 3. BIFURCACIÓN: El script decide qué probar basándose en el JSON
    if espera_entrar == True:
        # --- Camino de Éxito (Flujo Feliz) ---
        inventario = InventoryPage(page)
        expect(inventario.titulo_pagina).to_have_text("Products")
        inventario.agregar_mochila()
        expect(inventario.obtener_badge_carrito()).to_have_text("1")
        print(f"\n[✔️] COMPRA EXITOSA: El usuario {usuario} logró comprar.")
        
    else:
        # --- Camino de Error (Flujo Negativo) ---
        # Validamos que el sistema no lo deje entrar y le muestre el mensaje rojo
        mensaje_error = page.locator("[data-test=\"error\"]")
        expect(mensaje_error).to_be_visible()
        print(f"\n[🚫] BLOQUEO EXITOSO: El sistema detuvo correctamente al usuario {usuario}.")