import unittest
import symenu
import os

class TestSymenu(unittest.TestCase):

    def setUp(self):
        items = os.path.join(os.path.dirname(__file__), 'fixture')
        self.symenu = symenu.SyMenu(items, 'p:\\software')

    def test_query(self):

        expected = [{'SubTitle': 'p:\\software\\Atom\\app\\atom.exe',
                    'JsonRPCAction': {'parameters': ['p:\\software\\Atom\\app\\atom.exe'],
                    'method': 'open_process'},
                    'IcoPath': 'p:\\software\\SyMenu\\Icons\\atom.exe_1.ico',
                    'Title': 'Atom'}]

        result = self.symenu.find_items("Atom")

        self.assertListEqual(expected, result)

    def test_query_empty(self):

        expected = []

        result = self.symenu.find_items('Something else')
        self.assertListEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
