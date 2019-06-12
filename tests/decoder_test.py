
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
        p = assertExecutesSuccessfully(self, binary_path)
        self.assertEqual(b'', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_empty_message(self):
        msg = SimpleMessage().SerializeToString()

        p = assertExecutesSuccessfully(self, binary_path, stdin=msg)
        self.assertNotEqual(b'{}', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_string_message(self):
        msg = SimpleMessage(
            text='hello',
        ).SerializeToString()

        p = assertExecutesSuccessfully(self, binary_path, stdin=msg)
        self.assertNotEqual(b'{}', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_int32_message(self):
        msg = SimpleMessage(
            small_int=100,
        ).SerializeToString()

        p = assertExecutesSuccessfully(self, binary_path, stdin=msg)
        self.assertEqual(b'{"small_int":100}', p.stdout)
        self.assertEqual(b'', p.stderr)


def assertExecutesSuccessfully(test: TestDecoder, path: str, stdin=None) -> subprocess.CompletedProcess:
        p = subprocess.run([path], capture_output=True, input=stdin)
        test.assertEqual(
            0, p.returncode,
            msg=f'process failed with code {p.returncode};\nstderr: {p.stderr}'
        )
        return p
