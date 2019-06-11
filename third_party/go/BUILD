package(default_visibility = ["PUBLIC"])

go_get(
    name = "jsonpb",
    get = "github.com/golang/protobuf/jsonpb",
    deps = [
        ":ptypes",
    ],
)

go_get(
    name = "protobuf",
    get = "github.com/golang/protobuf/proto",
)

go_get(
    name = "ptypes",
    get = "github.com/golang/protobuf/ptypes",
    install = [
        "",
        "struct",
    ],
    deps = [
        ":protobuf",
    ],
)
