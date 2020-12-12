import time
import functions
from selenium import webdriver
from answers import main_answer


def main():

    user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko)' \
                 'Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30'

    option = webdriver.ChromeOptions()
    option.set_capability('dom.webdriver.enabled', False)
    option.set_capability('dom.webnotifications.enabled', False)
    option.set_capability('media.volume_scale', '0.0')
    option.set_capability('general.useragent.override', user_agent)

    browser = webdriver.Chrome(options=option)
    browser.get('https://sdo.rzd.ru/lms/Do?doaction=Go&s=gEFRWuqMwUTCcqxARPgv&id=0&type=customloginpage')

    xpath_login = '/html/body/div/div[1]/div/div/div/div[2]/form/table[1]/tbody/tr[1]/td[2]/input'
    xpath_password = '/html/body/div/div[1]/div/div/div/div[2]/form/table[1]/tbody/tr[2]/td[2]/div/input'
    xpath_button = '/html/body/div/div[1]/div/div/div/div[2]/form/button'

    login = ''
    password = ''

    # Login In
    login_user = login  # input('Введите логин: ')
    password_user = password  # input('Введите пароль: ')

    if login_user and password_user:
        browser.find_element_by_xpath(xpath_login).send_keys(login_user)
        browser.find_element_by_xpath(xpath_password).send_keys(password_user)
        browser.find_element_by_xpath(xpath_button).click()
    else:
        return

    # Head page
    xpath_my_training = '/html/body/div[1]/div/div/table/tbody/tr[2]/td[1]' \
                        '/div/div/div[2]/div/div/div/div/ul/li[2]/div/a'

    # this pause 5 second maybe
    time.sleep(5)
    browser.find_element_by_xpath(xpath_my_training).click()

    # My training page
    filter_tables = '/html/body/div[1]/div/div/table/tbody/tr[2]/td[2]/div/div/div[2]/div[4]/div/div[2]/div/div' \
                    '/div[2]/div/table/tbody/tr/td/div/div/div/div[2]/div/div/div[1]/span/div/span[3]/ul/li[1]'

    # pause 5 seconds for refresh page
    time.sleep(5)
    browser.find_element_by_xpath(filter_tables).click()

    # this pause 5 second maybe
    time.sleep(10)

    # numbers all tasks SDO
    class_tasks = 'mira-grid-column-autonumber'
    class_block = 'mira-grid-cell-image'
    numbers = browser.find_elements_by_class_name(class_tasks)
    blocked_task = browser.find_elements_by_class_name(class_block)

    # functions from module 'functions.py'
    begin_element = functions.test_elements_on_block(numbers, blocked_task)
    first_element = begin_element + 1

    class_elements_run = 'mira-grid-cell-operation'

    # pause 5 seconds for load page
    time.sleep(10)
    section = browser.find_elements_by_class_name(class_elements_run)

    # click on section
    section[first_element].click()

    # pause 5 seconds
    time.sleep(5)

    class_button_task = 'mira-button'
    last_task_button = browser.find_elements_by_class_name(class_button_task)
    last_task_button[-1].click()

    # pause 5 seconds
    time.sleep(15)

    # transition window and iframe
    browser.switch_to.window(browser.window_handles[1])
    browser.switch_to.frame('Content')

    # if there are pages, then we determine their quantity
    last_page = browser.find_element_by_class_name('slides').text
    next_button = browser.find_elements_by_class_name('component_base')
    number_of_page = functions.last_page_task(last_page)

    if number_of_page:
        count = 0
        number_of_page = number_of_page - 1
        while 0 < number_of_page:
            next_button[-1].click()
            time.sleep(3)
            count += 1
            if count == number_of_page:
                break

        while True:
            # work with iframe in new window
            # xpath_span_text = '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/div[25]' \
            #                  '/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/p/span'
            # xpath_span_one = '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/div[24]/div/' \
            #                 'div[2]/div/div/div[3]/div/div[1]/div/div[1]/p/span'

            span_question = browser.find_elements_by_tag_name('span')

            save_text = str(span_question[0].text)

            functions.path_to_save_file('question.txt', 'D:\\Code\\sdo.rzd', save_text)

            # Start code answers future

            main_answer()

            # Up code answers future
            response_text = functions.read_file('D:\\Code\\sdo.rzd', 'correct_answer.txt')

            # call function exceptions
            response_text = functions.read_exceptions_response(questions=save_text)

            # answers to sdo.rzd
            elements_answers = browser.find_elements_by_tag_name('span')

            list_elements_answers = []
            for el_ans in elements_answers:
                list_elements_answers.append(str(el_ans.text).replace(',', '').lower().replace('\n', '')\
                                             .replace(',', '').replace('.', '').replace('–', '').replace('(', '')\
                                             .replace(')', '').replace('«', '').replace('»', '').replace(':', '')\
                                             .replace(';', ''))
            list_elements_answers.pop(0)

            # Index of the correct response input
            index = functions.response_true(list_elements_answers, response_text.lower())

            # click of input
            elements_check_inputs = browser.find_elements_by_class_name('fill')
            elements_check_inputs.pop(0)
            elements_check_inputs[index].click()

            answer_page = browser.find_elements_by_class_name('show_slides')
            text_answer_page = answer_page[1].text

            answer_next_button = browser.find_elements_by_class_name('next')
            answer_next_button[1].click()

            # if finish off
            if text_answer_page:
                if int(text_answer_page[-7] + text_answer_page[-6]) >= 10:
                    count_page = int(text_answer_page[-7] + text_answer_page[-6])
                    # pause
                    count_finish_page = count_page + 1
                    if count_finish_page >= 11:
                        finish_button = browser.find_elements_by_class_name('finish')
                        finish_button[0].click()
                        time.sleep(5)
                        finish_btn = browser.find_elements_by_tag_name('button')
                        finish_btn[14].click()

                elif int(text_answer_page[-6]) == 5:
                    count_page = int(text_answer_page[-7] + text_answer_page[-6])
                    # pause
                    count_finish_page = count_page + 1
                    if count_finish_page >= 6:
                        finish_button = browser.find_elements_by_class_name('finish')
                        finish_button[0].click()
                        time.sleep(5)

                        finish_btn = browser.find_elements_by_tag_name('button')
                        finish_btn[14].click()

                        browser.close()
                        break

    # function for determining the response
    functions.clear_file('D:\\Code\\PassageSDO', 'correct_answer.txt')
    functions.clear_file('D:\\Code\\PassageSDO', 'question.txt')

    main()


if __name__ == '__main__':
    main()
