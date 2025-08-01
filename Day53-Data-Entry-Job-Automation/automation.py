from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from web_data import WebData

GOOGLE_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSeVm-7ShbJFVHdrwT2BGJYrRc-E-fDEY0Xm7t_ZgvTPW9kMqQ/viewform?usp=dialog'

class Automation:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.open_form()

    def open_form(self):
        self.driver.get(GOOGLE_FORM)
        sleep(3)

    def fill_form(self, addresses, prices, links):
        for i in range(len(addresses)):
            try:
                address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
                price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
                link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

                address_input.send_keys(addresses[i])
                price_input.send_keys(prices[i])
                link_input.send_keys(links[i])

                send_but = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
                send_but.click()
                sleep(2)

                new_rec_but = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Başka bir yanıt gönder')]")
                new_rec_but.click()
                sleep(2)

            except Exception as e:
                print(f"Error at index {i}: {e}")
