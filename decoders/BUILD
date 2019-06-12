subinclude("//tools:proto_decoder")

package(default_visibility=["//tests/..."])

protos = [
    "simple_message",
    "string_only",
]

def camel_case(name:str) -> str:
    words = name.split('_')
    return ''.join([word[0].upper() + word[1:] for word in words])

for proto in protos:
    proto_decoder(
        name = proto + "_decoder",
        args = [],
        proto_target = "//proto:examples",
        message = camel_case(proto),
    )
