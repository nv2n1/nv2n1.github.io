---
title: "globus_gass_transfer_create_listener(3)"
name: "globus_gass_transfer_create_listener"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_create_listener/"
description: "Implementing Servers –"
---

<h2 class="name">NAME</h2>
<p> Implementing Servers &#8211; </p>
<p> GASS Server Implementation.</p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_gass_transfer_close_callback_t</code> )(void *callback_arg, globus_gass_transfer_listener_t listener) </p>
<p> typedef void(* <code>globus_gass_transfer_listen_callback_t</code> )(void *callback_arg, globus_gass_transfer_listener_t listener) </p>
<h3>Functions</h3>
<p> int <code>globus_gass_transfer_create_listener</code> (globus_gass_transfer_listener_t *listener, globus_gass_transfer_listenerattr_t *attr, char *scheme) </p>
<p> int <code>globus_gass_transfer_close_listener</code> (globus_gass_transfer_listener_t listener, <code>globus_gass_transfer_close_callback_t</code> callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_register_listen</code> (globus_gass_transfer_listener_t listener, <code>globus_gass_transfer_listen_callback_t</code> callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_register_accept</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, globus_gass_transfer_listener_t listener, globus_gass_transfer_callback_t callback, void *user_arg) </p>
<p> void * <code>globus_gass_transfer_listener_get_user_pointer</code> (globus_gass_transfer_listener_t listener) </p>
<p> int <code>globus_gass_transfer_listener_set_user_pointer</code> (globus_gass_transfer_listener_t listener, void *user_pointer) </p>
<p> char * <code>globus_gass_transfer_listener_get_base_url</code> (globus_gass_transfer_listener_t listener) </p>
<p> int <code>globus_gass_transfer_refer</code> (<code>globus_gass_transfer_request_t</code> request, char **urls, globus_size_t num_urls) </p>
<p> int <code>globus_gass_transfer_authorize</code> (<code>globus_gass_transfer_request_t</code> request, globus_size_t total_length) </p>
<p> int <code>globus_gass_transfer_deny</code> (<code>globus_gass_transfer_request_t</code> request, int reason, char *message) </p>
<h2>Detailed Description</h2>
<p> GASS Server Implementation. </p>
<p> Another mode of using the GASS Transfer API is to implement data servers. The primary difference between the client and server parts of the GASS Transfer API are how requests are generated. </p>
<p> To implement a server, the user would call <code>globus_gass_transfer_create_listener()</code> to create a new server port on which a specific protocol will be used to request file transfer operations. The user may obtain the URL that the listener is bound to by calling <code>globus_gass_transfer_listener_get_base_url()</code>. </p>
<p> Once the listener is created, the user can call <code>globus_gass_transfer_register_listen()</code> to wait for clients to connect to it. Once the server has detected an attempt to connect by a client, the use can call <code>globus_gass_transfer_register_accept()</code> to accept the connection from the client and parse the request. </p>
<p> In the callback associated with <code>globus_gass_transfer_register_accept()</code>, the server can decide how to process the request. The user may choose to authorize the request by calling <code>globus_gass_transfer_authorize()</code>, refer it to another URL or URLs by calling <code>globus_gass_transfer_refer()</code> or deny the client access to the URL by calling <code>globus_gass_transfer_deny()</code>.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_gass_transfer_close_callback_t)(void *callback_arg, globus_gass_transfer_listener_t listener)</h3>
<p> Listener close callback </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_arg</i><br />
 <i>listener</i></dl>
<h3>typedef void(* globus_gass_transfer_listen_callback_t)(void *callback_arg, globus_gass_transfer_listener_t listener)</h3>
<p> Listen callback. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_arg</i><br />
 <i>listener</i></dl>
