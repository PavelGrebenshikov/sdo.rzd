from selenium import webdriver
from functions import read_file, path_to_save_file
from time import sleep


def main_answer():
    user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko)' \
                 'Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30'

    option = webdriver.ChromeOptions()
    option.set_capability('dom.webdriver.enabled', False)
    option.set_capability('dom.webnotifications.enabled', False)
    option.set_capability('media.volume_scale', '0.0')
    option.set_capability('general.useragent.override', user_agent)

    browser = webdriver.Chrome(options=option)
    browser.get('https://rwlib.net/sdo')

    sleep(3)
    question = read_file('D:\\Code\\sdo.rzd', 'question.txt')

    browser.find_element_by_name('s').send_keys(question)

    sleep(3)
    browser.find_element_by_id('s-send').click()

    sleep(3)
    answer = browser.find_elements_by_class_name('sdo')

    answer[1].click()

    sleep(3)
    correct_ans = browser.find_element_by_class_name('select').text

    path_to_save_file('correct_answer.txt', 'D:\\Code\\sdo.rzd', correct_ans)

    browser.close()
