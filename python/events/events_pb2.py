# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: events/events.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='events/events.proto',
  package='robocar.events',
  syntax='proto3',
  serialized_options=b'Z\010./events',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x65vents/events.proto\x12\x0erobocar.events\x1a\x1fgoogle/protobuf/timestamp.proto\"T\n\x08\x46rameRef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"C\n\x0c\x46rameMessage\x12$\n\x02id\x18\x01 \x01(\x0b\x32\x18.robocar.events.FrameRef\x12\r\n\x05\x66rame\x18\x02 \x01(\x0c\"d\n\x0fSteeringMessage\x12\x10\n\x08steering\x18\x01 \x01(\x02\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12+\n\tframe_ref\x18\x03 \x01(\x0b\x32\x18.robocar.events.FrameRef\"d\n\x0fThrottleMessage\x12\x10\n\x08throttle\x18\x01 \x01(\x02\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12+\n\tframe_ref\x18\x03 \x01(\x0b\x32\x18.robocar.events.FrameRef\"A\n\x10\x44riveModeMessage\x12-\n\ndrive_mode\x18\x01 \x01(\x0e\x32\x19.robocar.events.DriveMode\"f\n\x0eObjectsMessage\x12\'\n\x07objects\x18\x01 \x03(\x0b\x32\x16.robocar.events.Object\x12+\n\tframe_ref\x18\x02 \x01(\x0b\x32\x18.robocar.events.FrameRef\"\x80\x01\n\x06Object\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.robocar.events.TypeObject\x12\x0c\n\x04left\x18\x02 \x01(\x05\x12\x0b\n\x03top\x18\x03 \x01(\x05\x12\r\n\x05right\x18\x04 \x01(\x05\x12\x0e\n\x06\x62ottom\x18\x05 \x01(\x05\x12\x12\n\nconfidence\x18\x06 \x01(\x02\"&\n\x13SwitchRecordMessage\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\x8c\x01\n\x0bRoadMessage\x12&\n\x07\x63ontour\x18\x01 \x03(\x0b\x32\x15.robocar.events.Point\x12(\n\x07\x65llipse\x18\x02 \x01(\x0b\x32\x17.robocar.events.Ellipse\x12+\n\tframe_ref\x18\x03 \x01(\x0b\x32\x18.robocar.events.FrameRef\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"r\n\x07\x45llipse\x12%\n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x15.robocar.events.Point\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\r\n\x05\x61ngle\x18\x04 \x01(\x02\x12\x12\n\nconfidence\x18\x05 \x01(\x02\"\x82\x01\n\rRecordMessage\x12+\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x1c.robocar.events.FrameMessage\x12\x31\n\x08steering\x18\x02 \x01(\x0b\x32\x1f.robocar.events.SteeringMessage\x12\x11\n\trecordSet\x18\x03 \x01(\t*-\n\tDriveMode\x12\x0b\n\x07INVALID\x10\x00\x12\x08\n\x04USER\x10\x01\x12\t\n\x05PILOT\x10\x02*2\n\nTypeObject\x12\x07\n\x03\x41NY\x10\x00\x12\x07\n\x03\x43\x41R\x10\x01\x12\x08\n\x04\x42UMP\x10\x02\x12\x08\n\x04PLOT\x10\x03\x42\nZ\x08./eventsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_DRIVEMODE = _descriptor.EnumDescriptor(
  name='DriveMode',
  full_name='robocar.events.DriveMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='USER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PILOT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1196,
  serialized_end=1241,
)
_sym_db.RegisterEnumDescriptor(_DRIVEMODE)

DriveMode = enum_type_wrapper.EnumTypeWrapper(_DRIVEMODE)
_TYPEOBJECT = _descriptor.EnumDescriptor(
  name='TypeObject',
  full_name='robocar.events.TypeObject',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUMP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLOT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1243,
  serialized_end=1293,
)
_sym_db.RegisterEnumDescriptor(_TYPEOBJECT)

TypeObject = enum_type_wrapper.EnumTypeWrapper(_TYPEOBJECT)
INVALID = 0
USER = 1
PILOT = 2
ANY = 0
CAR = 1
BUMP = 2
PLOT = 3



_FRAMEREF = _descriptor.Descriptor(
  name='FrameRef',
  full_name='robocar.events.FrameRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='robocar.events.FrameRef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='robocar.events.FrameRef.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='robocar.events.FrameRef.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=156,
)


_FRAMEMESSAGE = _descriptor.Descriptor(
  name='FrameMessage',
  full_name='robocar.events.FrameMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='robocar.events.FrameMessage.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame', full_name='robocar.events.FrameMessage.frame', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=225,
)


_STEERINGMESSAGE = _descriptor.Descriptor(
  name='SteeringMessage',
  full_name='robocar.events.SteeringMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='steering', full_name='robocar.events.SteeringMessage.steering', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='robocar.events.SteeringMessage.confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_ref', full_name='robocar.events.SteeringMessage.frame_ref', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=327,
)


_THROTTLEMESSAGE = _descriptor.Descriptor(
  name='ThrottleMessage',
  full_name='robocar.events.ThrottleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='throttle', full_name='robocar.events.ThrottleMessage.throttle', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='robocar.events.ThrottleMessage.confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_ref', full_name='robocar.events.ThrottleMessage.frame_ref', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=429,
)


_DRIVEMODEMESSAGE = _descriptor.Descriptor(
  name='DriveModeMessage',
  full_name='robocar.events.DriveModeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='drive_mode', full_name='robocar.events.DriveModeMessage.drive_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=496,
)


_OBJECTSMESSAGE = _descriptor.Descriptor(
  name='ObjectsMessage',
  full_name='robocar.events.ObjectsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='objects', full_name='robocar.events.ObjectsMessage.objects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_ref', full_name='robocar.events.ObjectsMessage.frame_ref', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=498,
  serialized_end=600,
)


_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='robocar.events.Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='robocar.events.Object.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='left', full_name='robocar.events.Object.left', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top', full_name='robocar.events.Object.top', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right', full_name='robocar.events.Object.right', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='robocar.events.Object.bottom', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='robocar.events.Object.confidence', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=731,
)


_SWITCHRECORDMESSAGE = _descriptor.Descriptor(
  name='SwitchRecordMessage',
  full_name='robocar.events.SwitchRecordMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='robocar.events.SwitchRecordMessage.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=733,
  serialized_end=771,
)


_ROADMESSAGE = _descriptor.Descriptor(
  name='RoadMessage',
  full_name='robocar.events.RoadMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contour', full_name='robocar.events.RoadMessage.contour', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ellipse', full_name='robocar.events.RoadMessage.ellipse', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_ref', full_name='robocar.events.RoadMessage.frame_ref', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=774,
  serialized_end=914,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='robocar.events.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='robocar.events.Point.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='robocar.events.Point.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=916,
  serialized_end=945,
)


_ELLIPSE = _descriptor.Descriptor(
  name='Ellipse',
  full_name='robocar.events.Ellipse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='center', full_name='robocar.events.Ellipse.center', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='robocar.events.Ellipse.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='robocar.events.Ellipse.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle', full_name='robocar.events.Ellipse.angle', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='robocar.events.Ellipse.confidence', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=947,
  serialized_end=1061,
)


_RECORDMESSAGE = _descriptor.Descriptor(
  name='RecordMessage',
  full_name='robocar.events.RecordMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='robocar.events.RecordMessage.frame', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='steering', full_name='robocar.events.RecordMessage.steering', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recordSet', full_name='robocar.events.RecordMessage.recordSet', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1064,
  serialized_end=1194,
)

_FRAMEREF.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FRAMEMESSAGE.fields_by_name['id'].message_type = _FRAMEREF
_STEERINGMESSAGE.fields_by_name['frame_ref'].message_type = _FRAMEREF
_THROTTLEMESSAGE.fields_by_name['frame_ref'].message_type = _FRAMEREF
_DRIVEMODEMESSAGE.fields_by_name['drive_mode'].enum_type = _DRIVEMODE
_OBJECTSMESSAGE.fields_by_name['objects'].message_type = _OBJECT
_OBJECTSMESSAGE.fields_by_name['frame_ref'].message_type = _FRAMEREF
_OBJECT.fields_by_name['type'].enum_type = _TYPEOBJECT
_ROADMESSAGE.fields_by_name['contour'].message_type = _POINT
_ROADMESSAGE.fields_by_name['ellipse'].message_type = _ELLIPSE
_ROADMESSAGE.fields_by_name['frame_ref'].message_type = _FRAMEREF
_ELLIPSE.fields_by_name['center'].message_type = _POINT
_RECORDMESSAGE.fields_by_name['frame'].message_type = _FRAMEMESSAGE
_RECORDMESSAGE.fields_by_name['steering'].message_type = _STEERINGMESSAGE
DESCRIPTOR.message_types_by_name['FrameRef'] = _FRAMEREF
DESCRIPTOR.message_types_by_name['FrameMessage'] = _FRAMEMESSAGE
DESCRIPTOR.message_types_by_name['SteeringMessage'] = _STEERINGMESSAGE
DESCRIPTOR.message_types_by_name['ThrottleMessage'] = _THROTTLEMESSAGE
DESCRIPTOR.message_types_by_name['DriveModeMessage'] = _DRIVEMODEMESSAGE
DESCRIPTOR.message_types_by_name['ObjectsMessage'] = _OBJECTSMESSAGE
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
DESCRIPTOR.message_types_by_name['SwitchRecordMessage'] = _SWITCHRECORDMESSAGE
DESCRIPTOR.message_types_by_name['RoadMessage'] = _ROADMESSAGE
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Ellipse'] = _ELLIPSE
DESCRIPTOR.message_types_by_name['RecordMessage'] = _RECORDMESSAGE
DESCRIPTOR.enum_types_by_name['DriveMode'] = _DRIVEMODE
DESCRIPTOR.enum_types_by_name['TypeObject'] = _TYPEOBJECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrameRef = _reflection.GeneratedProtocolMessageType('FrameRef', (_message.Message,), {
  'DESCRIPTOR' : _FRAMEREF,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.FrameRef)
  })
_sym_db.RegisterMessage(FrameRef)

FrameMessage = _reflection.GeneratedProtocolMessageType('FrameMessage', (_message.Message,), {
  'DESCRIPTOR' : _FRAMEMESSAGE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.FrameMessage)
  })
