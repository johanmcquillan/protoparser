package main

import (
	"fmt"
	//"os"

	"github.com/golang/protobuf/proto"

	"github.com/johanmcquillan/protoparser/proto/finance"
)

func main() {
	//input := os.Args[1]

	txn := &finance.Transaction{
		ToAccount: "ME",
		FromAccount: "YOU",
	}

	msg, err := proto.Marshal(txn)
	if err != nil {
		panic(err)
	}

	transformer(msg)
}

func transformer(data []byte) string {
	fmt.Println(string(data))
	return ""
}
