from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def escribir_por_id(driver, xpath, ruc):
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, xpath))
    )
    input_element.send_keys(ruc)

def click_por_xpath(driver, xpath):
    button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
    )
    button_element.click()

def click_por_id(driver, xpath):
    button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, xpath))
    )
    button_element.click()

def click_por_cssselector(driver, xpath):
    button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, xpath))
    )
    button_element.click()

def esperar_elemento_por_tag(driver, xpath):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, xpath))
    )