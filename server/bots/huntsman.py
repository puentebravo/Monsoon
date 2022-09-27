from selenium import webdriver
from dotenv import load_dotenv
import os
load_dotenv()

# port = 465
# destination = "https://www.newegg.com/p/2WK-0004-002X8?Description=xbox%20series%20x&cm_re=xbox_series%20x-_-2WK-0004-002X8-_-Product&quicklink=true"
# sender_email = os.getenv("LOGIN_EMAIL")
# auth = os.getenv("LOGIN_PASS")
# receiver_email = os.getenv("TARGET_EMAIL")
# message = """
# Subject: ---SCAN RESULTS---

# Scan complete. Item in stock at {}. Immediate acquisition recommended.

# """.format(destination)

path = os.getenv("EXE_PATH")

driver = webdriver.Chrome(executable_path=r"{}".format(path))

def Hunt(destination, sleep): 

    driver.get(destination)

    target = driver.find_element_by_tag_name("body")

    tarString = target.text

    if (tarString.find("In stock.")):
        driver.close()
        return "Item in stock at: {}. Immediate acquisition recommended.".format(destination)
    
    else:
        driver.close()
        return "Item not in stock. Retrying in {} seconds".format(sleep)
    
    