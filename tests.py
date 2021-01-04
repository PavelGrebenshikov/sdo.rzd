import unittest
import functions


class FunctionsTestCase(unittest.TestCase):
    """ Юнит Тесты для функций """

    def test_list_blocked(self):
        """ Тестирование на заполенине списка длиной от первого до последнего элемента в списке """
        array = ['Python', 'C++', 'PHP', 'Ruby', 'C', 'Perl']
        elements_len = functions.list_blocked(array)
        self.assertEqual(len(elements_len), len(array))

    def test_list_access(self):
        """ Тестирование на заполенине списка длиной от первого до последнего элемента в списке """
        array = ['Testing', 'template', 'Root', 'User']
        elements_len = functions.list_blocked(array)
        self.assertEqual(len(elements_len), len(array))

    def test_elements_on_block(self):
        """ Сравнение двух списков на длину """
        array_1 = ['User', 'Root', 'No']
        array_2 = ['User', 'History', 'Dog']
        max_length = functions.test_elements_on_block(array_1, array_2)
        self.assertEqual(max_length, 2)

    def test_read_file(self):
        """ Тестирование на прочтение файла """
        """ Path необходимо указать полный путь к файлу """
        read_file = functions.read_file('D:\\Code\\sdo.rzd', 'correct_answer.txt')
        self.assertTrue(read_file)

    def test_validation_answer(self):
        """ Мелкое тестирование букв на нижний регистр """
        lower_word = functions.validation_answer('PYtHon')
        self.assertEqual(lower_word, 'python')

    def test_last_page_task(self):
        """ Тестирование на определения количество страниц """
        page = "Page 3 of 14"
        last_page = functions.last_page_task(page)
        self.assertEqual(last_page, 14)


    def test_answer_out(self):
        """ Тестирование на поиск вопроса в файле json, провека 3х начальных букв и 3х последних"""
        """ Сюда попадает вопрос """
        questions = "С применением какого прибора производят регулировку и разгонку зазоров?"
        answer_out = functions.answer_out(questions)
        self.assertEqual(answer_out, "гидравлического разгонщика")


    def test_response_true(self):
        """ Тестирование на верность ответа """
        """ Questions = None, т.к вопрос берется из браузера """
        """ Если ответ не совпадает с списков ответов, то аргумент questions ищет ответ в файле json """
        array_answers = ['Python', 'C++', 'Perl', 'Ruby', 'GO']
        response = 'Python'
        answer = functions.response_true(array_answers, response, None)
        self.assertEqual(answer, 0)


if __name__ == '__main__':
    app = FunctionsTestCase(unittest.TestCase)
