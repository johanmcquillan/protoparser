
import argparse

from tools.go_writer.common import GoFile


_VAR_PB = 'pb'
_VAR_PPKG = 'protopkg'


class GoEncoder(GoFile):

    _std_imports = [
        'bufio',
        'bytes',
        'os',
    ]

    _third_party_imports = [
        'github.com/golang/protobuf/jsonpb',
        'github.com/golang/protobuf/proto',
    ]

    @property
    def std_imports(self):
        return self._std_imports

    @property
    def third_party_imports(self):
        return self._third_party_imports

    def write_opts(self):
        pass

    def write_main(self):
        self.writeln('func main() {')

        self.writeln('unmarshaller := &jsonpb.Unmarshaler{}', indent=1)
        self.writeln()

        self.writeln('scanner := bufio.NewScanner(os.Stdin)', indent=1)
        self.writeln('for scanner.Scan() {', indent=1)
        self.writeln('json := scanner.Bytes()', indent=2)
        self.writeln('reader := bytes.NewReader(json)', indent=2)
        self.writeln(f'{self.proto_var} := &{self.proto_pkg}.{self.proto_message}{{}}', indent=2)
        self.writeln(f'if err := unmarshaller.Unmarshal(reader, {self.proto_var}); err != nil {{', indent=2)
        self.writeln(f'panic(err)', indent=3)
        self.writeln('}', indent=2)
        self.writeln()

        self.writeln(f'msg, err := proto.Marshal({self.proto_var})', indent=2)
        self.writeln('if err != nil {', indent=2)
        self.writeln('panic(err)', indent=3)
        self.writeln('}', indent=2)

        self.writeln(f'os.Stdout.Write(msg)', indent=2)
        self.writeln('}', indent=1)
        self.writeln('}')
