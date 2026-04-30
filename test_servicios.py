import requests

def test_validar_usuarios_api_local():
    # 1. Apuntamos a tu servidor local en lugar de la URL real
    url = "http://localhost:8080/usuarios.json.js"
    
    # 2. Hacemos la petición GET
    respuesta = requests.get(url)
    
    # 3. Validamos que el servidor local responda 200 OK
    assert respuesta.status_code == 200, f"Falló: Código de estado fue {respuesta.status_code}"
    
    # 4. Validamos que el JSON simulado contenga 'data'
    cuerpo_respuesta = respuesta.json()
    assert "data" in cuerpo_respuesta, "Falló: El JSON no contiene el nodo 'data'"
    
    print("\n¡Prueba automatizada exitosa! Burlamos el proxy usando un Mock local.")