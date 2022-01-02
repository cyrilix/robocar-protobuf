.PHONY: generate
PROTOC_GEN_GO := $(GOPATH)/bin/protoc-gen-go
PROTOC := $(shell which protoc)
# If protoc isn't on the path, set it to a target that's never up to date, so
# the install command always runs.
ifeq ($(PROTOC),)
    PROTOC = must-rebuild
endif

# Figure out which machine we're running on.
UNAME := $(shell uname)

$(PROTOC):
# Run the right installation command for the operating system.
ifeq ($(UNAME), Darwin)
	brew install protobuf
endif
ifeq ($(UNAME), Linux)
	sudo apt-get install protobuf-compiler
endif
# You can add instructions for other operating systems here, or use different
# branching logic as appropriate.

# If $GOPATH/bin/protoc-gen-go does not exist, we'll run this command to install
# it.
$(PROTOC_GEN_GO):
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest

events.pb.go: events/events.proto | $(PROTOC_GEN_GO) $(PROTOC)
	protoc --go_out=./go --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative events/events.proto

events.pb.py: events/events.proto | $(PROTOC)
	protoc --python_out=./python events/events.proto

events: events.pb.go events.pb.py

# This is a "phony" target - an alias for the above command, so "make compile"
# still works.
generate: events

