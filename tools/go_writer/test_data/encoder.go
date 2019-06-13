package main

import (
	"bufio"
	"bytes"
	"os"

	"github.com/golang/protobuf/jsonpb"
	"github.com/golang/protobuf/proto"

	protopkg "github.com/johanmcquillan/protoparser/proto/examples"
)

func main() {
	opts := &Opts{}
	if _, err := flags.Parse(opts); err != nil {
		panic(err)
	}

	marshaller := &jsonpb.Unmarshaler{}

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		json := scanner.Bytes()
		reader := bytes.NewReader(json)
		pb := &protopkg.SimpleMessage{}
		if err := marshaller.Unmarshal(reader, pb); err != nil {
			panic(err)
		}
		msg, err := proto.Marshal(pb)
		if err != nil {
			panic(err)
		}
		os.Stdout.Write(msg)
	}
}
