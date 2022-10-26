# robocar-protobuf

Protobuf message definitions for robocar

## Generate package

```bash
poetry self install
poetry shell
cd ..
protoc --python_out=./python --mypy_out=./python events/events.proto
cd python
poetry build
```