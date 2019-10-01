import unittest
import main
import os
from unittest.mock import patch

class TestMain(unittest.TestCase):

    def setUp(self):
        self.config_file = os.path.join(os.path.dirname(__file__), 'fixture/config.json')
        self.wox = main.Main(self.config_file)

    def test_get_config_from_file(self):
        expected = {'SyMenuRoot': 'p:\\software\\SyMenu', 'SoftwareRoot': 'p:\\software'}
        result = self.wox._get_config()

        self.assertDictEqual(expected, result)

    def test_get_config_fail(self):
        self.config_file = os.path.join(os.path.dirname(__file__), 'fixture/not_existing.json')

        with self.assertRaises(main.ConfigError) as ae:
            wox = main.Main(self.config_file)
            self.assertRegex(str(ae.exception), 'Cannot read config: \[Errno 2\] No such file or directory.*?')

if __name__ == '__main__':
    unittest.main()
