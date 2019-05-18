
import argparse


_INDENT = ' '*4


class GoFile(object):

    def __init__(self, imports=None):
        if imports is None:
            imports = []
        self.imports = imports

    def write_imports(self, f):
        f.write('\nimport (\n')
        f.write(_INDENT + '"fmt"\n')

        if len(self.imports) > 0:
            f.write('\n')
            for i in sorted(self.imports):
                f.write(_INDENT + i + '\n')
        f.write(')\n')

    def write_main(self, f):
        f.write('\nfunc main() {\n')

        f.write(_INDENT +  'fmt.Println("Hello World!")\n')

        f.write('}\n')


    def generate(self):

        with open('main.go', 'w') as f:
            f.write('package main\n\n')

            self.write_imports(f)
            self.write_main(f)


def main():
    parser = argparse.ArgumentParser('go_writer')
    parser.add_argument('-i', '--imports', nargs='*')

    args = parser.parse_args()

    GoFile(imports=args.imports).generate()


if __name__ == '__main__':
    main()
