
import argparse
import os

class GoFile(object):

    def __init__(self, imports=None):
        if imports is None:
            imports = []
        self.imports = imports

    def generate(self):

        with open('main.go', 'w') as f:
            f.write('package main\n\n')

            f.write('import (\n')
            f.write('    "fmt"\n')
            for i in self.imports:
                f.write('    ' + i + '\n')
            f.write(')\n\n')

            f.write('func main() {')

            f.write('    fmt.Println("Hello World!")\n')

            f.write('}\n')


def main():
    parser = argparse.ArgumentParser('go_writer')
    parser.add_argument('-i', '--imports', nargs='*')

    args = parser.parse_args()

    GoFile(imports=args.imports).generate()


if __name__ == '__main__':
    main()
