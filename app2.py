import asyncio
from pyppeteer import launch

async def generar_pdf(url, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    
    await page.goto(url)
    
    await page.pdf({ 'path': pdf_path, 'format': 'A4'})
    
    await browser.close()
    

asyncio.get_event_loop().run_until_complete(generar_pdf('index.html', 'ejemplo2.pdf'))
    