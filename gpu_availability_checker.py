from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import requests
import webbrowser
from datetime import datetime
from colorama import Fore, Style
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException


# path to chrome.exe
pth_chrome = r""

webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(pth_chrome))
chrome = webbrowser.get("chrome")


# variables for notifications using Telegram

bot_token = "" # Bot token for Telegram
chat_id = ""  # chat id for the telegram channel the notifications get send to 
url = "https://api.telegram.org/bot%s/sendMessage?chat_id=%s" % (bot_token, chat_id)


# options for chrome browser, in this case headless without an gui
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

# path to chromedriver-exe
service = Service(r"")
driver = webdriver.Chrome(service=service, options=chrome_options)




# these are the keywords/phrases to look for on the respective stores 

#amazon
gpu_not_availabe_amazon = "Derzeit nicht verfügbar."

#mindfactory

gpu_availabe_mindfactory = "In den Warenkorb"


#alternate

gpu_available_alternate = "Auf Lager"
gpu_available_alternate_2 = "In den Warenkorb"
gpu_available_alternate_3 = "Ware neu eingetroffen"

# Galaxus

gpu_available_galaxus = "geliefert"
gpu_available_galaxus_2 = "Lager"

time_amazon = 0
time_alternate = 0
time_mindfactory = 0
time_galaxus = 0

# dictionary for gpus, with skus names and stores and the product url

gpu_dict = {
    "MSI Suprim 5090 (Amazon)": "https://www.amazon.de/dp/B0DT6SN14V", 
    "MSI Suprim Liquid 5090 (Amazon)": "https://www.amazon.de/dp/B0BSN426TP",
    "MSI Gaming Trio 5090 (Amazon)": "https://www.amazon.de/dp/B0DT6Q3BXM",
    "MSI Ventus 5090 (Amazon)":"https://www.amazon.de/dp/B0DT6S77JK",
    "ASUS Astral 5090 (Amazon)": "https://www.amazon.de/dp/B0DTHV8THW",
    "PNY 5090 (Amazon)":"https://www.amazon.de/dp/B0DTJF8YT4",
    "Gigabyte Windforce 5090 (Alternate)": "https://www.alternate.de/GIGABYTE/GeForce-RTX-5090-WINDFORCE-OC-32G-Grafikkarte/html/product/100108938",
    "Gigabyte Aorus Master 5090 (Alternate)": "https://www.alternate.de/GIGABYTE/GeForce-RTX-5090-AORUS-MASTER-32G-Grafikkarte/html/product/100108932",
    "Gigabyte Aorus Master Ice 5090 (Alternate)": "https://www.alternate.de/GIGABYTE/GeForce-RTX-5090-AORUS-MASTER-ICE-32G-Grafikkarte/html/product/100108931",
    "Gigabyte Gaming OC 5090 (Alternate)": "https://www.alternate.de/GIGABYTE/GeForce-RTX-5090-GAMING-OC-32G-Grafikkarte/html/product/100108936",
    "MSI Suprim Liquid 5090 (Alternate)": "https://www.alternate.de/MSI/GeForce-RTX-5090-32G-SUPRIM-LIQUID-SOC-Grafikkarte/html/product/100109560",
    "MSI Ventus 5090 (Alternate)": "https://www.alternate.de/MSI/GeForce-RTX-5090-32G-VENTUS-3X-OC-Grafikkarte/html/product/100109567",
    "ASUS ROG Astral Liquid (Alternate)": "https://www.alternate.de/ASUS/GeForce-RTX-5090-ROG-ASTRAL-LC-GAMING-OC-Grafikkarte/html/product/100110137",
    "Inno3d 5090 (Alternate)": "https://www.alternate.de/INNO3D/GeForce-RTX-5090-X3-Grafikkarte/html/product/100109380", 
    "ASUS ROG Astral (Alternate)": "https://www.alternate.de/ASUS/GeForce-RTX-5090-ROG-ASTRAL-GAMING-OC-Grafikkarte/html/product/100110139", 
    "Gainward Phantom 5090 (Alternate)":  "https://www.alternate.de/Gainward/GeForce-RTX-5090-Phantom-Grafikkarte/html/product/100109795", 
    "Zotac Solid 5090 (Alternate)": "https://www.alternate.de/ZOTAC/GeForce-RTX-5090-SOLID-Grafikkarte/html/product/100110077", 
    "ASUS TUF Gaming 5090 (Alternate)": "https://www.alternate.de/ASUS/GeForce-RTX-5090-TUF-GAMING-Grafikkarte/html/product/100110148",
    "ASUS TUF Gaming 5090 (Galaxus)": "https://www.galaxus.de/de/s1/product/asus-tuf-rtx5090-32g-gaming-32-gb-grafikkarte-54200110",
    "Palit Gamerock 5090 (Mindfactory)": "https://www.mindfactory.de/product_info.php/pid/awin/32GB-Palit-GeForce-RTX-5090-GameRock-Aktiv-PCIe-5-0-x16-1xHDMI-2-1b-3xD_1611615.html",
    "Gigabyte Gaming OC 5090 (Mindfactory)": "https://www.mindfactory.de/product_info.php/pid/awin/suggest/true/32GB-Gigabyte-GeForce-RTX-5090-Gaming-OC-Aktiv-PCIe-5-0-x16_1611048.html",
    "Gigabyte Windforce 5090 (Mindfactory)": "https://www.mindfactory.de/product_info.php/pid/awin/32GB-Gigabyte-GeForce-RTX-5090-Windforce-OC-Aktiv-PCIe-5-0-x16-1xHDMI-2_1611049.html",
    "Gigabyte Aorus Master 5090 (Mindfactory)": "https://www.mindfactory.de/product_info.php/pid/awin/32GB-Gigabyte-GeForce-RTX-5090-AORUS-Master-Aktiv-PCIe-5-0-x16-1xHDMI-2_1611047.html"}

