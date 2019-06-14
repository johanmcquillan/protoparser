
import argparse

from tools.go_writer.decode import GoDecoder
from tools.go_writer.encode import GoEncoder


def add_common_arguments(parser: argparse.ArgumentParser):
    parser.add_argument('-o', '--outfile', type=str, required=True)
    parser.add_argument('-i', '--import', dest='proto_import', type=str, required=True)
    parser.add_argument('-m', '--message', dest='proto_message', type=str, required=True)


def write_decoder(args: argparse.Namespace):
    with GoDecoder(
            out_file=args.outfile,
            proto_import=args.proto_import,
            proto_message=args.proto_message,
    ) as go:
        go.generate()


def write_encoder(args: argparse.Namespace):
    with GoEncoder(
            out_file=args.outfile,
            proto_import=args.proto_import,
            proto_message=args.proto_message,
    ) as go:
        go.generate()


def main():
    parser = argparse.ArgumentParser('go_writer')
    subparsers = parser.add_subparsers()
    subparsers.required = True

    decoder_parser = subparsers.add_parser('decoder')
    add_common_arguments(decoder_parser)
    decoder_parser.set_defaults(func=write_decoder)

    encoder_parser = subparsers.add_parser('encoder')
    add_common_arguments(encoder_parser)
    encoder_parser.set_defaults(func=write_encoder)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