<h2>Function Documentation</h2>
<h3>int globus_gass_transfer_authorize (<code>globus_gass_transfer_request_t</code>request, globus_size_ttotal_length)</h3>
<p> Authorize a request. </p>
<p> This function causes the request to be authorized for processing. It should be called in response to a request accept callback when the server wants to agree to process this request. After calling this function, the server implementation should call <code>globus_gass_transfer_send_bytes()</code> or <code>globus_gass_transfer_receive_bytes()</code> to send or receive the data associated with the URL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A new request handle, passed to the server in an accept callback.<br />
 <i>total_length</i> For a &#8216;get&#8217; request, the total_length of the file to be retrieved if known. This value may be GLOBUS_GASS_LENGTH_UNKNOWN if the protocol supports transferring arbitrarily-sized files.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> The request handle was not valid, not created by calling <code>globus_gass_transfer_register_accept()</code>, or has already been denied or authorized.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> The protocol module does not support authorizing requests.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_refer()</code>, <code>globus_gass_transfer_deny()</code></dl>
<h3>int globus_gass_transfer_close_listener (globus_gass_transfer_listener_tlistener, <code>globus_gass_transfer_close_callback_t</code>callback, void *user_arg)</h3>
<p> Close a GASS listener. </p>
<p> This function calls the protocol specific function needed to close a GASS server listener port. Callbacks for any outstanding accepts will be called before the close callback is invoked. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> Listener handle created by calling <code>globus_gass_transfer_create_listener()</code>.<br />
 <i>callback</i> Function to call once the listener handle has been closed.<br />
 <i>user_arg</i> Argument to be passed to the <i>callback</i> function.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The close operation was successfully registered on the listener.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> The listener handle was invalid.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_INITIALIZED</i> The listener handle was not properly initialized.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_DONE</i> A close has already been registered on the listener.</dl>
<h3>int globus_gass_transfer_create_listener (globus_gass_transfer_listener_t *listener, globus_gass_transfer_listenerattr_t *attr, char *scheme)</h3>
<p> Create a new protocol-specific listener socket for a GASS server. </p>
<p> This function creates a new socket to listen for client connections as a GASS server. The listener handle pointer is initialized to contain the a new handle which can be used in subsequent server operations. </p>
<p> After calling this function, a user may call the <code>globus_gass_transfer_register_listen()</code> or <code>globus_gass_transfer_close_listener()</code> functions with this listener handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> A new listener handle to initialize.<br />
 <i>attr</i> Protocol-specific attributes for the new listener.<br />
 <i>scheme</i> The protocol scheme to implement for the listener.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The listener was successfully created.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>listener</i> or <i>scheme</i> parameter was NULL<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> The <i>scheme</i> is not supported by any protocol module.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_MALLOC_FAILED</i> Data structures associated with the transfer could not be allocated.</dl>
<h3>int globus_gass_transfer_deny (<code>globus_gass_transfer_request_t</code>request, intreason, char *message)</h3>
<p> Deny a request. </p>
<p> This function causes the request to be denied for further processing. It should be called in response to a request ccept callback when the server wants to refuse processing this request for the client. After calling this function, the server implementation need do nothing further with the request handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A new request handle, passed to the server in an accept callback.<br />
 <i>reason</i> A protocol-specific reason code.<br />
 <i>message</i> An informational message to be sent to the client.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> The request handle was not valid, not created by calling <code>globus_gass_transfer_register_accept()</code>, or has already been denied or authorized.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> The protocol module does not support denying requests.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_refer()</code>, <code>globus_gass_transfer_authorize()</code></dl>
