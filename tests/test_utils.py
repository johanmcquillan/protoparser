
import unittest
import subprocess

def assert_executes_successfully(
        test: unittest.TestCase, path: str, stdin=None, orig_name=True, enums=False, defaults=False, indent='',
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
