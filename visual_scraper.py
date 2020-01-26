from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import time

BROWSER = webdriver.Firefox()

def build_master_list(ticker_file):
    master_list = []

    with open(ticker_file, "r") as fp:
        for line in fp:
            master_list.append(line.rstrip())

    return sorted(master_list)

def iterate_through(master_list):
    if len(master_list) < 1:
        raise Exception("The given master list is empty!")

    INVESTAGRAMS_URL = "https://www.investagrams.com/stock/"
    SLEEP_DURATION = 3
    links_generated = 0

    for company in master_list:
        BROWSER.get(INVESTAGRAMS_URL + company)

        price_chart = BROWSER.find_element_by_id("ChartContent")
        BROWSER.execute_script("arguments[0].scrollIntoView();", price_chart)

        time.sleep(SLEEP_DURATION)

        links_generated += 1
        if links_generated % 10 == 0:
            print("{} links generated.".format(links_generated)
                + " Stopping at {}.".format(company)
                + " Press Enter to continue...", end='')
            input()

        open_tab_and_switch()

def open_tab_and_switch():
    BROWSER.execute_script("window.open()")
    BROWSER.switch_to.window(BROWSER.window_handles[-1])

def get_starting_point():
    print("Provide ticker of starting point (Press Enter to skip)\n> ", end='')
    response = input()
    return response

def jump_to(master_list, starting_point=None):
    if not starting_point:
        return master_list

    if starting_point not in master_list:
        raise Exception("That ticker is not in the master list.")

    return master_list[master_list.index(starting_point):]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "ticker_file",
        nargs="?",
        default="PSEMasterlist.csv",
        help="Newline-separated file of ticker symbols."
    )
    return parser.parse_args().ticker_file

if __name__ == "__main__":
    ticker_file = parse_args()
    master_list = build_master_list(ticker_file)
    starting_point = get_starting_point()
    master_list = jump_to(master_list, starting_point)
    iterate_through(master_list)

