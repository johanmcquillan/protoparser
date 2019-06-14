
python_library(
    name = "test_utils",
    srcs = ["test_utils.py"],
)

for test in glob(["*_test.py"]):
    name = splitext(test)[0]
    message = "_".join(name.split("_")[:-1])

    python_test(
        name = name,
        srcs = [test],
        deps = [
            ":test_utils",
            "//proto:examples",
        ],
        data = [
            "//parsers:%s_decoder" % message,
        ],
    )
