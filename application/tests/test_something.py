import unittest

def get_long_string(number, word):
    lastletter = word[-1]
    for x in range(number):
        word += lastletter
    return word


class TestJournalMethod(unittest.TestCase):
    def test_get_long_string(self):
        #Arrange
        word = 'hello'
        number = -5
        expected_response = 'hello'

        #Act
        response = get_long_string(number, word)

        #Assert
        self.assertEqual(response, expected_response)
        # self.assertTrue(len(response) > len(word))
        self.assertEqual(len(response), len(word) + number)


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
