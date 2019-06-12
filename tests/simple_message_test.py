
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
        p = assert_executes_successfully(self, binary_path)
        self.assertEqual(b'', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_empty_message(self):
        msg = SimpleMessage().SerializeToString()

        p = assert_executes_successfully(self, binary_path, stdin=msg)
        self.assertNotEqual(b'{}', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_string_message(self):
        msg = SimpleMessage(
            text='hello',
        ).SerializeToString()

        p = assert_executes_successfully(self, binary_path, stdin=msg)
        self.assertNotEqual(b'{}', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_int32_message(self):
        msg = SimpleMessage(
            small_int=100,
        ).SerializeToString()

        p = assert_executes_successfully(self, binary_path, stdin=msg)
        self.assertEqual(b'{"small_int":100}', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_int64_message(self):
        msg = SimpleMessage(
            big_int=999,
        ).SerializeToString()

        p = assert_executes_successfully(self, binary_path, stdin=msg)
        self.assertEqual(b'{"big_int":"999"}', p.stdout)
        self.assertEqual(b'', p.stderr)

    def test_simple_message(self):
        msg = SimpleMessage(
            small_int=123,
            big_int=456,
            text='goodbye',
        ).SerializeToString()

        p = assert_executes_successfully(self, binary_path, stdin=msg)
        self.assertEqual(b'{"small_int":123,"big_int":"456","text":"goodbye"}', p.stdout)
        self.assertEqual(b'', p.stderr)


def assert_executes_successfully(
        test: TestDecoder, path: str, stdin=None, orig_name=True, enums=False, defaults=False, indent='',
) -> subprocess.CompletedProcess:

    args = []
    if orig_name:
        args.append('-o')
    if enums:
        args.append('-e')
    if indent != '':
        args.append('-i=' + indent)
    if defaults:
        args.append('-d')

    cmd = [path]
    if len(args) > 0:
        cmd.append(' '.join(args))

    p = subprocess.run(cmd, capture_output=True, input=stdin)
    test.assertEqual(
        0, p.returncode,
        msg=f'process failed with code {p.returncode};\nstderr: {p.stderr}'
    )

    return p
