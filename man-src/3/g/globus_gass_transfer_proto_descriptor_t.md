---
title: "globus_gass_transfer_proto_descriptor_t(3)"
name: "globus_gass_transfer_proto_descriptor_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_proto_descriptor_t/"
description: "globus_gass_transfer_proto_descriptor_t –"
---

<h2 class="name">NAME</h2>
<p> globus_gass_transfer_proto_descriptor_t &#8211; </p>
<p> Protocol module descriptor structure.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_gass_transfer_proto.h&gt;</p>
<h3>Data Fields</h3>
<p> char * <code>url_scheme</code> </p>
<p> <code>globus_gass_transfer_proto_new_attr_t</code> <code>new_requestattr</code> </p>
<p> <code>globus_gass_transfer_proto_new_request_t</code> <code>new_request</code> </p>
<p> <code>globus_gass_transfer_proto_new_attr_t</code> <code>new_listenerattr</code> </p>
<p> <code>globus_gass_transfer_proto_create_listener_t</code> <code>new_listener</code> </p>
<h2>Detailed Description</h2>
<p> Protocol module descriptor structure. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_register_protocol()</code>, <code>globus_gass_transfer_proto_unregister_protocol()</code></dl>
<h2>Field Documentation</h2>
<h3><code>globus_gass_transfer_proto_create_listener_t</code> globus_gass_transfer_proto_descriptor_t::new_listener</h3>
<p> New listener. </p>
<p> The function pointed to by this pointer is used by GASS to create a new listener handle. The listener handle has been initialized with the parameters passed to one of the functions in the <code>Client-Initiated Operations</code> section of the GASS Transfer API. </p>
<p> The protocol module should begin processing this request by sending appropriate messages to the file server. Once the request is authorized, denied, or referred, the protocol module calls <code>globus_gass_transfer_proto_request_ready()</code>, <code>globus_gass_transfer_proto_request_denied()</code>, or <code>globus_gass_transfer_proto_request_referred()</code>. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_new_request_t</code></dl>
<h3><code>globus_gass_transfer_proto_new_attr_t</code> globus_gass_transfer_proto_descriptor_t::new_listenerattr</h3>
<p> New listener attributes. </p>
<p> The function pointed to by this pointer is used by GASS to forward requests to create a listener attribute for this protocol&#8217;s <i>url_scheme</i> to the protocol module. The function returns a listener attribute which inherits from one of the GASS Transfer request attributes. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_new_attr_t</code></dl>
<h3><code>globus_gass_transfer_proto_new_request_t</code> globus_gass_transfer_proto_descriptor_t::new_request</h3>
<p> New request. </p>
<p> The function pointed to by this pointer is used by GASS to initiate a new file transfer request by a protocol module. The request handle has been initialized with the parameters passed to one of the functions in the <code>Client-Initiated Operations</code> section of the GASS Transfer API. </p>
<p> The protocol module should begin processing this request by sending appropriate messages to the file server. Once the request is authorized, denied, or referred, the protocol module calls <code>globus_gass_transfer_proto_request_ready()</code>, <code>globus_gass_transfer_proto_request_denied()</code>, or <code>globus_gass_transfer_proto_request_referred()</code>. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_new_request_t</code></dl>
<h3><code>globus_gass_transfer_proto_new_attr_t</code> globus_gass_transfer_proto_descriptor_t::new_requestattr</h3>
<p> New request attributes. </p>
<p> The function pointed to by this pointer is used by GASS to forward requests to create a request attribute for this protocol&#8217;s <i>url_scheme</i> to the protocol module. The function returns a request attribute which inherits from one of the GASS Transfer request attributes. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_new_attr_t</code></dl>
<h3>char* globus_gass_transfer_proto_descriptor_t::url_scheme</h3>
<p> URL Scheme. </p>
<p> The URL scheme which this protocol module supports. The scheme is the first part of a URL, which names the protocol which is used to access the resource named by the URL, for example &#8216;http&#8217; or &#8216;ftp&#8217;. </p>
<p> The GASS Transfer library allows only one protocol module to be registered to handle a particular <i>url_scheme</i>. However, a protocol module may implement only the client or only the server part of the protocol. If a protocol has several variations with different scheme names (for example http and https), each scheme must be registered with GASS in order to be used. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
