
import argparse


_INDENT = 4 * ' '

_VAR_PB = 'pb'
_VAR_PPKG = 'protoPkg'

class GoFile(object):

    def __init__(self, imports=None):
        if imports is None:
            imports = []
        self.imports = sorted(imports)
        self.f = None

    def open(self):
        self.f = open('main.go', 'x')

    def close(self):
        self.f.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def write(self, string: str, indent=0):
        self.f.write(indent * _INDENT + string)

    def writeln(self, *args, indent=0):
        for arg in args:
            self.write(arg + '\n', indent=indent)

    def write_imports(self):
        self.writeln('\nimport (')
        self.writeln('"fmt"', indent=1)

        if len(self.imports) > 0:
            self.writeln()
            for i, path in enumerate(self.imports):
                self.writeln("%s%d %s" % (_VAR_PPKG, i, path), indent=1)
        self.writeln(')')

    def write_main(self):
        self.writeln('\nfunc main() {')

        self.writeln('fmt.Println("Hello World!")', indent=1)
        self.writeln()

        self.writeln('}')

    def generate(self):
        self.writeln('package main')

        self.write_imports()
        self.write_main()


def main():
    parser = argparse.ArgumentParser('go_writer')
    parser.add_argument('-i', '--imports', nargs='*')

    args = parser.parse_args()

    with GoFile(imports=args.imports) as go:
        go.generate()


if __name__ == '__main__':
    main()
