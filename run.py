import os, time, sys
from selenium import webdriver


def login(user, passwd):
    browser = webdriver.Chrome(os.path.join(os.path.dirname(__file__), "chromedriver.exe"))
    browser.get("https://vpn.phytium.com.cn:4433/")
    browser.find_element_by_css_selector('#svpn_name').send_keys(user)
    browser.find_element_by_css_selector('#svpn_password').send_keys(passwd)
    browser.find_element_by_css_selector('#logButton').click()

    time.sleep(15)

    browser.quit()


if __name__ == '__main__':
    login(sys.argv[1], sys.argv[2])
