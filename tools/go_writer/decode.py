
import argparse

from tools.go_writer.common import GoFile


_VAR_PB = 'pb'
_VAR_PPKG = 'protopkg'


class GoDecoder(GoFile):

    _std_imports = [
        'bufio',
        'os',
    ]

    _third_party_imports = [
        'github.com/golang/protobuf/jsonpb',
        'github.com/golang/protobuf/proto',
        'github.com/jessevdk/go-flags',
    ]

    @property
    def std_imports(self):
        return self._std_imports

    @property
    def third_party_imports(self):
        return self._third_party_imports

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
        self.writeln(f'{self.proto_var} := &{self.proto_pkg}.{self.proto_message}{{}}', indent=2)
        self.writeln(f'if err := proto.Unmarshal(msg, {_VAR_PB}); err != nil {{', indent=2)
        self.writeln(f'panic(err)', indent=3)
        self.writeln('}', indent=2)

        self.writeln(f'marshaller.Marshal(os.Stdout, {_VAR_PB})', indent=2)
        self.writeln('}', indent=1)
        self.writeln('}')
