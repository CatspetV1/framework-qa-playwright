from playwright.sync_api import Page, expect

def test_crear_nuevo_registro_api(page: Page):
    # 1. Preparamos nuestro paquete de datos (El Body)
    nuevos_datos = {
        "title": "Ingeniero QA Automation",
        "body": "Aprendiendo Playwright en AlmaLinux",
        "userId": 1
    }
    
    # 2. Hacemos la petición POST. 
    # Fíjate cómo ahora usamos page.request.post() y le pasamos el parámetro 'data'
    respuesta = page.request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=nuevos_datos
    )
    
    # 3. Validamos que el servidor haya creado el registro con éxito.
    # El código HTTP para "Creado exitosamente" es el 201
    expect(respuesta).to_be_ok()
    assert respuesta.status == 201
    
    # 4. Extraemos la respuesta del servidor
    datos_creados = respuesta.json()
    
    # Imprimimos lo que nos respondió el servidor
    print(f"\n¡Registro creado en el servidor!: {datos_creados}")