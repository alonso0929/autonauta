import os
from utils.interactions import get_element_click, get_element_send_keys, get_element_value, sleep
from behave import given, when, then
from dotenv import load_dotenv
from locators.locators import Locators
from selenium import webdriver

load_dotenv()
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

@given("user navigates to Consulta SUNAT page")
def step_set_url(context):
    driver.get(os.getenv("WEB_URL"))
    sleep(1)

@when("user search for RUC {ruc}")
def step_make_get_request(context, ruc):
    get_element_send_keys(driver, "name", Locators.TXT_RUC, ruc)
    sleep(2)
    get_element_click(driver, "id", Locators.BTN_SEARCH)
    sleep(2)

@then("it should show all the results according to the search {name}")
def step_verify_status(context, name):
    clean_name = name.strip('"')
    value_name = get_element_value(driver, "xpath", Locators.LBL_NAME)
    assert value_name == clean_name, f"Expected name: {clean_name}, but received {value_name}"
