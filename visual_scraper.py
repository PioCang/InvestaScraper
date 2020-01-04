from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

BROWSER = webdriver.Firefox()

def build_master_list():
    MASTER_LIST_FILE = "PSEMasterlist.csv"
    master_list = []

    with open(MASTER_LIST_FILE, "r") as fp:
        for line in fp:
            master_list.append(line.rstrip())

    return master_list

def iterate_through(master_list):
    if len(master_list) < 1:
        raise Exception("The given master list is empty!")

    INVESTAGRAMS_URL = "https://www.investagrams.com/stock/"
    SLEEP_DURATION = 15

    for company in master_list:
        BROWSER.get(INVESTAGRAMS_URL + company)

        price_chart = BROWSER.find_element_by_id("ChartContent")
        BROWSER.execute_script("arguments[0].scrollIntoView();", price_chart)
        #input() # Pause after every company
        time.sleep(SLEEP_DURATION)
        open_tab_and_switch()

def open_tab_and_switch():
    BROWSER.execute_script("window.open()")
    BROWSER.switch_to.window(BROWSER.window_handles[-1])

if __name__ == "__main__":
    master_list = build_master_list()
    iterate_through(master_list)

