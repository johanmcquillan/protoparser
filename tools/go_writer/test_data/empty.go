package main

import (
	"fmt"
	"os"
	"strings"

	"github.com/golang/protobuf/proto"

	protopkg "github.com/johanmcquillan/protoparser/proto/finance"
)

func main() {
	arg := []byte(strings.Join(os.Args[1:], ""))
	pb := &protopkg.Transaction{}
	if err := proto.Unmarshal(arg, pb); err != nil {
		panic(err)
	}
}
