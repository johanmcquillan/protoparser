package main

import (
	"bufio"
	"bytes"
	"os"

	"github.com/golang/protobuf/jsonpb"
	"github.com/golang/protobuf/proto"

	pbpkg "github.com/johanmcquillan/protoparser/proto/examples"
)

func main() {
	unmarshaller := &jsonpb.Unmarshaler{}

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		json := scanner.Bytes()
		reader := bytes.NewReader(json)
		pb := &pbpkg.SimpleMessage{}
		if err := unmarshaller.Unmarshal(reader, pb); err != nil {
			panic(err)
		}

		msg, err := proto.Marshal(pb)
		if err != nil {
			panic(err)
		}
		os.Stdout.Write(msg)
	}
}
