"""Module to fetch company code"""
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait

# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://www.google.com/finance/")
# driver.minimize_window()

nifty_50 = ["ADANIENT", "ADANIPORTS", "APOLLOHOSP", "ASIANPAINT", "AXISBANK", "BAJAJ-AUTO", "BAJFINANCE",
            "BAJAJFINSV", "BEL", "BPCL", "BHARTIARTL", "BRITANNIA", "CIPLA", "COALINDIA", "DRREDDY", "EICHERMOT",
            "GRASIM", "HCLTECH", "HDFCBANK", "HDFCLIFE", "HEROMOTOCO", "HINDALCO", "HINDUNILVR", "ICICIBANK", "ITC",
            "INDUSINDBK", "INFY", "JSWSTEEL"]
for company_code in nifty_50:
    input_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '//*[@id="yDmH0d"]/c-wiz[2]/div/div[3]/div[3]/div/div/div/div[1]/input[2]')))
    input_box.click()
    input_box.send_keys(company_code)
    input_box.send_keys(Keys.RETURN)
    prc_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@class="YMlKec fxKbKc"]')))
    company_name = driver.find_element(By.XPATH,
                                       '//*[@id="yDmH0d"]/c-wiz[3]/div/div[4]/div/main/div[1]/div[1]/div[2]')

    print(f"{company_name.text} today price is = {prc_label.text}")
    driver.back()
driver.quit()
