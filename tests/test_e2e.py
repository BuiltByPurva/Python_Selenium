# tests/test_e2e.py
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")   # headless (works better on newer Chrome)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_homepage_and_nav(driver):
    driver.get("http://localhost:5000/")
    h = driver.find_element(By.ID, "welcome").text
    assert "Hello from Flask" in h
    driver.find_element(By.ID, "next").click()
    time.sleep(0.5)
    assert "Next page reached" in driver.page_source
