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

pth_chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pth_firefox = r"C:\Program Files\Mozilla Firefox\firefox.exe"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(pth_chrome))
chrome = webbrowser.get('chrome')
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(pth_firefox))
firefox = webbrowser.get('firefox')

url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s' % (
'', '')
webhook_url = ""


# headless

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
service = Service(r"C:\Program Files\Google\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)


# with browser

# service = Service(r"C:\Program Files\Google\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service)

#amazon
gpu_not_availabe = "Derzeit nicht verfügbar."

#mindfactory

gpu_availabe_mindfactory = "In den Warenkorb"


#alternate


gpu_available_alternate = "Auf Lager"
gpu_available_alternate_2 = "In den Warenkorb"
gpu_available_alternate_3 = "Ware neu eingetroffen"

# Galaxus

gpu_available_galaxus = "geliefert"
gpu_available_galaxus_2 = "Lager"


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
    "ASUS TUF Gaming 5090 (Galaxus)": "https://www.galaxus.de/de/s1/product/asus-tuf-rtx5090-32g-gaming-32-gb-grafikkarte-54200110",}

mind_ = { "Palit Gamerock 5090 (Mindfactory)": "https://www.mindfactory.de/product_info.php/pid/awin/32GB-Palit-GeForce-RTX-5090-GameRock-Aktiv-PCIe-5-0-x16-1xHDMI-2-1b-3xD_1611615.html",
    "Gigabyte Gaming OC 5090 (Mindfactory)": "https://www.mindfactory.de/product_info.php/pid/awin/suggest/true/32GB-Gigabyte-GeForce-RTX-5090-Gaming-OC-Aktiv-PCIe-5-0-x16_1611048.html",
    "Gigabyte Windforce 5090 (Mindfactory)": "https://www.mindfactory.de/product_info.php/pid/awin/32GB-Gigabyte-GeForce-RTX-5090-Windforce-OC-Aktiv-PCIe-5-0-x16-1xHDMI-2_1611049.html",
    "Gigabyte Aorus Master 5090 (Mindfactory)": "https://www.mindfactory.de/product_info.php/pid/awin/32GB-Gigabyte-GeForce-RTX-5090-AORUS-Master-Aktiv-PCIe-5-0-x16-1xHDMI-2_1611047.html"}

def get_current_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


time_amazon = 0
time_alternate = 0
time_mindfactory = 0
time_galaxus = 0



