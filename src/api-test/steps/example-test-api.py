import os
import requests
from behave import given, when, then
from dotenv import load_dotenv

response = None
load_dotenv()

@given("the path is {path}")
def step_set_url(context, path):
    clean_path = path.strip('"')
    context.url = os.getenv("API_BASEURL")+clean_path

@when("I make a GET request")
def step_make_get_request(context):
    global response
    response = requests.get(context.url)

@then("the response status should be {status:d}")
def step_verify_status(context, status):
    assert response.status_code == status, f"Expected status: {status}, but received {response.status_code}"

@then("the response name should be {name}")
def step_verify_status(context, name):
    clean_name = name.strip('"')
    data = response.json()
    assert data["data"]["first_name"] == clean_name, f"Expected name: {clean_name}, but received {data["data"]["first_name"]}"