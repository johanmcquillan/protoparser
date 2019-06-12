package main

import (
	"bufio"
	"os"

	"github.com/golang/protobuf/jsonpb"
	"github.com/golang/protobuf/proto"
	"github.com/jessevdk/go-flags"

	protopkg "github.com/johanmcquillan/protoparser/proto/examples"
)

type Opts struct {
	EnumsAsInts  bool   `short:"e" long:"enums" description:"Whether to render enum values as integers, as opposed to string values"`
	EmitDefaults bool   `short:"d" long:"defaults" description:"Whether to render fields with zero values"`
	Indent       string `short:"i" long:"indent" description:"A string to indent each level by"`
	OrigName     bool   `short:"o" long:"original" description:"Whether to use the original (.proto) name for fields"`
}

func main() {
	opts := &Opts{}
	if _, err := flags.Parse(opts); err != nil {
		panic(err)
	}

	marshaller := &jsonpb.Marshaler{
		EnumsAsInts:  opts.EnumsAsInts,
		EmitDefaults: opts.EmitDefaults,
		OrigName:     opts.OrigName,
		Indent:       opts.Indent,
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
