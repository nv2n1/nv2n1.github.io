---
title: "globus_gass_transfer_proto-h(3)"
name: "globus_gass_transfer_proto-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_proto-h/"
description: "globus_gass_transfer_proto.h –"
---

<p>globus_gass_transfer_proto.h &#8211; </p>
<p> GASS Transfer Protocol Interface.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_gass_transfer.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>globus_gass_transfer_request_proto_s</code><br />
 <i>Protocol module request handling structure. </i><br />
 struct <code>globus_gass_transfer_listener_proto_s</code><br />
 <i>Protocol module listener handling structure. </i><br />
 struct <code>globus_gass_transfer_proto_descriptor_t</code><br />
 <i>Protocol module descriptor structure. </i></p>
<h3>Typedefs</h3>
<p>typedef struct<br />
 <code>globus_gass_transfer_request_proto_s</code> <code>globus_gass_transfer_request_proto_t</code>&quot; </p>
<p> typedef struct<br />
 <code>globus_gass_transfer_listener_proto_s</code> <code>globus_gass_transfer_listener_proto_t</code>&quot; </p>
<p> typedef void(* <code>globus_gass_transfer_proto_send_t</code> )(<code>globus_gass_transfer_request_proto_t</code> *proto, <code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t send_length, globus_bool_t last_data) </p>
<p> typedef void(* <code>globus_gass_transfer_proto_receive_t</code> )(<code>globus_gass_transfer_request_proto_t</code> *proto, <code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t bytes_length, globus_size_t wait_for_length) </p>
<p> typedef void(* <code>globus_gass_transfer_proto_func_t</code> )(<code>globus_gass_transfer_request_proto_t</code> *proto, <code>globus_gass_transfer_request_t</code> request) </p>
<p> typedef void(* <code>globus_gass_transfer_proto_new_request_t</code> )(<code>globus_gass_transfer_request_t</code> request, globus_gass_transfer_requestattr_t *attr) </p>
<p> typedef int(* <code>globus_gass_transfer_proto_create_listener_t</code> )(globus_gass_transfer_listener_t listener, globus_gass_transfer_listenerattr_t *attr, char *scheme, char **base_url, <code>globus_gass_transfer_listener_proto_t</code> **proto) </p>
<p> typedef void(* <code>globus_gass_transfer_proto_listener_t</code> )(<code>globus_gass_transfer_listener_proto_t</code> *proto, globus_gass_transfer_listener_t listener) </p>
<p> typedef globus_object_t *(* <code>globus_gass_transfer_proto_new_attr_t</code> )(char *url_scheme) </p>
<p> typedef void(* <code>globus_gass_transfer_proto_accept_t</code> )(<code>globus_gass_transfer_listener_proto_t</code> *proto, globus_gass_transfer_listener_t listener, <code>globus_gass_transfer_request_t</code> request, globus_gass_transfer_requestattr_t *attr) </p>
<h2>Detailed Description</h2>
<p>GASS Transfer Protocol Interface. </p>
<p> This header defines the GASS protocol module library interface</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gass_transfer from the source code.</p>
