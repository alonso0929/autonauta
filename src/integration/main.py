import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from .utils.configurations import chrome_options
from .utils.interactions import escribir_por_id, click_por_xpath, click_por_id, click_por_cssselector, esperar_elemento_por_tag
from .utils.utils import extract_table_data
from .locators.locators import Locators
 
load_dotenv()

def get_informacion_historica(ruc:str):
    driver = chrome_options()

    try:
        driver.get(os.getenv("WEB_URL_SCRAP"))
        escribir_por_id(driver, Locators.TXT_RUC, ruc)
        click_por_id(driver, Locators.BTN_ACEPTAR)
        click_por_xpath(driver, Locators.BTN_INFORMACION_HISTORICA)
        esperar_elemento_por_tag(driver, "tbody")

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        tables = soup.find_all("table")
    
        table_keys = [
            ["Nombre o Razón Social", "Fecha de Baja"],
            ["Condición del Contribuyente", "Fecha desde", "Fecha hasta"],
            ["Dirección del Domicilio Fiscal", "Fecha de Baja"]
        ]

        extracted_data = {
            "razon_social": extract_table_data(tables[0], table_keys[0]),
            "contribuyentes": extract_table_data(tables[1], table_keys[1]),
            "direcciones": extract_table_data(tables[2], table_keys[2])
        }

        return extracted_data
    finally:
        driver.quit()

def get_trabajadores(ruc:str):
    driver = chrome_options()

    try:
        driver.get(os.getenv("WEB_URL_SCRAP"))

        escribir_por_id(driver, Locators.TXT_RUC, ruc)
        click_por_id(driver, Locators.BTN_ACEPTAR)
        click_por_cssselector(driver, Locators.BTN_TRABAJADORES)
        esperar_elemento_por_tag(driver, "tbody")
 
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        tbody = soup.find("tbody")
        data = []
        if tbody:
            rows = tbody.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                if len(cells) >= 4:  
                    data.append({
                        "Periodo": cells[0].text.strip(),
                        "N° de Trabajadores": cells[1].text.strip(),
                        "N° de Pensionistas": cells[2].text.strip(),
                        "N° de Prestadores de Servicios": cells[3].text.strip()
                    })
                else:
                    print(f"Fila incompleta: {cells}")  
        return {
            "trabajadores": data,
        }  
    finally:
        driver.quit()

def get_representantes_legales(ruc:str):
    driver = chrome_options()

    try:
        driver.get(os.getenv("WEB_URL_SCRAP"))

        escribir_por_id(driver, Locators.TXT_RUC, ruc)
        click_por_id(driver, Locators.BTN_ACEPTAR)
        click_por_xpath(driver, Locators.BTN_REPRESENTANTES_LEGALES)
        esperar_elemento_por_tag(driver, "tbody")
 
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        tbody = soup.find("tbody")
        data = []
        if tbody:
            rows = tbody.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                if len(cells) >= 5:  
                    data.append({
                        "Documento": cells[0].text.strip(),
                        "Nro Documento": cells[1].text.strip(),
                        "Nombre": cells[2].text.strip(),
                        "Cargo": cells[3].text.strip(),
                        "Fecha desde": cells[4].text.strip()
                    })
                else:
                    print(f"Fila incompleta: {cells}")  
        return {
            "representantes_legales": data,
        }  
    finally:
        driver.quit()