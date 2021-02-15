# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yggdrasil.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yggdrasil.proto',
  package='yggdrasil',
  syntax='proto3',
  serialized_options=b'Z,github.com/redhatinsights/yggdrasil/protocol',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fyggdrasil.proto\x12\tyggdrasil\"\x07\n\x05\x45mpty\"\xbe\x01\n\x13RegistrationRequest\x12\x0f\n\x07handler\x18\x01 \x01(\t\x12\x0b\n\x03pid\x18\x02 \x01(\x03\x12\x18\n\x10\x64\x65tached_content\x18\x03 \x01(\x08\x12>\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32,.yggdrasil.RegistrationRequest.FeaturesEntry\x1a/\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\";\n\x14RegistrationResponse\x12\x12\n\nregistered\x18\x01 \x01(\x08\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"\xb5\x01\n\x04\x44\x61ta\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12/\n\x08metadata\x18\x02 \x03(\x0b\x32\x1d.yggdrasil.Data.MetadataEntry\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\x12\x13\n\x0bresponse_to\x18\x04 \x01(\t\x12\x11\n\tdirective\x18\x05 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\t\n\x07Receipt2\x8a\x01\n\nDispatcher\x12M\n\x08Register\x12\x1e.yggdrasil.RegistrationRequest\x1a\x1f.yggdrasil.RegistrationResponse\"\x00\x12-\n\x04Send\x12\x0f.yggdrasil.Data\x1a\x12.yggdrasil.Receipt\"\x00\x32\x37\n\x06Worker\x12-\n\x04Send\x12\x0f.yggdrasil.Data\x1a\x12.yggdrasil.Receipt\"\x00\x42.Z,github.com/redhatinsights/yggdrasil/protocolb\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='yggdrasil.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=30,
  serialized_end=37,
)


_REGISTRATIONREQUEST_FEATURESENTRY = _descriptor.Descriptor(
  name='FeaturesEntry',
  full_name='yggdrasil.RegistrationRequest.FeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yggdrasil.RegistrationRequest.FeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yggdrasil.RegistrationRequest.FeaturesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=230,
)

_REGISTRATIONREQUEST = _descriptor.Descriptor(
  name='RegistrationRequest',
  full_name='yggdrasil.RegistrationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='handler', full_name='yggdrasil.RegistrationRequest.handler', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pid', full_name='yggdrasil.RegistrationRequest.pid', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detached_content', full_name='yggdrasil.RegistrationRequest.detached_content', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features', full_name='yggdrasil.RegistrationRequest.features', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REGISTRATIONREQUEST_FEATURESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=230,
)


_REGISTRATIONRESPONSE = _descriptor.Descriptor(
  name='RegistrationResponse',
  full_name='yggdrasil.RegistrationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='registered', full_name='yggdrasil.RegistrationResponse.registered', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='yggdrasil.RegistrationResponse.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=232,
  serialized_end=291,
)


_DATA_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='yggdrasil.Data.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yggdrasil.Data.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yggdrasil.Data.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=475,
)

_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='yggdrasil.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='yggdrasil.Data.message_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='yggdrasil.Data.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='yggdrasil.Data.content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_to', full_name='yggdrasil.Data.response_to', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='directive', full_name='yggdrasil.Data.directive', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATA_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=475,
)


_RECEIPT = _descriptor.Descriptor(
  name='Receipt',
  full_name='yggdrasil.Receipt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=477,
  serialized_end=486,
)

_REGISTRATIONREQUEST_FEATURESENTRY.containing_type = _REGISTRATIONREQUEST
_REGISTRATIONREQUEST.fields_by_name['features'].message_type = _REGISTRATIONREQUEST_FEATURESENTRY
_DATA_METADATAENTRY.containing_type = _DATA
_DATA.fields_by_name['metadata'].message_type = _DATA_METADATAENTRY
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['RegistrationRequest'] = _REGISTRATIONREQUEST
DESCRIPTOR.message_types_by_name['RegistrationResponse'] = _REGISTRATIONRESPONSE
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['Receipt'] = _RECEIPT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'yggdrasil_pb2'
  # @@protoc_insertion_point(class_scope:yggdrasil.Empty)
  })
_sym_db.RegisterMessage(Empty)

RegistrationRequest = _reflection.GeneratedProtocolMessageType('RegistrationRequest', (_message.Message,), {

  'FeaturesEntry' : _reflection.GeneratedProtocolMessageType('FeaturesEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTRATIONREQUEST_FEATURESENTRY,
    '__module__' : 'yggdrasil_pb2'
    # @@protoc_insertion_point(class_scope:yggdrasil.RegistrationRequest.FeaturesEntry)
    })
  ,
  'DESCRIPTOR' : _REGISTRATIONREQUEST,
  '__module__' : 'yggdrasil_pb2'
  # @@protoc_insertion_point(class_scope:yggdrasil.RegistrationRequest)
  })
_sym_db.RegisterMessage(RegistrationRequest)
_sym_db.RegisterMessage(RegistrationRequest.FeaturesEntry)

RegistrationResponse = _reflection.GeneratedProtocolMessageType('RegistrationResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRATIONRESPONSE,
  '__module__' : 'yggdrasil_pb2'
  # @@protoc_insertion_point(class_scope:yggdrasil.RegistrationResponse)
  })
_sym_db.RegisterMessage(RegistrationResponse)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATA_METADATAENTRY,
    '__module__' : 'yggdrasil_pb2'
    # @@protoc_insertion_point(class_scope:yggdrasil.Data.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _DATA,
  '__module__' : 'yggdrasil_pb2'
  # @@protoc_insertion_point(class_scope:yggdrasil.Data)
  })
_sym_db.RegisterMessage(Data)
_sym_db.RegisterMessage(Data.MetadataEntry)

Receipt = _reflection.GeneratedProtocolMessageType('Receipt', (_message.Message,), {
  'DESCRIPTOR' : _RECEIPT,
  '__module__' : 'yggdrasil_pb2'
  # @@protoc_insertion_point(class_scope:yggdrasil.Receipt)
  })
_sym_db.RegisterMessage(Receipt)


DESCRIPTOR._options = None
_REGISTRATIONREQUEST_FEATURESENTRY._options = None
_DATA_METADATAENTRY._options = None

_DISPATCHER = _descriptor.ServiceDescriptor(
  name='Dispatcher',
  full_name='yggdrasil.Dispatcher',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=489,
  serialized_end=627,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='yggdrasil.Dispatcher.Register',
    index=0,
    containing_service=None,
    input_type=_REGISTRATIONREQUEST,
    output_type=_REGISTRATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='yggdrasil.Dispatcher.Send',
    index=1,
    containing_service=None,
    input_type=_DATA,
    output_type=_RECEIPT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISPATCHER)

DESCRIPTOR.services_by_name['Dispatcher'] = _DISPATCHER


_WORKER = _descriptor.ServiceDescriptor(
  name='Worker',
  full_name='yggdrasil.Worker',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=629,
  serialized_end=684,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='yggdrasil.Worker.Send',
    index=0,
    containing_service=None,
    input_type=_DATA,
    output_type=_RECEIPT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKER)

DESCRIPTOR.services_by_name['Worker'] = _WORKER

# @@protoc_insertion_point(module_scope)
