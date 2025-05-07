import time
from selenium.webdriver.common.by import By

def get_element_click(driver, locator_type, locator):
    locator_map = {
        "id": By.ID,
        "name": By.NAME,
        "css_selector": By.CSS_SELECTOR,
        "xpath": By.XPATH,
        "class_name": By.CLASS_NAME,
        "tag_name": By.TAG_NAME
    }
    
    if locator_type not in locator_map:
        raise ValueError(f"Locator '{locator_type}' invalid. Use one of these: {list(locator_map.keys())}")

    element = driver.find_element(locator_map[locator_type], locator)
    element.click()

def get_element_send_keys(driver, locator_type, locator, value):
    locator_map = {
        "id": By.ID,
        "name": By.NAME,
        "css_selector": By.CSS_SELECTOR,
        "xpath": By.XPATH,
        "class_name": By.CLASS_NAME,
        "tag_name": By.TAG_NAME
    }
    
    if locator_type not in locator_map:
        raise ValueError(f"Locator '{locator_type}' invalid. Use one of these: {list(locator_map.keys())}")

    element = driver.find_element(locator_map[locator_type], locator)
    element.send_keys(value)

def get_element_value(driver, locator_type, locator):
    locator_map = {
        "id": By.ID,
        "name": By.NAME,
        "css_selector": By.CSS_SELECTOR,
        "xpath": By.XPATH,
        "class_name": By.CLASS_NAME,
        "tag_name": By.TAG_NAME
    }
    
    if locator_type not in locator_map:
        raise ValueError(f"Locator '{locator_type}' invalid. Use one of these: {list(locator_map.keys())}")

    element = driver.find_element(locator_map[locator_type], locator)
    return element.text

def sleep(seconds):
    time.sleep(seconds)