_sym_db.RegisterMessage(FrameMessage)

SteeringMessage = _reflection.GeneratedProtocolMessageType('SteeringMessage', (_message.Message,), {
  'DESCRIPTOR' : _STEERINGMESSAGE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.SteeringMessage)
  })
_sym_db.RegisterMessage(SteeringMessage)

ThrottleMessage = _reflection.GeneratedProtocolMessageType('ThrottleMessage', (_message.Message,), {
  'DESCRIPTOR' : _THROTTLEMESSAGE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.ThrottleMessage)
  })
_sym_db.RegisterMessage(ThrottleMessage)

DriveModeMessage = _reflection.GeneratedProtocolMessageType('DriveModeMessage', (_message.Message,), {
  'DESCRIPTOR' : _DRIVEMODEMESSAGE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.DriveModeMessage)
  })
_sym_db.RegisterMessage(DriveModeMessage)

ObjectsMessage = _reflection.GeneratedProtocolMessageType('ObjectsMessage', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSMESSAGE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.ObjectsMessage)
  })
_sym_db.RegisterMessage(ObjectsMessage)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), {
  'DESCRIPTOR' : _OBJECT,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.Object)
  })
_sym_db.RegisterMessage(Object)

SwitchRecordMessage = _reflection.GeneratedProtocolMessageType('SwitchRecordMessage', (_message.Message,), {
  'DESCRIPTOR' : _SWITCHRECORDMESSAGE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.SwitchRecordMessage)
  })
_sym_db.RegisterMessage(SwitchRecordMessage)

RoadMessage = _reflection.GeneratedProtocolMessageType('RoadMessage', (_message.Message,), {
  'DESCRIPTOR' : _ROADMESSAGE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.RoadMessage)
  })
_sym_db.RegisterMessage(RoadMessage)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.Point)
  })
_sym_db.RegisterMessage(Point)

Ellipse = _reflection.GeneratedProtocolMessageType('Ellipse', (_message.Message,), {
  'DESCRIPTOR' : _ELLIPSE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.Ellipse)
  })
_sym_db.RegisterMessage(Ellipse)

RecordMessage = _reflection.GeneratedProtocolMessageType('RecordMessage', (_message.Message,), {
  'DESCRIPTOR' : _RECORDMESSAGE,
  '__module__' : 'events.events_pb2'
  # @@protoc_insertion_point(class_scope:robocar.events.RecordMessage)
  })
_sym_db.RegisterMessage(RecordMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
