
import unittest

from tools.go_writer.go_writer import GoFile


class MockFile(object):

    def __init__(self):
        self.text = ''

    def write(self, string):
        self.text += string


class TestGoWriter(unittest.TestCase):

    def setUp(self):
        self.gofile = GoFile("github.com/johanmcquillan/protoparser/proto/finance", "Transaction")
        self.gofile.f = MockFile()

        self.maxDiff = None

    def test_empty(self):
        test_data_path = 'tools/go_writer/test_data/empty.go'

        with open(test_data_path) as test_file:
            test_data = test_file.read()

            self.gofile.generate()

            self.assertEqual(test_data, self.gofile.f.text)
