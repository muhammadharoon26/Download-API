from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import time

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

def search_image(s):
    if s.find(".") != -1:
        driver.get(s)
    else:
        driver.get('https://www.google.com/search?as_st=y&tbm=isch&as_q=&as_epq={}&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=isz:lt,islt:xga'.format(s.replace(' ','+')))
    # time.sleep(1)

def image_click(i):
    image_results = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
    first_image = image_results[i]
    first_image.click()
    # time.sleep(1)

def download_image(i):
    image_element = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
    image_url = image_element[i].get_attribute("src")
    local_file = f"D:\\Git-Hub\\Download-API\\Images\\{s} Image #{i+1}.jpg"
    urllib.request.urlretrieve(image_url, local_file)

if __name__ == "__main__":
    s = input("SEARCH: ")
    search_image(s)
    print("Downloading Images of "+s)
    for i in range(100):
        image_click(i)
        download_image(i)
    print("All Images Downloaded !")