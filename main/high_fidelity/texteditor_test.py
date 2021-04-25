import unittest
from mock import Mock
from main.high_fidelity import textEditor

# print(textEditor.checksum("md5", "kash"))


class MyTestCase(unittest.TestCase):
    def test_wordcount(self):
        mock_file = Mock()
        textEditor.checksum(mock_file, "Hash")
        print(mock_file.mock_calls)


if __name__ == '__main__':
    unittest.main()
