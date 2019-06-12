for test in glob(["*_test.py"]):
    name = splitext(test)[0]
    decoder = "_".join(name.split("_")[:-1]) + "_decoder"

    python_test(
        name = name,
        srcs = [test],
        deps = [
            "//proto:examples",
        ],
        data = [
            "//decoders:" + decoder,
        ],
    )
