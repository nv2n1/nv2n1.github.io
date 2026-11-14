---
title: "globus_gass_transfer_send_bytes(3)"
name: "globus_gass_transfer_send_bytes"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_send_bytes/"
description: "Sending and Receiving Data –"
---

<h2 class="name">NAME</h2>
<p> Sending and Receiving Data &#8211; </p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_gass_transfer_bytes_callback_t</code> )(void *arg, <code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t length, globus_bool_t last_data) </p>
<h3>Functions</h3>
<p> int <code>globus_gass_transfer_send_bytes</code> (<code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t send_length, globus_bool_t last_data, <code>globus_gass_transfer_bytes_callback_t</code> callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_receive_bytes</code> (<code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t max_length, globus_size_t wait_for_length, <code>globus_gass_transfer_bytes_callback_t</code> callback, void *user_arg) </p>
<h2>Detailed Description</h2>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_gass_transfer_bytes_callback_t)(void *arg, <code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t length, globus_bool_t last_data)</h3>
<p> Byte send or receive callback function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>arg</i> The user_arg passed to the function which registered this callback. The user may use this value for any purpose.<br />
 <i>request</i> The request handle associated with this byte array.<br />
 <i>bytes</i> The byte array which was sent or received.<br />
 <i>length</i> The length of data which was sent or received.<br />
 <i>last_data</i> Boolean flag whether this is the final byte array for this request.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_send_bytes()</code>, <code>globus_gass_transfer_receive_bytes()</code></dl>
<h2>Function Documentation</h2>
<h3>int globus_gass_transfer_receive_bytes (<code>globus_gass_transfer_request_t</code>request, globus_byte_t *bytes, globus_size_tmax_length, globus_size_twait_for_length, <code>globus_gass_transfer_bytes_callback_t</code>callback, void *user_arg)</h3>
<p> Receive a byte array associated with a request handle. </p>
<p> This function receives a block of data from a server or client as part of the processing for a request. Multiple data blocks may be registered with the GASS transfer library at once. </p>
<p> When processing a server request, this function may only be used in conjunction with &#8216;put&#8217; or &#8216;append&#8217; requests. The user must call <code>globus_gass_transfer_authorize()</code> before calling this function. </p>
<p> When processing a client request, this function may only be used in conjunction with &#8216;get&#8217; requests. This function may not be called before either the callback function has been invoked, or the blocking globus_gass_tranfser_put() or <code>globus_gass_transfer_append()</code> function has returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle with which this block of bytes is associated.<br />
 <i>bytes</i> A user-supplied buffer containing the data associated with the request.<br />
 <i>max_length</i> The length of the <i>bytes</i> array.<br />
 <i>wait_for_length</i> The minimum amount of data to wait for before invoking the <i>callback</i> function. A partial byte array of at least this amount will be returned in the callback, unless end-of-file is reached before this amount.<br />
 <i>callback</i> Function to call once the <i>bytes</i> array has been received.<br />
 <i>user_arg</i> Argument to be passed to the <i>callback</i> function.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The <i>bytes</i> array was successfully registered with the GASS transfer library. The <i>callback</i> function will be invoked once it has been received.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>bytes</i> or <i>callback</i> parameter was NULL.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USER</i> The <i>request</i> was invalid, or it is not one on which bytes can be sent.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_INITIALIZED</i> The callback to a non-blocking file request has not been invoked yet, a blocking file request has not returned, or the request has not yet been authorized.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_REQUEST_FAILED</i> The <i>request</i> has failed by either the client, server, or protocol module implementation.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_DONE</i> The <i>request</i> has already been completed.</dl>
<h3>int globus_gass_transfer_send_bytes (<code>globus_gass_transfer_request_t</code>request, globus_byte_t *bytes, globus_size_tsend_length, globus_bool_tlast_data, <code>globus_gass_transfer_bytes_callback_t</code>callback, void *user_arg)</h3>
<p> Send a byte array associated with a request handle. </p>
<p> This function sends a block of data to a server or client as part of the processing for a request. Multiple data blocks may be registered with the GASS transfer library at once. </p>
<p> When processing a server request, this function may only be used in conjunction with &#8216;get&#8217; requests. The user must call <code>globus_gass_transfer_authorize()</code> before calling this function. </p>
<p> When processing a client request, this function may only be used in conjunction with &#8216;put&#8217; or &#8216;append&#8217; requests. This function may not be called before either the callback function has been invoked, or the blocking globus_gass_tranfser_put() or <code>globus_gass_transfer_append()</code> function has returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle with which this block of bytes is associated.<br />
 <i>bytes</i> A user-supplied buffer containing the data associated with the request.<br />
 <i>send_length</i> The length of the <i>bytes</i> array.<br />
 <i>last_data</i> A flag to indicate whether this is the final block of data for the request. If this is true, then the <i>callback</i> function will be delayed until the server acknowledges that the file has been completely received.<br />
 <i>callback</i> Function to call once the <i>bytes</i> array has been sent.<br />
 <i>user_arg</i> Argument to be passed to the <i>callback</i> function.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The <i>bytes</i> array was successfully registered with the GASS transfer library. The <i>callback</i> function will be invoked once it has been sent.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>bytes</i> or <i>callback</i> parameter was NULL.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USER</i> The <i>request</i> was invalid, or it is not one on which bytes can be sent.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_INITIALIZED</i> The callback to a non-blocking file request has not been invoked yet, a blocking file request has not returned, or the request has not yet been authorized.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_REQUEST_FAILED</i> The <i>request</i> has failed by either the client, server, or protocol module implementation.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_DONE</i> The <i>request</i> has already been completed.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
