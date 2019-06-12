package main

import (
	"bufio"
	"os"

	"github.com/golang/protobuf/jsonpb"
	"github.com/golang/protobuf/proto"

	protopkg "github.com/johanmcquillan/protoparser/proto/examples"
)

func main() {
	marshaller := &jsonpb.Marshaler{
		OrigName: true,
	}
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		msg := scanner.Bytes()
		pb := &protopkg.SimpleMessage{}
		if err := proto.Unmarshal(msg, pb); err != nil {
			panic(err)
		}
		marshaller.Marshal(os.Stdout, pb)
	}
}
