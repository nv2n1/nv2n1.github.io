---
title: "globus_gass_transfer_proto_request_denied(3)"
name: "globus_gass_transfer_proto_request_denied"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_proto_request_denied/"
description: "Protocol Modules –"
---

<h2 class="name">NAME</h2>
<p> Protocol Modules &#8211; </p>
<p> Protocol Implementation API.</p>
<h3>Data Structures</h3>
<p> struct <code>globus_gass_transfer_request_proto_s</code><br />
 <i>Protocol module request handling structure. </i><br />
 struct <code>globus_gass_transfer_listener_proto_s</code><br />
 <i>Protocol module listener handling structure. </i><br />
 struct <code>globus_gass_transfer_proto_descriptor_t</code><br />
 <i>Protocol module descriptor structure. </i></p>
<h3>Typedefs</h3>
<p> typedef struct<br />
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
<h3>Functions</h3>
<p> void <code>globus_gass_transfer_proto_send_complete</code> (<code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t nbytes, globus_bool_t failed, globus_bool_t last_data) </p>
<p> void <code>globus_gass_transfer_proto_receive_complete</code> (<code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t nbytes, globus_bool_t failed, globus_bool_t last_data) </p>
<p> void <code>globus_gass_transfer_proto_listener_ready</code> (globus_gass_transfer_listener_t listener) </p>
<p> int <code>globus_gass_transfer_proto_register_protocol</code> (<code>globus_gass_transfer_proto_descriptor_t</code> *proto_desc) </p>
<p> int <code>globus_gass_transfer_proto_unregister_protocol</code> (<code>globus_gass_transfer_proto_descriptor_t</code> *proto_desc) </p>
<p> void <code>globus_gass_transfer_proto_request_ready</code> (<code>globus_gass_transfer_request_t</code> request, <code>globus_gass_transfer_request_proto_t</code> *proto) </p>
<p> void <code>globus_gass_transfer_proto_new_listener_request</code> (globus_gass_transfer_listener_t listener, <code>globus_gass_transfer_request_t</code> request, <code>globus_gass_transfer_request_proto_t</code> *proto) </p>
<p> void <code>globus_gass_transfer_proto_request_denied</code> (<code>globus_gass_transfer_request_t</code> request, int reason, char *message) </p>
<p> void <code>globus_gass_transfer_proto_request_referred</code> (<code>globus_gass_transfer_request_t</code> request, char **url, globus_size_t num_urls) </p>
<h2>Detailed Description</h2>
<p> Protocol Implementation API. </p>
<p> The GASS Protocol Module API is designed to make it possible to extend the GASS client and server APIs to support additional protocols without making any changes to the core of the GASS implementation. GASS protocol modules are intended to to handle protocol-specific connection and data handling. The GASS Transfer library includes protocol modules which implement the HTTP, HTTPS, FTP, and GSI-FTP protocols. </p>
<p> Every protocol module implementation must include the following header file: </p>
<pre><code>
#include "globus_gass_transfer_proto.h"
</code></pre>
<p> To implement a protocol module, one must create a <code>globus_gass_transfer_proto_descriptor_t</code> structure which indicates what the protocol module is able to do. This structure contains the URL scheme which the protocol module supports, and function pointers which indicate what type of operations (client or server) that the module implements. To implement a client-side protocol module, the new_requestattr and new_request fields must be set to the protocol module&#8217;s implementations of those functions. To implement a server-side protocol module, the new_listenerattr and new_listener functions must be set to the protocol module&#8217;s implementations of those functions. </p>
<p> A protocol module implementor registers a protocol module with the GASS Transfer library by calling the function <code>globus_gass_transfer_proto_register_protocol()</code>, and unregisters the module by calling <code>globus_gass_transfer_proto_unregister_protocol()</code>. This functions must be called after the <code>GLOBUS_GASS_TRANSFER_MODULE</code> has already been activated. Once registered, applications may use URLs of the scheme type provided by the protocol module for the standard <code>client</code> or <code>server</code> operations.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>globus_gass_transfer_listener_proto_s</code> <code>globus_gass_transfer_listener_proto_t</code></h3>
<p> Protocol module listener handling structure. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_listener_proto_s</code></dl>
<h3>typedef void(* globus_gass_transfer_proto_accept_t)(<code>globus_gass_transfer_listener_proto_t</code> *proto, globus_gass_transfer_listener_t listener, <code>globus_gass_transfer_request_t</code> request, globus_gass_transfer_requestattr_t *attr)</h3>
<p> Protocol module implementation function type for server request parsing. </p>
<p> Function pointers of this type are associated with the <code>globus_gass_transfer_listener_proto_t</code> associated with a particular listener handle. They are called when a server implementation wants to accept a new connection from the listener. A new request is generated based on the protocol-specific request done on the new connection. </p>
<p> The new request will be created with the attributes specified in the <i>attr</i> parameter. Once the protocol module has parsed the request, it must call <code>globus_gass_transfer_proto_new_listener_request()</code> to let the server implementation decide how to process this request. </p>
<p> The protocol module should update the <i>request</i> to indicate the type of operation being requested, the size of the file (if applicable), and the identity of the client (if applicable). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proto</i> The protocol specific listener data structure associated with the listener handle.<br />
 <i>listener</i> The listener handle which the user requested the listen on.<br />
 <i>request</i> The new request handle.<br />
 <i>attr</i> The request attribute set to be used when processing this request.</dl>
