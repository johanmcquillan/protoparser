package main

import (
	"os"
	"strings"

	"github.com/golang/protobuf/jsonpb"
	"github.com/golang/protobuf/proto"

	protopkg "github.com/johanmcquillan/protoparser/proto/finance"
)

func main() {
	marshaller := &jsonpb.Marshaler{}
	arg := []byte(strings.Join(os.Args[1:], ""))
	pb := &protopkg.Transaction{}
	if err := proto.Unmarshal(arg, pb); err != nil {
		panic(err)
	}
	marshaller.Marshal(os.Stdout, pb)
}
