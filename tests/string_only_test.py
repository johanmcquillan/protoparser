
import os

import unittest

from tests.test_utils import assert_executes_successfully
from proto.examples_pb2 import StringOnly


binary_path = 'parsers/string_only_decoder'


class TestStringOnly(unittest.TestCase):

    def setUp(self):
        self.assertTrue(os.path.isfile(binary_path))
        self.assertTrue(os.access(binary_path, os.X_OK))

        self.maxDiff = None

    def test_no_input(self):
        p = assert_executes_successfully(self, binary_path)
        self.assertEqual(b'', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_empty_message(self):
        msg = StringOnly().SerializeToString()

        p = assert_executes_successfully(self, binary_path, stdin=msg)
        self.assertNotEqual(b'{}', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_message(self):
        msg = StringOnly(
            text='hello',
        ).SerializeToString()

        p = assert_executes_successfully(self, binary_path, stdin=msg)
        self.assertNotEqual(b'{}', p.stdout)
        self.assertEqual(b'', p.stderr)
