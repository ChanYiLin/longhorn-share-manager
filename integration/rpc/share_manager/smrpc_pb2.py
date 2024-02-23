# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smrpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='smrpc.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bsmrpc.proto\x1a\x1bgoogle/protobuf/empty.proto\"1\n\x15\x46ilesystemTrimRequest\x12\x18\n\x10\x65ncrypted_device\x18\x01 \x01(\x08\x32\xd1\x01\n\x13ShareManagerService\x12\x42\n\x0e\x46ilesystemTrim\x12\x16.FilesystemTrimRequest\x1a\x16.google.protobuf.Empty\"\x00\x12;\n\x07Unmount\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x39\n\x05Mount\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_FILESYSTEMTRIMREQUEST = _descriptor.Descriptor(
  name='FilesystemTrimRequest',
  full_name='FilesystemTrimRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encrypted_device', full_name='FilesystemTrimRequest.encrypted_device', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=44,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['FilesystemTrimRequest'] = _FILESYSTEMTRIMREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FilesystemTrimRequest = _reflection.GeneratedProtocolMessageType('FilesystemTrimRequest', (_message.Message,), {
  'DESCRIPTOR' : _FILESYSTEMTRIMREQUEST,
  '__module__' : 'smrpc_pb2'
  # @@protoc_insertion_point(class_scope:FilesystemTrimRequest)
  })
_sym_db.RegisterMessage(FilesystemTrimRequest)



_SHAREMANAGERSERVICE = _descriptor.ServiceDescriptor(
  name='ShareManagerService',
  full_name='ShareManagerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=96,
  serialized_end=305,
  methods=[
  _descriptor.MethodDescriptor(
    name='FilesystemTrim',
    full_name='ShareManagerService.FilesystemTrim',
    index=0,
    containing_service=None,
    input_type=_FILESYSTEMTRIMREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Unmount',
    full_name='ShareManagerService.Unmount',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Mount',
    full_name='ShareManagerService.Mount',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHAREMANAGERSERVICE)

DESCRIPTOR.services_by_name['ShareManagerService'] = _SHAREMANAGERSERVICE

# @@protoc_insertion_point(module_scope)