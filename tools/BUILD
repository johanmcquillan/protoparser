
def go_proto_decoder(name:str, args:list, proto_target:str, message:str):
    args_string = ' '.join(args)

    go_proto_import = CONFIG.GO_IMPORT_PATH + canonicalise(proto_target)[1:].replace(':', '/')

    genrule(
        name = '_%s#gosrc' % name,
        tools = ['//tools/go_writer'],
        outs = ['main.go'],
        cmd = [
            '$(exe //tools/go_writer) -i %s -m %s %s' % (go_proto_import, message, args_string),
        ],
    )

    go_binary(
        name = name,
        srcs = [':_%s#gosrc' % name],
        deps = [
            proto_target,
            '//third_party/go:jsonpb',
            '//third_party/go:protobuf',
        ],
    )

go_proto_decoder(
    name = 'example',
    args = [],
    proto_target = '//proto:finance',
    message = 'Transaction',
)
