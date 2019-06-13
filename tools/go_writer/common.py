
from abc import ABC, abstractmethod


class GoFile(ABC):

    indent = '\t'

    proto_pkg = 'pbpkg'
    proto_var = 'pb'

    def __init__(
            self,
            proto_import,
            proto_message,
            out_file='main.go',
    ):
        self.out_file = out_file
        self.proto_import = proto_import
        self.proto_message = proto_message
        self.f = None
        super().__init__()

    def open(self):
        self.f = open(self.out_file, 'x')

    def close(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def write(self, string: str, indent=0):
        self.f.write(indent * self.indent + string)

    def writeln(self, *args, indent=0):
        if len(args) == 0:
            self.write('\n')
            return
        for arg in args:
            self.write(arg + '\n', indent=indent)

    @property
    @abstractmethod
    def std_imports():
        pass

    @property
    @abstractmethod
    def third_party_imports():
        pass

    def write_imports(self):
        self.writeln('import (')

        for i in sorted(self.std_imports):
            self.writeln(f'"{i}"', indent=1)
        self.writeln()

        for i in sorted(self.third_party_imports):
            self.writeln(f'"{i}"', indent=1)
        self.writeln()

        self.writeln(f'{self.proto_pkg} "{self.proto_import}"', indent=1)
        self.writeln(')')

    @abstractmethod
    def write_opts():
        pass

    @abstractmethod
    def write_main():
        pass

    def generate(self):
        self.writeln('package main')
        self.writeln()

        self.write_imports()
        self.writeln()

        self.write_opts()

        self.write_main()
