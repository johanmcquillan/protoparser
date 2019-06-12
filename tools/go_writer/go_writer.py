
import argparse


_INDENT = '\t'

_VAR_PB = 'pb'
_VAR_PPKG = 'protopkg'

_IMPORTS_STD = [
    'bufio',
    'os',
]
_IMPORTS_3RD_PARTY = [
    'github.com/golang/protobuf/jsonpb',
    'github.com/golang/protobuf/proto',
    'github.com/jessevdk/go-flags',
]

class GoFile(object):

    def __init__(self, proto_import, proto_message):
        self.proto_import = proto_import
        self.proto_message = proto_message
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
        self.writeln('import (')

        for i in sorted(_IMPORTS_STD):
            self.writeln(f'"{i}"', indent=1)
        self.writeln()

        for i in sorted(_IMPORTS_3RD_PARTY):
            self.writeln(f'"{i}"', indent=1)
        self.writeln()

        self.writeln(f'{_VAR_PPKG} "{self.proto_import}"', indent=1)
        self.writeln(')')

    def write_opts(self):
        self.writeln('type Opts struct {')
        self.writeln('EnumsAsInts  bool   `short:"e" long:"enums" description:"Whether to render enum values as integers, as opposed to string values"`', indent=1)
        self.writeln('EmitDefaults bool   `short:"d" long:"defaults" description:"Whether to render fields with zero values"`', indent=1)
        self.writeln('Indent       string `short:"i" long:"indent" description:"A string to indent each level by"`', indent=1)
        self.writeln('OrigName     bool   `short:"o" long:"original" description:"Whether to use the original (.proto) name for fields"`', indent=1)
        self.writeln('}')

    def write_main(self):
        self.writeln('func main() {')

        self.writeln('opts := &Opts{}', indent=1)
        self.writeln('if _, err := flags.Parse(opts); err != nil {', indent=1)
        self.writeln('panic(err)', indent=2)
        self.writeln('}', indent=1)
        self.writeln()

        self.writeln('marshaller := &jsonpb.Marshaler{', indent=1)
        self.writeln('EnumsAsInts:  opts.EnumsAsInts,', indent=2)
        self.writeln('EmitDefaults: opts.EmitDefaults,', indent=2)
        self.writeln('OrigName:     opts.OrigName,', indent=2)
        self.writeln('Indent:       opts.Indent,', indent=2)
        self.writeln('}', indent=1)
        self.writeln()

        self.writeln('scanner := bufio.NewScanner(os.Stdin)', indent=1)
        self.writeln('for scanner.Scan() {', indent=1)
        self.writeln('msg := scanner.Bytes()', indent=2)
        self.writeln(f'{_VAR_PB} := &{_VAR_PPKG}.{self.proto_message}{{}}', indent=2)
        self.writeln(f'if err := proto.Unmarshal(msg, {_VAR_PB}); err != nil {{', indent=2)
        self.writeln(f'panic(err)', indent=3)
        self.writeln('}', indent=2)

        self.writeln(f'marshaller.Marshal(os.Stdout, {_VAR_PB})', indent=2)
        self.writeln('}', indent=1)
        self.writeln('}')

    def generate(self):
        self.writeln('package main')
        self.writeln()

        self.write_imports()
        self.writeln()

        self.write_opts()
        self.writeln()

        self.write_main()


def main():
    parser = argparse.ArgumentParser('go_writer')
    parser.add_argument('-i', '--import', dest='proto_import', type=str, required=True)
    parser.add_argument('-m', '--message', dest='proto_message', type=str, required=True)

    args = parser.parse_args()

    with GoFile(proto_import=args.proto_import, proto_message=args.proto_message) as go:
        go.generate()


if __name__ == '__main__':
    main()