<h3>typedef int(* globus_gass_transfer_proto_create_listener_t)(globus_gass_transfer_listener_t listener, globus_gass_transfer_listenerattr_t *attr, char *scheme, char **base_url, <code>globus_gass_transfer_listener_proto_t</code> **proto)</h3>
<p> Protocol module implementation function type for new server listeners. </p>
<p> A function pointer of this type is associated with the <code>globus_gass_transfer_proto_descriptor_t</code> for a particular protocol module&#8217;s implementation. It is called when the server has called <code>globus_gass_transfer_create_listener()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> The listener handle to assocate with the new <i>proto</i> created by the protocol module.<br />
 <i>attr</i> A protocol-specific attribute set, created by calling the protocol module&#8217;s <code>new_listenerattr function pointer</code>.<br />
 <i>scheme</i> The URL scheme that the server has requested for the new listener. This will be one the scheme associated with a particular protocol module.<br />
 <i>base_url</i> A pointer to be set the value of the base url of this listener. For most protocols, this will contain the scheme, hostname, and port number of the listener. This string must be allocated using one of the memory allocators defined in the globus_common library. It will be freed by the GASS Transfer library when the listener is closed.<br />
 <i>proto</i> A pointer to be set to a new globus_gass_transfer_listener_proto_t which will be associated with this listener. This must be allocated by the protocol module using one of the memory allocators defined in the globus_common library. It will be freed by the GASS Transfer library when the listener is closed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A GASS error value, or GLOBUS_SUCCESS.</dl>
<h3>typedef void(* globus_gass_transfer_proto_func_t)(<code>globus_gass_transfer_request_proto_t</code> *proto, <code>globus_gass_transfer_request_t</code> request)</h3>
<p> Protocol module implementation function type. </p>
<p> Function pointers of this type are associated with the <code>globus_gass_transfer_request_proto_t</code> associated with a particular request handle. They are called when certain functions which modify the status of a request have been called by a client or server. </p>
<p> A function of this type is used for the fail, deny, refer, authorize, and destroy fields of the <code>globus_gass_transfer_request_proto_t</code>. A protocol module can query the request handle to determine the status and, if applicable, denial reasons if necessary. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proto</i> The protocol module&#8217;s request handler.<br />
 <i>request</i> The request handle.</dl>
<h3>typedef void(* globus_gass_transfer_proto_listener_t)(<code>globus_gass_transfer_listener_proto_t</code> *proto, globus_gass_transfer_listener_t listener)</h3>
<p> Protocol module implementation function type for server operations. </p>
<p> Function pointers of this type are associated with the <code>globus_gass_transfer_listener_proto_t</code> associated with a particular listener handle. They are called when a server implementation wants to close the listener, listen for new connections, or destroy the listener. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proto</i> The protocol-specific implementation of the <code>globus_gass_transfer_listener_proto_t</code> for a particular listener.<br />
 <i>listener</i> The listener handle associated with the <i>proto</i>.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_create_listener_t</code></dl>
