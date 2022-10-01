from selenium import webdriver
# from dotenv import load_dotenv
# import os
# load_dotenv()

# # port = 465
# # destination = "https://www.newegg.com/p/2WK-0004-002X8?Description=xbox%20series%20x&cm_re=xbox_series%20x-_-2WK-0004-002X8-_-Product&quicklink=true"
# # sender_email = os.getenv("LOGIN_EMAIL")
# # auth = os.getenv("LOGIN_PASS")
# # receiver_email = os.getenv("TARGET_EMAIL")
# # message = """
# # Subject: ---SCAN RESULTS---

# # Scan complete. Item in stock at {}. Immediate acquisition recommended.

# # """.format(destination)

# path = os.getenv("EXE_PATH")

# driver = webdriver.Chrome(executable_path=r"{}".format(path))

# def Hunt(destination): 

#     driver.get(destination)

#     target = driver.find_element_by_tag_name("body")

#     tarString = target.text

#     if (tarString.find("In stock.")):
#         driver.close()
#         return "Item in stock at: {}! Immediate acquisition recommended.".format(destination)
    
#     else:
#         driver.close()
    
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}

def hunt(destination):
    if __name__ == "__main__":
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(destination)

        target = driver.find_element_by_tag_name("body")

        tarString = target.text

        if (tarString.find("In stock.")):
            return "Item in stock at: {}! Immediate acquisition recommended.".format(destination)

        driver.close()


hunt("https://www.amazon.com/Christmas-Decoration-Waterproof-Transformer-Extendable/dp/B07TWC328L/ref=sr_1_59?crid=1TDXEHCJLHRS7&keywords=christmas%2Blights&qid=1664668117&qu=eyJxc2MiOiI4Ljg2IiwicXNhIjoiOC4zNSIsInFzcCI6IjcuOTIifQ%3D%3D&sprefix=%2Caps%2C49&sr=8-59&th=1")