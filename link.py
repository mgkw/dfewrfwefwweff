import time
from threading import Thread
import random
import os
import requests
from selenium import webdriver
from user_agent import generate_user_agent
from selenium.webdriver.common.proxy import Proxy, ProxyType


# browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=browseres)


def get_proxies():
    lsis_url = ["https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
                "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
                "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
                "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
                "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
                "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
                "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
                "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt",
                ]

    gut = random.choice(lsis_url)
    raw_proxy_list = requests.get(gut).text
    refined_proxy_list = []
    for proxy_line in raw_proxy_list.splitlines():
        # ip, port = proxy_line.split(":")
        # protocol_guess = "https" if port == "443" else "http"
        refined_proxy_list.append(proxy_line)
    return random.choice(refined_proxy_list)


n = 0

while True:
    n += 1



    try:
        prk = get_proxies()
        #
        # prox = Proxy()
        # prox.proxy_type = ProxyType.MANUAL
        #
        # # Proxy IP & Port
        # prox.http_proxy = "{}".format(random.choice(prk))

        # browseres.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        # browseres.add_argument("--disable-dev-shm-usage")
        # browseres.add_argument("--no-sandbox")
        # browseres.add_argument("--incognito")
        # browseres.add_argument("--disable-site-isolation-trials")
        # browseres.add_argument("--headless")
        # browseres.add_argument("user-agent={}".format(str(generate_user_agent())))
        # # browseres.add_argument('--proxy-server=%s' % prk)
        # browseres.add_argument("ignore-certificate-errors")


        # capabilities = webdriver.DesiredCapabilities.CHROME
        # prox.add_to_capabilities(capabilities)
        #

        # # browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=browseres)
        # browser = webdriver.Chrome(executable_path="chromedriver.exe", options=browseres)
        # # browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=browseres)
        #

        browseres = webdriver.ChromeOptions()
        # browseres.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        # browseres.add_argument("--disable-dev-shm-usage")
        # browseres.add_argument("--no-sandbox")
        # browseres.add_argument("--incognito")
        # browseres.add_argument("--disable-site-isolation-trials")
        browseres.add_argument("--enable-notifications")
        prefs = {"profile.default_content_setting_values.notifications": 1}
        browseres.add_experimental_option("prefs", prefs)
        # browseres.add_argument("--headless")
        browseres.add_argument("user-agent={}".format(str(generate_user_agent())))
        # browseres.add_argument('--proxy-server=%s' % prk)
        # browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=browseres)
        browser = webdriver.Chrome(executable_path="chromedriver.exe", options=browseres)

        print(n, browseres.arguments)


        browser.get('https://615528.click-allow.top/?v=1')

        time.sleep(10)
        browser.refresh()
        # m = browser.find_element_by_xpath('//*[@id="zJdJSaE7yk4v"]').click()
        # time.sleep(5)
        # print(m)
        # browser.switch_to.window(browser.window_handles[1])
        # browser.close()
        # browser.switch_to.window(browser.window_handles[0])
        # browser.close()
        # time.sleep(1000)
        browser.quit()






    except Exception as e:
        print(e)
        continue