<h3>typedef globus_object_t*(* globus_gass_transfer_proto_new_attr_t)(char *url_scheme)</h3>
<p> Protocol module implementation function type for attribute creation. </p>
<p> A function pointer of this type is associated with the <code>globus_gass_transfer_proto_descriptor_t</code> defining a protocol module. It is called when a client requests a new request attribute set be created for a URL scheme handled by a protocol module. The function implementation must create a new request attribute usuable by the protocol. </p>
<p> The returned attribute must be a globus object which inherits from one of the base attributes defined in the GASS Transfer API. A client or server operation will use a request attribute generated by this function when creating a new <code>globus_gass_transfer_request_proto_t</code> to handle a request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url_scheme</i> The URL scheme that the request attribute should be compatible with.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A globus_object_t-based request attribute.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_new_request_t</code>, <code>globus_gass_transfer_proto_accept_t</code></dl>
<h3>typedef void(* globus_gass_transfer_proto_new_request_t)(<code>globus_gass_transfer_request_t</code> request, globus_gass_transfer_requestattr_t *attr)</h3>
<p> Protocol module implementation function type for new client requests. </p>
<p> A function pointer of this type is associated with the <code>globus_gass_transfer_proto_descriptor_t</code> for a particular protocol module&#8217;s implementation. It is called when the client has begun a file transfer request by calling one of the functions in the &#8216;@ref globus_gass_transfer_client&#8217; section of this manual. </p>
<p> When this function is called for a protocol module, the module should query the request handle to determine the URL which is being requested by the client, and the operation being done on that URL. The protocol module should initiate the request, and once it has determined that it has been authorized, denied, or referred, one of <code>globus_gass_transfer_proto_request_ready()</code>, <code>globus_gass_transfer_proto_request_denied()</code>, or <code>globus_gass_transfer_proto_request_referred()</code> must be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle containing the information about the request.<br />
 <i>attr</i> A protocol-specific attribute set, created by calling the protocol module&#8217;s <code>new_requestattr function pointer</code>.</dl>
<h3>typedef void(* globus_gass_transfer_proto_receive_t)(<code>globus_gass_transfer_request_proto_t</code> *proto, <code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t bytes_length, globus_size_t wait_for_length)</h3>
<p> Protocol module function type to handle receiving data. </p>
<p> A function pointer of this type is associated with the <code>globus_gass_transfer_request_proto_t</code> associated with a request handle. It is called when client or server has registered a bytes array for receiving from the client or server which is handling the request. The GASS Transfer Library will only pass one <i>bytes</i> array to the protocol module for processing per request at any given time. </p>
<p> Once the protocol module has processed the array, it must call <code>globus_gass_transfer_proto_receive_complete()</code> to let the GASS Transfer library continue to process the request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proto</i> The protocol module&#8217;s request handler.<br />
 <i>request</i> The request handle with which this block of bytes is associated.<br />
 <i>bytes</i> The user-supplied byte array containing the data associated with the request.<br />
 <i>bytes_length</i> The length of the <i>bytes</i> array.<br />
 <i>wait_for_length</i> The minimum amount of data to receive before calling <code>globus_gass_transfer_proto_receive_complete()</code> for the request. The GASS Transfer protocol module may call that function with a smaller value for the amount received if EOF has been reached.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_receive_bytes()</code></dl>
<h3>typedef void(* globus_gass_transfer_proto_send_t)(<code>globus_gass_transfer_request_proto_t</code> *proto, <code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t send_length, globus_bool_t last_data)</h3>
<p> Protocol module function type to handle sending data. </p>
<p> A function pointer of this type is associated with the <code>globus_gass_transfer_request_proto_t</code> associated with a request handle. It is called when client or server has registered a bytes array for sending to the client or server which is handling the request. The GASS Transfer Library will only pass one <i>bytes</i> array to the protocol module for processing per request at any given time. </p>
<p> Once the protocol module has processed the array, it must call <code>globus_gass_transfer_proto_send_complete()</code> to let the GASS Transfer library continue to process the request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proto</i> The protocol module&#8217;s request handler.<br />
 <i>request</i> The request handle with which this block of bytes is associated.<br />
 <i>bytes</i> The user-supplied byte array containing the data associated with the request.<br />
 <i>bytes_length</i> The length of the <i>bytes</i> array.<br />
 <i>last_data</i> A flag to indicate whether this is the final block of data for the request. If this is true, then the <i>callback</i> function will be delayed until the server acknowledges that the file has been completely received.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_send_bytes()</code></dl>
