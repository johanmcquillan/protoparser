
def go_proto_decoder(
        name:str, args:list, deps:list,
):
    args_string = ' '.join(args)
    genrule(
        name = '_%s#gosrc' % name,
        tools = ['//tools/go_writer'],
        outs = ['main.go'],
        cmd = [
            '$(exe //tools/go_writer) %s' % args_string,
        ],
    )

    go_binary(
        name = name,
        srcs = [':_%s#gosrc' % name],
        deps = deps,
    )


go_proto_decoder(
    name = 'test',
    args = [],
    deps = [],
)
