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
    return max(list_elements_new) if list_elements_new else None


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

    if list_questions[question]:
        return list_questions[question]
    else:
        return list_questions[question.capitalize()]

    # print(question)
    #
    # list_words_question = question.split(' ')
    #
    # first_words_questions = list_words_question[0] + ' ' + list_words_question[1] + ' ' + list_words_question[2]
    # last_words_questions = list_words_question[-1] + ' ' + list_words_question[-2] + ' ' + list_words_question[-3]
    #
    # answer_true = []
    #
    # for u in list_questions:
    #     list_words_answer = u.split(' ')
    #     first_words_answer = list_words_answer[0] + ' ' + list_words_answer[1] + ' ' + list_words_question[2]
    #     if first_words_questions == first_words_answer:
    #         answer_true.append(list_questions[u])
    #     elif first_words_questions == first_words_answer:
    #         answer_true.append(validation_answer(list_questions[u]))
    #     elif first_words_questions != first_words_answer:
    #         last_words_answer = list_words_answer[-1] + ' ' + list_words_answer[-2] + ' ' + list_words_question[-3]
    #         if last_words_questions == last_words_answer:
    #             answer_true.append(list_questions[u])
    #         elif last_words_questions == last_words_answer:
    #             answer_true.append(validation_answer(list_questions[u]))
    #     else:
    #         return 'Error: ошибка при первом сравнении слов'
    # return answer_true[0]


# array_answers = ['Python', 'C++', 'Perl', 'Ruby', 'оба варианта верны']
# response = 'Оба варианта верны'
# question = 'К чему может привести нарушение нормальной величины зазоров и взаимного расположения стыков?'

# print(answer_out(question))


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
        if len(answers) == 1:
            answer_list = [elements_lower.index(answers[0]), elements_lower.index(answers[1])]
            return answer_list
        elif len(answers) == 0:
            return elements_lower.index(answers[0])
        else:
            first_index = elements_lower.index(answers[0])
            two_index = elements_lower.index(answers[1])
            return first_index, two_index

    # for k in range(len(elements_lower)):
    #     if elements_lower[k] == resp_text:
    #         return elements_lower.index(resp_text)
    #     elif elements_lower[k] != resp_text:
    #         answers = answer_out(question)
    #         if len(answers) == 1:
    #             answer_list = [elements_lower.index(answers[0].lower()), elements_lower.index(answers[1].lower())]
    #             return answer_list
    #         else:
    #             return elements_lower.index(answers[0].lower())