<h3>typedef struct <code>globus_gass_transfer_request_proto_s</code> <code>globus_gass_transfer_request_proto_t</code></h3>
<p> Protocol module request handling structure. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_request_proto_s</code></dl>
<h2>Function Documentation</h2>
<h3>void globus_gass_transfer_proto_listener_ready (globus_gass_transfer_listener_tlistener)</h3>
<p> Server listener ready. </p>
<p> This function notifies the GASS Transfer Library that the protocol module has decided that a new request can be accepted on this particular listener. It must only be called after the GASS Transfer Library has called the <code>listen function</code> in a <code>globus_gass_transfer_listener_proto_t</code> protocol module-specific listener structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> The listener handle which is now ready for accepting a new connection.</dl>
<h3>void globus_gass_transfer_proto_new_listener_request (globus_gass_transfer_listener_tlistener, <code>globus_gass_transfer_request_t</code>request, <code>globus_gass_transfer_request_proto_t</code> *proto)</h3>
<p> New listener request. </p>
<p> This function notifies the GASS Transfer Library that new request generated by a server calling the <code>globus_gass_transfer_register_accept()</code> function has begun processing in a protocol module, and that protocol module is now ready to send or receive data to handle this request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> The listener handle used to accept this request.<br />
 <i>request</i> The request handle used for this request. This was created by the user calling one of the functions in the &#8216;@ref<br />
&nbsp;<wbr>globus_gass_transfer_client&#8217;&nbsp;<wbr>section of this manual.&nbsp;<wbr><br />
 <i>proto</i> The protocol-module specific request structure. This structure contains a set of function pointers to allow GASS to continue to process this request.</dl>
<h3>void globus_gass_transfer_proto_receive_complete (<code>globus_gass_transfer_request_t</code>request, globus_byte_t *bytes, globus_size_tnbytes, globus_bool_tfailed, globus_bool_tlast_data)</h3>
<p> Data receive complete. </p>
<p> A protocol module must call this function once a byte range registered for receive via the protocol module&#8217;s recv_buffer method has been completely processed. This function is called for protocol modules implementing either server or client functionality. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle associated with this byte array.<br />
 <i>bytes</i> The byte array which was received into. This should be the same as the pointer passed in the send_buffer method.<br />
 <i>nbytes</i> The number of bytes which were sent from this byte array. This may be different than length passed to the send_buffer method if an error occurred or EOF was reached while receiving the data.<br />
 <i>failed</i> A boolean indicating whether this byte range was successfully received or not. This should be set to <i>GLOBUS_TRUE</i> if either a protocol error or a user-generated abort has occurred while processing the byte range. If this is set to <i>GLOBUS_TRUE</i>, then the <i>last_data</i> parameter must also be set to <i>GLOBUS_TRUE</i>.<br />
 <i>last_data</i> A boolean indicating whether this byte range was the final one which can be processed for this request. This should be set to <i>GLOBUS_TRUE</i> if an error occurred while processing this byte range, and user-generated abort occurred, or this is the final byte range in the data transfer.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_send_bytes()</code></dl>
<h3>int globus_gass_transfer_proto_register_protocol (<code>globus_gass_transfer_proto_descriptor_t</code> *proto_desc)</h3>
<p> Register protocol. </p>
<p> This function registers a protocol module handler with the GASS Transfer library. If this succeeds, then users of the library may use the URLs with the protocol scheme implemented by this module descriptor in GASS Transfer operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proto_desc</i> The protocol module descriptor. See the &#8216;@ref<br />
&nbsp;<wbr>globus_gass_transfer_protocol&#8217;&nbsp;<wbr>section of the manual for information on this structure.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The protocol module was successfully registered with GASS.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>proto_desc</i> parameter was <i>GLOBUS_NULL</i>.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_ALREADY_REGISTERED</i> A protocol module has already been registered with GASS to handle this URL scheme.</dl>
<h3>void globus_gass_transfer_proto_request_denied (<code>globus_gass_transfer_request_t</code>request, intreason, char *message)</h3>
<p> Request denied. </p>
<p> This function notifies the GASS Transfer Library that new request generated by a client calling one of the functions in the &#8216;@ref globus_gass_transfer_client&#8217; section of the manual has been denied by the server, and so cannot be processed by the protocol module. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle used for this request. This was created by the user calling one of the functions in the &#8216;@ref<br />
&nbsp;<wbr>globus_gass_transfer_client&#8217;&nbsp;<wbr>section of this manual.&nbsp;<wbr><br />
 <i>reason</i> A protocol-specific reason code.<br />
 <i>message</i> A string containing a message describing why the request was denied. The GASS Transfer library is responsible for freeing this message. It must be allocated using one of the memory allocators defined in the Globus Common Library.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_request_ready()</code>, <code>globus_gass_transfer_proto_request_referred()</code></dl>