try:

    while True: 
        gpu_items = list(gpu_dict.items())
        random.shuffle(gpu_items)
        
        
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

            
            # if "Amazon" in gpu_name:
            #     price_not_found = False
            #     if "Wir bitten um Ihr Verständnis und wollen uns sicher sein dass Sie kein Bot sind." in gpu_check:
            #         print("Bot protection")
            #     try:
            #         product_container = driver.find_element(By.ID, 'ppd')  # Main product container
            #         price_element = product_container.find_element(By.CLASS_NAME, 'a-price-whole')
            #         if price_element:
            #             price_str = price_element.text.strip()
            #             price_str = price_str.replace('.', '').replace(',', '').replace('€', '')  
            #             price = int(price_str)
            #     except:
            #         price_not_found = True
                
            #     if gpu_not_availabe not in gpu_check and (price_not_found or price < 4000):
            #         print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Amazon")
            #         requests.post(url, json={'text': gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
            #         if current_time - time_amazon >= 360:
            #             time_amazon = time.time()
            #             requests.post(url, json={'text':"#"}, timeout=10)
            #             chrome.open_new_tab(gpu_url)
            #     else:
            #         print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Amazon")
            
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

                # try:
                #     product_container = driver.find_element(By.ID, 'ppd')  # Main product container
                #     price_element = product_container.find_element(By.CLASS_NAME, 'a-price-whole')
                #     if price_element:
                #         price_str = price_element.text.strip()
                #         price_str = price_str.replace('.', '').replace(',', '').replace('€', '')  
                #         price = int(price_str)
                #     else:
                #         price = 9999
                # except:
                #     price_not_found = True
                #     price = 9999
                
                if gpu_not_availabe not in gpu_check:
                    if price_not_found and ("MSI Gaming Trio 5090 (Amazon)" not in gpu_name and "ASUS Astral 5090 (Amazon)" not in gpu_name):
                        print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Amazon")
                        requests.post(url, json={'text': gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
                        if current_time - time_amazon >= 360:
                            time_amazon = time.time()
                            requests.post(url, json={'text':"#"}, timeout=10)
                            chrome.open_new_tab(gpu_url)
                            
                    elif price < 4000:
                        print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Amazon")
                        requests.post(url, json={'text': gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
                        if current_time - time_amazon >= 360:
                            time_amazon = time.time()
                            requests.post(url, json={'text':"#"}, timeout=10)
                            chrome.open_new_tab(gpu_url)
                    else:
                        print(f"[{get_current_time()}] {gpu_name}"+ Fore.YELLOW + " 3rd party seller"+ Style.RESET_ALL + " at Amazon")
                    
                else:
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Amazon")
            
            elif "Alternate" in gpu_name:
                if gpu_available_alternate in gpu_check or gpu_available_alternate_2 in gpu_check or gpu_available_alternate_3 in gpu_check:
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Alternate")
                    requests.post(url, json={'text': gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
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
                            
                    time.sleep(5)
                    cookie = driver.get_cookie("JSESSIONID") 
                    if cookie:
                        cart_cookie = cookie['value']
                        print(cart_cookie)
                        requests.post(url, json={'text': cart_cookie}, timeout=10)
                    else:
                        print("Cookie not found!")
                    if current_time - time_alternate >= 360:
                        time_alternate = time.time()
                        requests.post(url, json={'text':"#"}, timeout=10)
                        chrome.open_new_tab(gpu_url)
                    
                else: 
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Alternate")           
            
                        
            # elif "Alternate" in gpu_name:
            #     if gpu_available_alternate in gpu_check or gpu_available_alternate_2 in gpu_check or gpu_available_alternate_3 in gpu_check:
            #         #print(f"[{get_current_time()}] {gpu_name} in stock at Alternate")
            #         print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Alternate")
            #         requests.post(url, json={'text': gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
            #         if current_time - time_alternate >= 360:
            #             time_alternate = time.time()
            #             requests.post(url, json={'text':"#"}, timeout=10)
            #             chrome.open_new_tab(gpu_url)
                    
            #     else: 
            #         print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Alternate")
            
            elif "Mindfactory" in gpu_name:
                if gpu_availabe_mindfactory in gpu_check:
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Mindfactory")
                    requests.post(url, json={'text': gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
                    if current_time - time_mindfactory >= 360:
                        time_mindfactory = time.time()
                        requests.post(url, json={'text':"#"}, timeout=10)
                        chrome.open_new_tab(gpu_url)
                    
                else: 
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Mindfactory")
            
            elif "Galaxus" in gpu_name:
                if gpu_available_galaxus in gpu_check or gpu_available_galaxus_2 in gpu_check:
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Galaxus")
                    requests.post(url, json={'text': gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
                    if current_time - time_galaxus >= 360:
                        time_galaxus = time.time()
                        requests.post(url, json={'text':"#"}, timeout=10)
                        chrome.open_new_tab(gpu_url)
                    
                else: 
                    print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Galaxus")
              
        time.sleep(random.uniform(1, 3))           
        
except KeyboardInterrupt:
    print("Script interrupted. Closing browser...")
    driver.quit()
    

#         if "Amazon" in gpu_name:
# if "Wir bitten um Ihr Verständnis und wollen uns sicher sein dass Sie kein Bot sind." in gpu_check:
#     print("Bot protection")
# try:
#     product_container = driver.find_element(By.ID, 'ppd')  # Main product container
#     price_element = product_container.find_element(By.CLASS_NAME, 'a-price-whole')
#     if price_element:
#         price_str = price_element.text.strip()
#         price_str = price_str.replace('.', '').replace(',', '').replace('€', '')  
#         price = int(price_str)
#         if price < 4000:
#             print(f"[{get_current_time()}] {gpu_name}"+ Fore.GREEN + " in stock"+ Style.RESET_ALL + " at Amazon")
#             requests.post(url, json={'text': gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
#             if current_time - time_amazon >= 360:
#                 time_amazon = time.time()
#                 requests.post(url, json={'text':"#"}, timeout=10)
#                 chrome.open_new_tab(gpu_url)
#         else:
#             print(f"[{get_current_time()}] {gpu_name}"+ Fore.YELLOW + " 3rd party seller"+ Style.RESET_ALL + " at Amazon")
# except:
#     print(f"[{get_current_time()}] {gpu_name}"+ Fore.RED + " not in stock"+ Style.RESET_ALL + " at Amazon")


# if "Amazon" in gpu_name:
#     if gpu_not_availabe not in gpu_check:
#         if "Verkäufer\nWNR DIGITAL" not in gpu_check:
#             print(f"[{get_current_time()}] {gpu_name} in stock at Amazon")
#             requests.post(url, json={'text': gpu_name + " in stock" + "\n" + gpu_url}, timeout=10)
#             if current_time - time_amazon >= 360:
#                 time_amazon = time.time()
#                 requests.post(url, json={'text':"#"}, timeout=10)
#                 chrome.open_new_tab(gpu_url)
#         else:
#             print(f"[{get_current_time()}] {gpu_name} fuck this seller")
#     else:
#         print(f"[{get_current_time()}] {gpu_name} not in stock at Amazon")
            
            
# gpu_dict = {
#     "MSI Suprim 5090 (Amazon)": suprim_5090, 
#     "MSI Suprim Liquid 5090 (Amazon)": suprim_liquid_5090,
#     "MSI Gaming Trio 5090 (Amazon)": gaming_trio_5090,
#     "MSI Ventus 5090 (Amazon)": ventus_5090,
#     "ASUS Astral 5090 (Amazon)": astral_5090,
#     "PNY 5090 (Amazon)": pny_5090,
#     "Gigabyte Windforce 5090 (Alternate)": gigabyte_windforce_5090_a,
#     "Gigabyte Aorus Master 5090 (Alternate)": gigabyte_aorus_master_5090_a,
#     "Gigabyte Aorus Master Ice 5090 (Alternate)": gigabyte_ice_5090_a,
#     "Gigabyte Gaming OC 5090 (Alternate)": gigabyte_gaming_5090_a,
#     "MSI Suprim Liquid 5090 (Alternate)": suprim_liquid_5090_a,
#     "ASUS ROG Astral Liquid (Alternate)": rog_astral_lc_5090_a,
#     "Inno3d 5090 (Alternate)": inno3d_5090_a, 
#     "ASUS ROG Astral (Alternate)": rog_astral_5090_a, 
#     "Gainward Phantom 5090 (Alternate)": gainward_phantom_5090_a, 
#     "Zotac Solid 5090 (Alternate)": zotac_solid_5090_a, 
#     "ASUS TUF Gaming 5090 (Alternate)": asus_tuf_5090_a,
#     "ASUS TUF Gaming 5090 (Galaxus)": asus_tuf_5090_g,
#     "Palit Gamerock 5090 (Mindfactory)": palit_5090_m,
#     "Gigabyte Gaming OC 5090 (Mindfactory)": gigabyte_gaming_5090_m,
#     "Gigabyte Windforce 5090 (Mindfactory)": gigabyte_windforce_5090_m,
#     "Gigabyte Aorus Master 5090 (Mindfactory)": gigabyte_master_5090_m}

#amazon
# gpu_not_availabe = "Derzeit nicht verfügbar."
# suprim_5090 = "https://www.amazon.de/dp/B0DT6SN14V"
# suprim_liquid_5090 = "https://www.amazon.de/dp/B0BSN426TP"
# gaming_trio_5090 = "https://www.amazon.de/dp/B0DT6Q3BXM"
# ventus_5090 = "https://www.amazon.de/dp/B0DT6S77JK"
# astral_5090 = "https://www.amazon.de/dp/B0DTHV8THW"
# pny_5090 ="https://www.amazon.de/dp/B0DTJF8YT4"


# #mindfactory

# gpu_availabe_mindfactory = "In den Warenkorb"

# palit_5090_m = "https://www.mindfactory.de/product_info.php/pid/awin/32GB-Palit-GeForce-RTX-5090-GameRock-Aktiv-PCIe-5-0-x16-1xHDMI-2-1b-3xD_1611615.html"
# gigabyte_gaming_5090_m = "https://www.mindfactory.de/product_info.php/pid/awin/suggest/true/32GB-Gigabyte-GeForce-RTX-5090-Gaming-OC-Aktiv-PCIe-5-0-x16_1611048.html"
# gigabyte_windforce_5090_m = "https://www.mindfactory.de/product_info.php/pid/awin/32GB-Gigabyte-GeForce-RTX-5090-Windforce-OC-Aktiv-PCIe-5-0-x16-1xHDMI-2_1611049.html"
# gigabyte_master_5090_m = "https://www.mindfactory.de/product_info.php/pid/awin/32GB-Gigabyte-GeForce-RTX-5090-AORUS-Master-Aktiv-PCIe-5-0-x16-1xHDMI-2_1611047.html"

# #alternate


# inno3d_5090_a = "https://www.alternate.de/INNO3D/GeForce-RTX-5090-X3-Grafikkarte/html/product/100109380"
# gigabyte_gaming_5090_a = "https://www.alternate.de/GIGABYTE/GeForce-RTX-5090-GAMING-OC-32G-Grafikkarte/html/product/100108936"
# gigabyte_ice_5090_a = "https://www.alternate.de/GIGABYTE/GeForce-RTX-5090-AORUS-MASTER-ICE-32G-Grafikkarte/html/product/100108931"
# gigabyte_aorus_master_5090_a = "https://www.alternate.de/GIGABYTE/GeForce-RTX-5090-AORUS-MASTER-32G-Grafikkarte/html/product/100108932"
# gigabyte_windforce_5090_a = "https://www.alternate.de/GIGABYTE/GeForce-RTX-5090-WINDFORCE-OC-32G-Grafikkarte/html/product/100108938"
# suprim_liquid_5090_a = "https://www.alternate.de/MSI/GeForce-RTX-5090-32G-SUPRIM-LIQUID-SOC-Grafikkarte/html/product/100109560"
# rog_astral_lc_5090_a = "https://www.alternate.de/ASUS/GeForce-RTX-5090-ROG-ASTRAL-LC-GAMING-OC-Grafikkarte/html/product/100110137"
# rog_astral_5090_a ="https://www.alternate.de/ASUS/GeForce-RTX-5090-ROG-ASTRAL-GAMING-OC-Grafikkarte/html/product/100110139"
# gainward_phantom_5090_a = "https://www.alternate.de/Gainward/GeForce-RTX-5090-Phantom-Grafikkarte/html/product/100109795"
# zotac_solid_5090_a = "https://www.alternate.de/ZOTAC/GeForce-RTX-5090-SOLID-Grafikkarte/html/product/100110077"
# asus_tuf_5090_a = "https://www.alternate.de/ASUS/GeForce-RTX-5090-TUF-GAMING-Grafikkarte/html/product/100110148"

# # Galaxus

# gpu_galaxus_available = "geliefert"
# gpu_galaxus_available_2 = "Lager"

# asus_tuf_5090_g = "https://www.galaxus.de/de/s1/product/asus-tuf-rtx5090-32g-gaming-32-gb-grafikkarte-54200110"