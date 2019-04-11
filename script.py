from config import keys
from selenium import webdriver
import time

def order(k):

    driver = webdriver.Chrome('./chromedriver')
	
    driver.get(k['url'])
    
	#send_keys recibe una string, escribe un un texfield
	#.click() hace click
	#find_element_by_xpath busca un elemento por xpath ... inspeccionar ... copiar ... xpath
	
    driver.find_element_by_xpath('//*[@id="email-email"]').send_keys(k['email'])
    driver.find_element_by_xpath('//*[@id="password-password"]').send_keys(k['pass'])
    driver.find_element_by_xpath('//*[@id="sumbitLogin"]').click()
    time.sleep(5) 
	
if __name__ == '__main__':
    order(keys)