def get_current_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")





try:
    # shuffles the items in gpu_dict
    while True: 
        gpu_items = list(gpu_dict.items())
        random.shuffle(gpu_items)
        
        # opens the gpu pages at retailers
        for gpu_name, gpu_url in gpu_items:
            current_time = time.time()
            time.sleep(random.uniform(1, 1.7))
            max_retries = 10
            retries = 0
            page_loaded = False
            while not page_loaded and retries < max_retries:
                try:
                    driver.get(gpu_url)
                    page_loaded = True
                except WebDriverException as e:
                    retries += 1
                    print(f"Attempt {retries} of {max_retries} failed")
                    time.sleep(10)
            
            if not page_loaded:
                print(f"Failed to load {gpu_url} after {max_retries} attempts.")

            time.sleep(2)  
            gpu_check = driver.execute_script("return document.body.innerText;")
           
           # checks availibilty on amazon by page content and if a page element is present
            if "Amazon" in gpu_name:
                if "Wir bitten um Ihr Verständnis und wollen uns sicher sein dass Sie kein Bot sind." in gpu_check:
                    print("Bot protection")
                try:
                    product_container = driver.find_element(By.ID, 'ppd')
                    price_element = product_container.find_element(By.CLASS_NAME, 'a-price-whole')
                    price_str = price_element.text.strip()

                    if price_str: 
                        price_str = price_str.replace('.', '').replace(',', '').replace('€', '')  
                        price = int(price_str)
                        price_not_found = False
                    else:
                        price = 9999
                        price_not_found = True
                except:
                    price_not_found = True
                    price = 9999

                # opens the page and sends notification if product is available and is under a certain price
                if gpu_not_availabe_amazon not in gpu_check:
                    if price_not_found and ("MSI Gaming Trio 5090 (Amazon)" not in gpu_name and "ASUS Astral 5090 (Amazon)" not in gpu_name):
                        print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Amazon")
                        requests.post(url, json={"text": gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
                        if current_time - time_amazon >= 360:
                            time_amazon = time.time()
                            requests.post(url, json={'text':"#"}, timeout=10)
                            chrome.open_new_tab(gpu_url)
                            
                    elif price < 4000:
                        print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Amazon")
                        requests.post(url, json={"text": gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
                        if current_time - time_amazon >= 360:
                            time_amazon = time.time()
                            requests.post(url, json={'text':"#"}, timeout=10)
                            chrome.open_new_tab(gpu_url)
                    else:
                        print(f"[{get_current_time()}] {gpu_name}"+ Fore.YELLOW + " 3rd party seller"+ Style.RESET_ALL + " at Amazon")
                    
                else:
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Amazon")
            
            # checks availability on Alternate and tries to add product to shopping cart
            elif "Alternate" in gpu_name:
                if gpu_available_alternate in gpu_check or gpu_available_alternate_2 in gpu_check or gpu_available_alternate_3 in gpu_check:
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Alternate")
                    requests.post(url, json={"text": gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
                    cookies_accepted = False
                    
                    while cookies_accepted == False:
                        try:
                            popup = driver.find_element(By.ID, "usercentrics-cmp-ui")
                            driver.execute_script("arguments[0].style.display = 'none';", popup) 
                            print("Cookie popup closed.")
                        except:
                            print("No cookie popup found.")
                        try:
                            button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart")))
                            button.click()
                            cookies_accepted = True
                        except TimeoutException:
                            print("Button was not clickable in time.")
                        except NoSuchElementException:
                            print("Button not found!")
                        except ElementClickInterceptedException:
                            print("Button is intercepted by another element (e.g., overlay or popup).")
                            cookies_accepted = False
                            driver.get(gpu_url)
                            time.sleep(1)

                    # if the product was added to the shopping cart, tries to extract a cookie for reserving it       
                    time.sleep(5)
                    cookie = driver.get_cookie("JSESSIONID") 
                    if cookie:
                        cart_cookie = cookie["value"]
                        print(cart_cookie)
                        requests.post(url, json={"text": cart_cookie}, timeout=10)
                    else:
                        print("Cookie not found!")
                    if current_time - time_alternate >= 360:
                        time_alternate = time.time()
                        requests.post(url, json={"text":"#"}, timeout=10)
                        chrome.open_new_tab(gpu_url)
                    
                else: 
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Alternate")           
            
            # checks availability on Mindfactory
            elif "Mindfactory" in gpu_name:
                if gpu_availabe_mindfactory in gpu_check:
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Mindfactory")
                    requests.post(url, json={"text": gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
                    if current_time - time_mindfactory >= 360:
                        time_mindfactory = time.time()
                        requests.post(url, json={"text":"#"}, timeout=10)
                        chrome.open_new_tab(gpu_url)
                    
                else: 
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Mindfactory")
            
            # checks availability on Galaxus
            elif "Galaxus" in gpu_name:
                if gpu_available_galaxus in gpu_check or gpu_available_galaxus_2 in gpu_check:
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Galaxus")
                    requests.post(url, json={"text": gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
                    if current_time - time_galaxus >= 360:
                        time_galaxus = time.time()
                        requests.post(url, json={"text":"#"}, timeout=10)
                        chrome.open_new_tab(gpu_url)
                    
                else: 
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Galaxus")
              
        time.sleep(random.uniform(1, 3))           
        
except KeyboardInterrupt:
    print("Script interrupted. Closing browser.")
    driver.quit()
    
