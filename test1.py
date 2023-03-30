import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import logging
from selenium.webdriver.common.by import By

from loguru import logger
logger.add("german.txt", format="{time}, {level} , {message}")
def test1():
    driver = webdriver.ChromeOptions()

    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    driver = webdriver.Chrome()
    logger.info(f"smoke test pass")

    driver.get(url)
    driver.fullscreen_window()
    logger.info( 'Enter the site -www.globalsqa.com-')
    time.sleep(2)

    customers_login = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button')
    customers_login.click()
    logger.info( 'click on customers login')
    time.sleep(2)

    your_name = driver.find_element(By.NAME, 'userSelect')
    your_name.click()
    logger.info('Click on Your name')
    time.sleep(2)

    harry = driver.find_element(By.XPATH, '//*[@id="userSelect"]/option[3]')
    harry.click()
    logger.info('Click on harry potter')
    time.sleep(2)

    login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button')
    login_button.click()
    logger.info('Click on login')
    time.sleep(2)

    login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[2]')
    login_button.click()
    logger.info('Click on deposit')
    time.sleep(2)

    login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input')
    login_button.click()
    logger.info('Click on amount')
    time.sleep(2)

    text_box = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input')
    text_box.send_keys('eeeee')
    logger.info('enter eeeee')
    time.sleep(2)

    deposit = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/button')
    deposit.click()
    logger.info('Click on deposit')
    time.sleep(3)

    if driver.find_element(By.CSS_SELECTOR,
                           'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > span'):
        return False
    else:
        return True