<h3>char* globus_gass_transfer_listener_get_base_url (globus_gass_transfer_listener_tlistener)</h3>
<p> Get the base URL of a listener. </p>
<p> This function queries a listener handle for the base URL which the server is listening on. For most protocols, this contains the protocol scheme, host, and port that the listener has registered itself on. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> The listener handle to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns a pointer to a string containing the base URL. This string must not be freed or modified by the caller. It may not be referred to after the function globus_gass_transfer_listener_close() has been called.</dl>
<h3>void* globus_gass_transfer_listener_get_user_pointer (globus_gass_transfer_listener_tlistener)</h3>
<p> Get the user pointer associated with a listener. </p>
<p> This function will query the listener&#8217;s user_pointer field and return it&#8217;s value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> The listener handle.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> If the listener handle is invalid or the user_pointer&#8217;s value has not been set, then GLOBUS_NULL will be returned. Otherwise, the value of the user pointer will be returned.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_listener_set_user_pointer()</code></dl>
<h3>int globus_gass_transfer_listener_set_user_pointer (globus_gass_transfer_listener_tlistener, void *user_pointer)</h3>
<p> Set the user pointer associated with a listener. </p>
<p> This function will set the listener&#8217;s user_pointer field. The pointer may be used to associate any pointer-sized data with a listener handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> The listener handle.<br />
 <i>user_pointer</i> The value of the user pointer.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The user pointer was successfully set.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> The <i>listener</i> handle was invalid.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_listener_get_user_pointer()</code></dl>
<h3>int globus_gass_transfer_refer (<code>globus_gass_transfer_request_t</code>request, char **urls, globus_size_tnum_urls)</h3>
<p> Refer a request. </p>
<p> This function causes the request to be referred to another URL or list of URLs. It should be called in response to a request accept callback when the server wants to refer the client to another server or servers to process the request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A new request handle, passed to the server in an accept callback.<br />
 <i>urls</i> An array of strings, each being a URL pointing to sources of the same data as the original URL.<br />
 <i>num_urls</i> The length of the <i>urls</i> array.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> The request handle was not valid, not created by calling <code>globus_gass_transfer_register_accept()</code>, or has already been denied or authorized.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> The protocol module does not support referrals.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_deny()</code>, <code>globus_gass_transfer_authorize()</code></dl>
<h3>int globus_gass_transfer_register_accept (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, globus_gass_transfer_listener_tlistener, globus_gass_transfer_callback_tcallback, void *user_arg)</h3>
<p> Accept new client connections. </p>
<p> This function causes the listener handle to accept a new connection on the listener and parse the file request. Once the file request has been parsed, the specified <i>callback</i> function will be called. The server implementation must then either authorize, deny, or refer this request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A pointer to a new request handle. This request handle will be initialized when the callback function is invoked.<br />
 <i>attr</i> Request attributes.<br />
 <i>listener</i> The listener handle to register for the new request.<br />
 <i>callback</i> Function to call when the protocol module has parsed the file request.<br />
 <i>user_arg</i> Argument to be passed to the callback function.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The listen callback has been registered with the protocol module.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> An invalid <i>listener</i> handle was passed to this function.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_INITIALIZED</i> An uninitialized <i>listener</i> handle was passed to this function.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INTERNAL_ERROR</i> The request could not be initialized due to some internal resource depletion.<br />
 <i>GLOBUS_GASS_NOT_REGISTERED.</i> The <code>globus_gass_transfer_register_listen()</code> function has not yet been called.<br />
 <i>GLOBUS_GASS_ALREADY_REGISTERED.</i> The listener is already processing a new request.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_DONE</i> The listener has been registered for closing.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_register_listen()</code>;</dl>
<h3>int globus_gass_transfer_register_listen (globus_gass_transfer_listener_tlistener, <code>globus_gass_transfer_listen_callback_t</code>callback, void *user_arg)</h3>
<p> Listen for new client connections. </p>
<p> This function causes the listener handle to listen for new client connections. When one is ready, it calls the specified <i>callback</i> function, letting the server implementer continue to accept the connection and process the request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> The listener handle to register for new connections.<br />
 <i>callback</i> Function to call when a new connection may be accepted.<br />
 <i>user_arg</i> Argument to be passed to the callback function.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The listen callback has been registered with the protocol module.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> An invalid <i>listener</i> handle was passed to this function.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_INITIALIZED</i> An uninitialized <i>listener</i> handle was passed to this function.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_ALREADY_REGISTERED</i> The listener has already been registered for a new connection.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_DONE</i> The listener has been registered for closing.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_register_accept()</code>;</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAT">Author</a></p>
<dd></dl>
