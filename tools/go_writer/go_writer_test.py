
import unittest

from tools.go_writer.decode import GoDecoder


test_data_path = 'tools/go_writer/test_data/decoder.go'


class MockFile(object):

    def __init__(self):
        self.text = ''

    def write(self, string):
        self.text += string


class TestGoDecoder(unittest.TestCase):

    def setUp(self):
        self.gofile = GoDecoder("github.com/johanmcquillan/protoparser/proto/examples", "SimpleMessage")
        self.gofile.f = MockFile()

        self.maxDiff = None

    def test_writes_correctly(self):

        with open(test_data_path) as test_file:
            test_data = test_file.read()

            self.gofile.generate()

            self.assertEqual(test_data, self.gofile.f.text)
