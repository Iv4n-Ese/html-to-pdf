from xhtml2pdf import pisa
import requests

def convert_url_to_pdf(url, pdf_path):
    # Obtiene el contenido HTML de la URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Fallo al buscar la URL: {url}")
        return False
    
    html_content = response.text
    
    # Genera el PDF
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)
        
    return not pisa_status.err

# URL a buscar
url_to_fetch = "http://www.pagina-a-convertir.html"

# Nombre del PDF a guardar
pdf_path = "nombreArchivo.pdf"

# Genera el PDF
if convert_url_to_pdf(url_to_fetch, pdf_path):
    print(f"PDF generado y guardado con el nombre de: {pdf_path}")
else:
    print("Fallo al generar el PDF")