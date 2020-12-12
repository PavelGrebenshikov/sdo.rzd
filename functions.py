# functions for SDO


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
    return max(list_elements_new)


def path_to_save_file(filename, path, quest):
    with open(path + '\\' + filename, 'w', encoding='utf-8') as question:
        question.write(quest + '\n')


def read_file(path, filename):
    with open(path + '\\' + filename, 'r', encoding='utf-8') as read:
        return read.read()


def clear_file(path, filename):
    open(path + '\\' + filename, 'w').close()


def response_true(element, resp_text):
    resp_text.replace('\n', '').replace(',', '').replace('.', '') \
        .replace('–', '').replace('(', '').replace(')', '').replace('«', '').replace('»', '').replace(':', '') \
        .replace(';', '')

    print(element)
    print('Ответ: ' + resp_text)

    return element.index(resp_text)


def last_page_task(pages):
    list_pages = []

    for number_page in pages:
        list_pages.append(number_page)

    if list_pages:
        if list_pages[-2] == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
            return int(list_pages[-2] + list_pages[-1])
        elif list_pages[-1]:
            return int(list_pages[-1])


def read_exceptions_response(questions):
    list_exceptions_questions = {
        'На какую высоту необходимо произвести подъем груза после зацепки, чтобы убедиться в надежности зацепки'
        'и дальнейшего подъема и перемещение груза?': 'На высоту 200-300 мм',
        'Работа крана должна вестись под руководством:': 'Дорожного мастера или бригадира пути, назначенного приказом '
                                                         'по предприятию ответственным за безопасное производство '
                                                         'работ кранами',
        'Передвижение дрезин с грузом на крюке крана разрешается при скорости?': 'не более 5 км/ч',
    }

    for k, v in list_exceptions_questions.items():
        if k == questions:
            return v.replace(',', '').lower().replace('\n', '') \
                .replace(',', '').replace('.', '').replace('–', '').replace('(', '') \
                .replace(')', '').replace('«', '').replace('»', '').replace(':', '') \
                .replace(';', '')

    ans = read_file('D:\\Code\\sdo.rzd', 'correct_ans.txt')
    return ans.replace(',', '').lower().replace('\n', '') \
        .replace(',', '').replace('.', '').replace('–', '').replace('(', '') \
        .replace(')', '').replace('«', '').replace('»', '').replace(':', '') \
        .replace(';', '')
