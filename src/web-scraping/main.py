import pandas as pd
from playwright.sync_api import sync_playwright
from utils.utils import crear_carpeta

file_path = crear_carpeta("report.xlsx")

with sync_playwright() as p: 
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_extra_http_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    page.goto("https://datos.bancomundial.org/indicador/FR.INR.RINR")

    page.wait_for_selector(".item")  
    countries = page.query_selector_all(".item")
    data = []

    for country in countries:
        name_element = country.query_selector("a.country-name")  

        if name_element:  
            year_element = country.query_selector("div:nth-of-type(2)")  
            value_element = country.query_selector("div:nth-of-type(3)")    

            if year_element and value_element:
                name = name_element.text_content().strip()
                year = year_element.text_content().strip()
                value = value_element.text_content().strip()
                data.append({"País": name, "Año": year, "Valor": value})
        else:
            continue

    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False, engine="openpyxl")
    print(f"Reporte generado exitosamente: {file_path}")

    browser.close()