<h3>void globus_gass_transfer_proto_request_ready (<code>globus_gass_transfer_request_t</code>request, <code>globus_gass_transfer_request_proto_t</code> *proto)</h3>
<p> Request ready. </p>
<p> This function notifies the GASS Transfer Library that new request generated by a client has begun processing in a protocol module, and that protocol module is now ready to send or receive data to handle this request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle used for this request. This was created by the user calling one of the functions in the &#8216;@ref<br />
&nbsp;<wbr>globus_gass_transfer_client&#8217;&nbsp;<wbr>section of this manual.&nbsp;<wbr><br />
 <i>proto</i> The protocol-module specific request structure. This structure contains a set of function pointers to allow GASS to continue to process this request.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_request_referred()</code>, <code>globus_gass_transfer_proto_request_denied()</code></dl>
<h3>void globus_gass_transfer_proto_request_referred (<code>globus_gass_transfer_request_t</code>request, char **url, globus_size_tnum_urls)</h3>
<p> Request referred. </p>
<p> This function notifies the GASS Transfer Library that new request generated by a client calling one of the functions in the &#8216;@ref globus_gass_transfer_client&#8217; section of the manual has been referred to another URL by the server, and so processing has stopped. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle used for this request. This was created by the user calling one of the functions in the &#8216;@ref<br />
&nbsp;<wbr>globus_gass_transfer_client&#8217;&nbsp;<wbr>section of this manual.&nbsp;<wbr><br />
 <i>url</i> An array of url strings containing alternate locations for this file. The GASS transfer library is responsible for freeing this array. It must be allocated using one of the memory allocators defined in the Globus Common Library.<br />
 <i>num_urls</i> The length of the <i>url</i> array.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_proto_request_ready()</code>, <code>globus_gass_transfer_proto_request_denied()</code>, <code>globus_gass_transfer_proto_request_referred()</code></dl>
<h3>void globus_gass_transfer_proto_send_complete (<code>globus_gass_transfer_request_t</code>request, globus_byte_t *bytes, globus_size_tnbytes, globus_bool_tfailed, globus_bool_tlast_data)</h3>
<p> Data send complete. </p>
<p> A protocol module must call this function once a byte range registered for sending via the protocol module&#8217;s send_buffer method has been completely processed. This function is called for protocol modules implementing either server or client functionality. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle associated with this byte array.<br />
 <i>bytes</i> The byte array which was sent. This should be the same as the pointer passed in the send_buffer method.<br />
 <i>nbytes</i> The number of bytes which were sent from this byte array. This may be different than length passed to the send_buffer method if an error occurred.<br />
 <i>failed</i> A boolean indicating whether this byte range was successfully sent or not. This should be set to <i>GLOBUS_TRUE</i> if either a protocol error or a user-generated abort has occurred while processing the byte range. If this is set to <i>GLOBUS_TRUE</i>, then the <i>last_data</i> parameter must also be set to <i>GLOBUS_TRUE</i>.<br />
 <i>last_data</i> A boolean indicating whether this byte range was the final one which can be processed for this request. This should be set to <i>GLOBUS_TRUE</i> if an error occurred while processing this byte range, and user-generated abort occurred, or this is the final byte range in the data transfer.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_send_bytes()</code></dl>
<h3>int globus_gass_transfer_proto_unregister_protocol (<code>globus_gass_transfer_proto_descriptor_t</code> *proto_desc)</h3>
<p> Unregister protocol. </p>
<p> This function unregisters a protocol module handler from the GASS Transfer library. If this succeeds, then users of the library may no longer user URLs with the protocol scheme implemented by this module descriptor in GASS Transfer operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proto_desc</i> The protocol module descriptor. See the &#8216;@ref<br />
&nbsp;<wbr>globus_gass_transfer_protocol&#8217;&nbsp;<wbr>section of the manual for information on this structure.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The protocol module was successfully registered with GASS.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>proto_desc</i> parameter was <i>GLOBUS_NULL</i>.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> A protocol module has not been registered with GASS to handle this URL scheme.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAR">Function Documentation</a></p>
<dd>
<dt><a href="#lbBB">Author</a></p>
<dd></dl>
