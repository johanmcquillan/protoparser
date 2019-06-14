python_binary(
    name = "go_writer",
    main = "go_writer.py",
    srcs = [
        "decode.py",
        "common.py",
        "encode.py",
    ],
    visibility = ["PUBLIC"],
)

python_test(
    name = "test",
    srcs = ["go_writer_test.py"],
    deps = [
        ":go_writer",
    ],
    data = glob(["test_data/*"]),
)
