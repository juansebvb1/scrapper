import json
import requests
from bs4 import BeautifulSoup

url = "https://www.idealista.com/alquiler-viviendas/tarragona-provincia/"

# Ejemplo de cabeceras adicionales
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Referer": "https://www.google.com/"
}

with requests.Session() as s:
    s.headers.update(headers)
    response = s.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Si lo deseas, aquí puedes extraer datos específicos
        html_content = soup.prettify()
        
        # Prepara los datos a enviar
        data = {
            "html": html_content,
            # Agrega más campos si extraes otros datos
        }
        
        # URL del webhook en n8n (cambia este valor por el que te haya proporcionado n8n)
        webhook_url = "https://prueba123.app.n8n.cloud/webhook-test/1e5859e6-7583-4b62-899a-971061c772b9"
        
        # Envía los datos a n8n
        webhook_response = requests.post(webhook_url, json=data)
        
        if webhook_response.status_code == 200:
            print("Datos enviados correctamente a n8n")
        else:
            print("Error al enviar los datos a n8n:", webhook_response.status_code)
    else:
        print("Error al obtener la página:", response.status_code)
