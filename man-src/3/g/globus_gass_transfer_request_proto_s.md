---
title: "globus_gass_transfer_request_proto_s(3)"
name: "globus_gass_transfer_request_proto_s"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_request_proto_s/"
description: "globus_gass_transfer_request_proto_s –"
---

<h2 class="name">NAME</h2>
<p> globus_gass_transfer_request_proto_s &#8211; </p>
<p> Protocol module request handling structure.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_gass_transfer_proto.h&gt;</p>
<h3>Data Fields</h3>
<p> <code>globus_gass_transfer_proto_send_t</code> <code>send_buffer</code> </p>
<p> <code>globus_gass_transfer_proto_receive_t</code> <code>recv_buffer</code> </p>
<p> <code>globus_gass_transfer_proto_func_t</code> <code>fail</code> </p>
<p> <code>globus_gass_transfer_proto_func_t</code> <code>deny</code> </p>
<p> <code>globus_gass_transfer_proto_func_t</code> <code>refer</code> </p>
<p> <code>globus_gass_transfer_proto_func_t</code> <code>authorize</code> </p>
<p> <code>globus_gass_transfer_proto_func_t</code> <code>destroy</code> </p>
<h2>Detailed Description</h2>
<p> Protocol module request handling structure. </p>
<p> This structure is created by a GASS transfer protocol module to handle a particular request. It is created in response to a <code>listener&#8217;s accept method</code> or a <code>protocol module&#8217;s new_request method</code>. </p>
<p> Memory management of this structure is the responsibility of the protocol module. The destroy method will be called when the GASS Transfer library is finished dealing with it. </p>
<p> A protocol module may create a extension to this structure to contain protocol-specific information, as long as the first fields of the structure match this type. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_request_ready()</code></dl>
<h2>Field Documentation</h2>
<h3><code>globus_gass_transfer_proto_func_t</code> globus_gass_transfer_request_proto_s::authorize</h3>
<p> Authorize a request.</p>
<h3><code>globus_gass_transfer_proto_func_t</code> globus_gass_transfer_request_proto_s::deny</h3>
<p> Deny a request.</p>
<h3><code>globus_gass_transfer_proto_func_t</code> globus_gass_transfer_request_proto_s::destroy</h3>
<p> Destroy a request.</p>
<h3><code>globus_gass_transfer_proto_func_t</code> globus_gass_transfer_request_proto_s::fail</h3>
<p> Fail a request. </p>
<p> This function is called when the application calls globus_gass_transfer_fail() on a request.</p>
<h3><code>globus_gass_transfer_proto_receive_t</code> globus_gass_transfer_request_proto_s::recv_buffer</h3>
<p> Receive bytes. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_gass_transfer_proto_recv_t</dl>
<h3><code>globus_gass_transfer_proto_func_t</code> globus_gass_transfer_request_proto_s::refer</h3>
<p> Refer a request.</p>
<h3><code>globus_gass_transfer_proto_send_t</code> globus_gass_transfer_request_proto_s::send_buffer</h3>
<p> Send bytes. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_send_t</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Author</a></p>
<dd></dl>
