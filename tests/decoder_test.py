
import os
import subprocess

import unittest

from proto.examples_pb2 import SimpleMessage


binary_path = 'decoders/simple_message_decoder'


class TestDecoder(unittest.TestCase):

    def setUp(self):
        self.assertTrue(os.path.isfile(binary_path))
        self.assertTrue(os.access(binary_path, os.X_OK))

        self.maxDiff = None

    def test_no_input(self):
        p = subprocess.run([binary_path], capture_output=True)
        self.assertEqual(0, p.returncode)
        self.assertEqual(b'{}', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_simple_input(self):
        msg = SimpleMessage(
            text='hello',
            small_int=1,
            big_int=2,
        ).SerializeToString()

        p = subprocess.run([binary_path], capture_output=True, input=msg)
        self.assertEqual(0, p.returncode)
        self.assertNotEqual(b'{}', p.stdout)
        self.assertEqual(b'', p.stderr)
