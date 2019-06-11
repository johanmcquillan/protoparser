
import argparse


_INDENT = '\t'

_VAR_PB = 'pb'
_VAR_PPKG = 'protopkg'

class GoFile(object):

    def __init__(self, proto_import):
        self.proto_import = proto_import
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
        if len(args) == 0:
            self.write('\n')
            return
        for arg in args:
            self.write(arg + '\n', indent=indent)

    def write_imports(self):
        self.writeln('\nimport (')
        self.writeln('"fmt"', indent=1)
        self.writeln('"os"', indent=1)
        self.writeln('"strings"', indent=1)

        self.writeln()
        self.writeln('"github.com/golang/protobuf/proto"', indent=1)

        self.writeln()
        self.writeln('%s "%s"' % (_VAR_PPKG, self.proto_import), indent=1)
        self.writeln(')')

    def write_main(self):
        self.writeln('\nfunc main() {')

        self.writeln('arg := []byte(strings.Join(os.Args[1:], ""))', indent=1)

        self.writeln(f'{_VAR_PB} := &{_VAR_PPKG}.Transaction{{}}', indent=1)
        self.writeln(f'if err := proto.Unmarshal(arg, {_VAR_PB}); err != nil {{', indent=1)
        self.writeln(f'panic(err)', indent=2)
        self.writeln('}', indent=1)





        self.writeln('}')

    def generate(self):
        self.writeln('package main')

        self.write_imports()
        self.write_main()


def main():
    parser = argparse.ArgumentParser('go_writer')
    parser.add_argument('-i', '--import', dest='proto_import', type=str, required=True)

    args = parser.parse_args()

    with GoFile(proto_import=args.proto_import) as go:
        go.generate()


if __name__ == '__main__':
    main()
