# functions for SDO
import json


def list_blocked(elements):
    list_blocked_access = []

    for i in range(len(elements)):
        list_blocked_access.append(i)

    return list_blocked_access


def list_access(elements_access):
    list_tasks_access = []

    for len_task in range(len(elements_access)):
        list_tasks_access.append(len_task)

    return list_tasks_access


def test_elements_on_block(blocked_elements, access_elements):
    list_elements_new = []

    for elements_access in range(len(access_elements)):
        for elements_blocked in range(len(blocked_elements)):
            if elements_access == elements_blocked:
                list_elements_new.append(elements_blocked)
    return max(list_elements_new) if list_elements_new else 0


def path_to_save_file(filename, path, quest):
    with open(path + '\\' + filename, 'w', encoding='utf-8') as question:
        question.write(quest)


def read_file(path, filename):
    with open(path + '\\' + filename, 'r', encoding='utf-8') as read:
        return read.read()


def clear_file(path, filename):
    open(path + '\\' + filename, 'w').close()


def validation_answer(answer):
    return answer.lower()


def last_page_task(pages):
    list_pages = []

    for number_page in pages:
        list_pages.append(number_page)

    if list_pages:
        if list_pages[-2] == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
            return int(list_pages[-2] + list_pages[-1])
        elif list_pages[-1]:
            return int(list_pages[-1])


def json_load(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        exceptions = json.load(f)
        return exceptions


def json_save(list_except, filename):
    with open(filename, 'w', encoding='utf-8') as j:
        json.dump(list_except, j, ensure_ascii=False)


def answer_out(question):
    list_questions = json_load('data.json')

    # переопределение / убераем в конце строки пробелы
    question = question.rstrip()

    if list_questions[question]:
        return list_questions[question]
    else:
        return list_questions[question.capitalize()]


def response_true(element, resp_text, question):
    # переопределение resp_test в нижний регистр
    resp_text = resp_text.lower().rstrip()

    # Создаём список для element's в нижнем регистре
    elements_lower = []

    # проходим по каждому элементу и делаем ему нижний регистр
    for j in range(len(element)):
        elements_lower.append(element[j].lower().rstrip())

    # проходим по каждому элементу и сравневаем их с ответом

    if resp_text in elements_lower:
        return elements_lower.index(resp_text)
    else:
        answers = answer_out(question)
        if type(answers) == str:
            return elements_lower.index(answers)
        else:
            answer_list = [elements_lower.index(answers[0]), elements_lower.index(answers[1])]
            return answer_list
