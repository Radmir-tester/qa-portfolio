from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys , ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

def open():
    browser.implicitly_wait(20)
    browser.maximize_window()

def open_main_page ():
    browser.get("https://www.labirint.ru/")
    my_cookie = {
        'name': 'cookie_policy' ,
        'value': '1'
    } 
    browser.add_cookie(my_cookie)

def search(term: str):
    poisk = browser.find_element(By.CSS_SELECTOR, "[placeholder='Поиск по Лабиринту']")
    poisk.send_keys(term, Keys.ENTER)

def go_to_card_page(index: int):
    browser.find_elements(By.CSS_SELECTOR , ".product-card ")[index].click()

def click_on_buy_button():
    waiter = WebDriverWait(browser , 20)
    waiter.until (EC.presence_of_element_located((By.CSS_SELECTOR,"._delivery_zuu52_128"))) 
    locator = browser.find_element(By.CSS_SELECTOR,"._price_zuu52_13")
    locator.click()

def get_cart_counter():
    return browser.find_element(By.CSS_SELECTOR , ".cartCount_aiaze_184").text 

def close_driver():
    browser.quit()

def test_1():
    open()
    open_main_page()
    search("python")
    go_to_card_page(0)
    click_on_buy_button()
    counter = get_cart_counter()
    print(counter == "1")
    close_driver()
test_1()

