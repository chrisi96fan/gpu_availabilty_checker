# gpu_availabilty_checker

This is a small script that checks the availability of certain products, specifically RTX 5090 GPUs, using browser automation with the Selenium library. 

When a product becomes available, it sends a notification via Telegram. 

For the store Alternate, the script can automatically add the product to the shopping cart and extract a specific cookie to reserve the item.


#Requirements:

1. The required Python libraries are listed in the requirements.txt file. You can install them with:

pip install -r requirements.txt

2. Download and install the most recent chromedriver.exe from https://googlechromelabs.github.io/chrome-for-testing/ and extract it to the chrome.exe location.


#Setup

1. Set the required parameters such as paths to both chrome.exe and chromedriver.exe and bot_token and chat_id for Telegram notifications in gpu_availability_checker.

2. Compile the script with running the following command in the folder where you cloned the repository.

pyinstaller gpu_availability_checker.py 


Note: I haven’t updated or tested the script since March 2025, so functionality is not guaranteed.
