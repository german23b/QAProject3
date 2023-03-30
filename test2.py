# driver = webdriver.Chrome('/Users/german/Desktop/chromedriver_mac64')
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from loguru import logger

def test2():
    driver = webdriver.Chrome()
    driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    logger.log(3, 'Enter the site -www.globalsqa.com-')
    driver.fullscreen_window()
    logger.info('fullscreen')
    time.sleep(2)

    customers_login = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button')
    customers_login.click()
    logger.info('Click on customer login')
    time.sleep(2)

    your_name = driver.find_element(By.NAME, 'userSelect')
    your_name.click()
    logger.info('Click on Your name')
    time.sleep(2)

    harry = driver.find_element(By.XPATH, '//*[@id="userSelect"]/option[4]')
    harry.click()
    logger.info('Click on Ron weasly')
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
    text_box.send_keys('10')
    logger.info('enter 10')
    time.sleep(2)

    deposit1 = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/button')
    logger.info('Click on deposit')
    deposit1.click()

    text_box = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input')
    time.sleep(1)
    text_box.send_keys('100')
    logger.info('enter 100')
    time.sleep(2)

    deposit2 = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/button')
    logger.info('Click on deposit')
    deposit2.click()

    text_box = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input')
    time.sleep(1)
    text_box.send_keys('250')
    logger.info('enter 250')
    time.sleep(2)

    deposit3 = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/button')
    deposit3.click()
    logger.info('Click on deposit')
    time.sleep(2)

    transactions = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[1]')
    transactions.click()
    logger.info('Click on transactions')
    time.sleep(2)

    driver.save_screenshot('the test result.png')
    time.sleep(2)

    if driver.find_element(By.CSS_SELECTOR, '#anchor0 > td:nth-child(2)'):
        return False
    if driver.find_element(By.CSS_SELECTOR, '#anchor1 > td:nth-child(2)'):
        return False
    if driver.find_element(By.CSS_SELECTOR, '#anchor2 > td:nth-child(2)'):
        return False
