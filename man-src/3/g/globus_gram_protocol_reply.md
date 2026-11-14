---
title: "globus_gram_protocol_reply(3)"
name: "globus_gram_protocol_reply"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_protocol_reply/"
description: "Message I/O –"
---

<h2 class="name">NAME</h2>
<p> Message I/O &#8211; </p>
<p> Mesage I/O.</p>
<h3>Typedefs</h3>
<p> typedef unsigned long <code>globus_gram_protocol_handle_t</code><br />
 <i>Unique GRAM protocol identifier. </i><br />
 typedef struct<br />
 globus_gram_protocol_hash_entry_s <code>globus_gram_protocol_extension_t</code>&quot;<br />
 <i>GRAM protocol extension attribute-value pair. </i></p>
<h3>Functions</h3>
<p> int <code>globus_gram_protocol_setup_attr</code> (globus_io_attr_t *attr)<br />
 <i>Create default I/O attribute for GRAM. </i><br />
 globus_bool_t <code>globus_gram_protocol_authorize_self</code> (gss_ctx_id_t context)<br />
 <i>Determine if a GSSAPI context has the same source and target identities. </i><br />
 int <code>globus_gram_protocol_allow_attach</code> (char **url, globus_gram_protocol_callback_t callback, void *callback_arg)<br />
 <i>Create a GRAM protocol service listener. </i><br />
 int <code>globus_gram_protocol_callback_disallow</code> (char *url)<br />
 <i>Stop a GASS protocol listener from handling new requests. </i><br />
 int <code>globus_gram_protocol_post</code> (const char *url, <code>globus_gram_protocol_handle_t</code> *handle, globus_io_attr_t *attr, globus_byte_t *message, globus_size_t message_size, globus_gram_protocol_callback_t callback, void *callback_arg)<br />
 <i>Post a GRAM protocol request to a GRAM server. </i><br />
 int <code>globus_gram_protocol_post_delegation</code> (const char *url, <code>globus_gram_protocol_handle_t</code> *handle, globus_io_attr_t *attr, globus_byte_t *message, globus_size_t message_size, gss_cred_id_t cred_handle, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 req_flags, OM_uint32 time_req, globus_gram_protocol_callback_t callback, void *callback_arg)<br />
 <i>Post a GRAM protocol delegation request to a GRAM server. </i><br />
 int <code>globus_gram_protocol_reply</code> (<code>globus_gram_protocol_handle_t</code> handle, int code, globus_byte_t *message, globus_size_t message_size)<br />
 <i>Reply to a GRAM protocol message. </i><br />
 int <code>globus_gram_protocol_accept_delegation</code> (<code>globus_gram_protocol_handle_t</code> handle, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 req_flags, OM_uint32 time_req, globus_gram_protocol_delegation_callback_t callback, void *arg)<br />
 <i>Perform the server-side of the GSSAPI delegation handshake to receive a new delegated credential. </i><br />
 int <code>globus_gram_protocol_get_sec_context</code> (<code>globus_gram_protocol_handle_t</code> handle, gss_ctx_id_t *context)<br />
 <i>Get a reference to the GSSAPI security context associated with a GRAM protocol handle. </i></p>
<h2>Detailed Description</h2>
<p> Mesage I/O. </p>
<p> The functions in this section are related to sending and receiving GRAM protocol messages.</p>
<h2>Typedef Documentation</h2>
<h3><code>globus_gram_protocol_extension_t</code></h3>
<p> GRAM protocol extension attribute-value pair. The <i>globus_gram_protocol_extension_t</i> data type contains an attribute value pair that represents an extension to the GRAM2 protocol.</p>
<h3><code>globus_gram_protocol_handle_t</code></h3>
<p> Unique GRAM protocol identifier. The <i></i><code>globus_gram_protocol_handle_t</code> data type is used by functions in the GRAM protocol API as a unique discriminant between instances of a callback invocation. </p>
<p> There are no public functions that operate on these handles. They are used as identifiers for callback functions.</p>
<h2>Function Documentation</h2>
<h3>int globus_gram_protocol_accept_delegation (<code>globus_gram_protocol_handle_t</code>handle, gss_OID_setrestriction_oids, gss_buffer_set_trestriction_buffers, OM_uint32req_flags, OM_uint32time_req, globus_gram_protocol_delegation_callback_tcallback, void *arg)</h3>
<p> Perform the server-side of the GSSAPI delegation handshake to receive a new delegated credential. The <code>globus_gram_protocol_accept_delegation()</code> function performs the service side accepting of a GRAM protocol delegation exchange with a GRAM protocol client. This is performed after the delegation HTTP message has been unpacked by the application. </p>
<p> The <code>globus_gram_protocol_accept_delegation()</code> function returns after processing the GSSAPI handshake, passing the delegated credential or error information to the function pointed to by the <i>callback</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A GRAM protocol handle on which the server received a protocol refresh message.<br />
 <i>restriction_oids</i> A set of OID values indicating the data in the <i>restriction_buffers</i> parameter. This parameter may have the value GSS_C_NO_OID_SET if there are no restriction buffers.<br />
 <i>restriction_buffers</i> A set of binary data buffers which will be included in the delegated credential. The type of data in these buffers is determined by the OID values in <i>restriction_oids</i>. This parameter may have the value GSS_C_EMPTY_BUFFER_SET if there are no extra restrictions to be added to the credential.<br />
 <i>req_flags</i> A bitwise-or of GSSAPI flag values to use when delegating the credential using gss_init_delegation().<br />
 <i>time_req</i> An integer value indicating the length of time (in seconds) that the delegated credential should be valid for. This is an advisory parameter: no error will be returned if a credential with the requested lifetime can not be created.<br />
 <i>callback</i> A pointer to a function to call when the delegation handshake has completed or failed. This function will be passed the value of <i>arg</i> as well as the handle and delegated credential or erorr that occurred processing the delegation messages.<br />
 <i>arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>callback</i> as its first parameter. This may be NULL if the application has a NULL <i>callback</i> or does not require the pointer to establish its context in the callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_accept_delegation()</code> returns GLOBUS_SUCCESS and registers the function pointed to by <i>callback</i> to be called after the delegation completes or fails. If an error occurs, <code>globus_gram_protocol_accept_delegation()</code> returns an integer error code and the <i>callback</i> function is not registered.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_MALLOC_FAILED</i> Malloc failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_protocol_allow_attach (char **url, globus_gram_protocol_callback_tcallback, void *callback_arg)</h3>
<p> Create a GRAM protocol service listener. The <code>globus_gram_protocol_allow_attach()</code> function creates a GRAM protocol listener to which other processes can send GRAM protocol messages. The listener will automatically accept new connections on it&#8217;s TCP/IP port and parse GRAM requests. The requests will be passed to the function pointed to by the <i>callback</i> parameter for the application to unpack, handle, and send a reply by calling <code>globus_gram_protocol_reply()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url</i> An output parameter that will be initialized to point to a string that will hold the URL of the new listener. This URL may be published or otherwise passed to applications which need to contact this GRAM protocol server. The URL will be of the form <i><a rel="nofollow" href="https://host:port/">https://host:port/</a></i>.<br />
 <i>callback</i> A pointer to a function to be called when a new request has been received by this listener. This function will be passed the request, which may be unpacked using one of the functions described in the <code>message packing </code> section of the documentation.<br />
 <i>callback_arg</i> A pointer to arbitrary user data which will be passed to the callback function as its first parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_allow_attach()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>url</i> parameter to point to a newly allocated string. The caller is then responsible for freeing this string. If an error occurs, an integer error code will be returned and the <i>url</i> parameter value will be uninitialized.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_protocol_callback_disallow()</code></dl>
<h3>globus_bool_t globus_gram_protocol_authorize_self (gss_ctx_id_tcontext)</h3>
<p> Determine if a GSSAPI context has the same source and target identities. The <code>globus_gram_protocol_authorize_self()</code> function implements a predicate which returns true if the source and destination identities used to establish the GSSAPI security context are the same. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A GSSAPI security context which has been previously established. The source and target names of this context will be inspected by this function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> If the source and target identiies are the same, then <i></i><code>globus_gram_protocol_authorize_self()</code> returns <i>GLOBUS_TRUE</i>, otherwise, this function returns <i>GLOBUS_FALSE</i>.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_TRUE</i> The source and target identities are the same.<br />
 <i>GLOBUS_FALSE</i> The source and target identities are not the same or this function is unabled to inspect the security context.</dl>
<h3>int globus_gram_protocol_callback_disallow (char *url)</h3>
<p> Stop a GASS protocol listener from handling new requests. The <code>globus_gram_protocol_callback_disallow()</code> function stops the listener named by the value of the <i>url</i> parameter from receiving any new requests. It also frees memory used internally by the GRAM protocol implementation to handle requests for this listener. </p>
<p> The <code>globus_gram_protocol_callback_disallow()</code> function will wait until all requests being processed by this listener have completed processing. Once <code>globus_gram_protocol_callback_disallow()</code> returns, no further request callbacks will occur for the listener. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url</i> A pointer to the URL string which names the listener to disable.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_protocol_callback_disallow()</code> function returns <i>GLOBUS_SUCCESS</i> and frees internal state associated with the listener named by the <i>url</i> parameter. If an error occurs, its integer error code value will be returned and no listener will be affected.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_CALLBACK_NOT_FOUND</i> Callback not found</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_protocol_allow_attach()</code></dl>
<h3>int globus_gram_protocol_get_sec_context (<code>globus_gram_protocol_handle_t</code>handle, gss_ctx_id_t *context)</h3>
<p> Get a reference to the GSSAPI security context associated with a GRAM protocol handle. The <i></i><code>globus_gram_protocol_get_sec_context()</code> function retrieves a reference to the GSSAPI security context associated with a particular GRAM protocol handle. This context may be inspected by the caller but must not be destroyed by the caller. The <i></i><code>globus_gram_protocol_get_sec_context()</code> function must only be called after the GRAM protocol library has called the <i>callback</i> function associated with a GRAM protocol message exchange. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The GRAM protocol handle associated with a GRAM protocol message exchange.<br />
 <i>context</i> The GSSAPI security context associated with the protocol handle.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <i></i><code>globus_gram_protocol_get_sec_context()</code> returns GLOBUS_SUCCESS and modifies the <i>context</i> parameter to point to the security context associated with the <i>handle</i> parameter. If an error occurs, an interger error code is returned and the value of the <i>context</i> parameter is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request</dl>
<h3>int globus_gram_protocol_post (const char *url, <code>globus_gram_protocol_handle_t</code> *handle, globus_io_attr_t *attr, globus_byte_t *message, globus_size_tmessage_size, globus_gram_protocol_callback_tcallback, void *callback_arg)</h3>
<p> Post a GRAM protocol request to a GRAM server. The <code>globus_gram_protocol_post()</code> function initiates a GRAM protocol message exchange with a GRAM protocol listener. It returns after framing the message and initiating the connection. When the message exchange is complete, the function pointed to by <i>callback</i> is invoked either in another thread or when a non-threaded application calls the globus_poll() or globus_cond_wait() functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url</i> A pointer to a string containing the URL of the server to post the request to. This URL must be an HTTPS URL naming a GRAM service resource.<br />
 <i>handle</i> A pointer to a <i>globus_gram_protocol_handle_t</i> which will be initialized with a unique handle identifier. This identifier will be passed to the <i>callback</i> function to allow the caller to differentiate replies to multiple GRAM Protocol requests. This pointer may be NULL if the caller will not have multiple simultaneous requests.<br />
 <i>attr</i> A pointer to a Globus I/O attribute set, which will be used as parameters when connecting to the GRAM server. The value of <i>attr</i> may be NULL, in which case, the default GRAM Protocol attributes will be used (authentication to self, SSL-compatible transport, with message integrity).<br />
 <i>message</i> A pointer to a message string to be sent to the GRAM server. This is normally created by calling one of the GRAM Protocol <code>pack </code> functions. This message need not be NULL terminated as the length is passed in the <i>message_size</i> parameter.<br />
 <i>message_size</i> The length of the <i>message</i> string. Typically generated as one of the output parameters to one of the GRAM Protocol <code>pack </code> functions.<br />
 <i>callback</i> A pointer to a function to call when the response to this message is received or the message exchange fails. This may be NULL, in which case no callback will be received, and the caller will be unable to verify whether the message was successfully received.<br />
 <i>callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>callback</i> as its first parameter. This may be NULL if the application has a NULL <i>callback</i> or does not require the pointer to establish its context in the callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_post()</code> returns GLOBUS_SUCCESS, initiates the message exchange, registers the function pointed to by <i>callback</i> to be called when the exchange completes or fails, and modifies the <i>handle</i> parameter if it is non-NULL. If an error occurs, its error code will be returned, the <i>handle</i> parameter will be uninitialized and the function pointed to be <i>callback</i> will not be called.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> There is no way to time out or cancel a service request that is begun with <code>globus_gram_protocol_post()</code>.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_protocol_reply()</code></dl>
<h3>int globus_gram_protocol_post_delegation (const char *url, <code>globus_gram_protocol_handle_t</code> *handle, globus_io_attr_t *attr, globus_byte_t *message, globus_size_tmessage_size, gss_cred_id_tcred_handle, gss_OID_setrestriction_oids, gss_buffer_set_trestriction_buffers, OM_uint32req_flags, OM_uint32time_req, globus_gram_protocol_callback_tcallback, void *callback_arg)</h3>
<p> Post a GRAM protocol delegation request to a GRAM server. The <code>globus_gram_protocol_post_delegation()</code> function initiates a GRAM protocol delegation exchange with a GRAM protocol listener. The delegation protocol is a custom mix of HTTP and SSL records. </p>
<p> The <code>globus_gram_protocol_post_delegation()</code> function returns after framing the message and initiating the connection to be used for delegation. When the message exchange is complete, the function pointed to by <i>callback</i> is invoked either in another thread or when a non-threaded application calls the globus_poll() or globus_cond_wait() functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url</i> A pointer to a string containing the URL of the server to post the request to. This URL must be an HTTPS URL naming a GRAM service resource.<br />
 <i>handle</i> A pointer to a <i>globus_gram_protocol_handle_t</i> which will be initialized with a unique handle identifier. This identifier will be passed to the <i>callback</i> function to allow the caller to differentiate replies to multiple GRAM Protocol requests. This pointer may be NULL if the caller will not have multiple simultaneous requests.<br />
 <i>attr</i> A pointer to a Globus I/O attribute set, which will be used as parameters when connecting to the GRAM server. The value of <i>attr</i> may be NULL, in which case, the default GRAM Protocol attributes will be used (authentication to self, SSL-compatible transport, with message integrity).<br />
 <i>message</i> A pointer to a message string to be sent to the GRAM server. This is normally created by calling one of the GRAM Protocol <code>pack </code> functions. This message need not be NULL terminated as the length is passed in the <i>message_size</i> parameter.<br />
 <i>message_size</i> The length of the <i>message</i> string. Typically generated as one of the output parameters to one of the GRAM Protocol <code>pack </code> functions.<br />
 <i>cred_handle</i> Handle to an existing GSSAPI security credential. If this parameter is set to <i>GSS_C_NO_CREDENTIAL</i>, then the current account&#8217;s default credential will be used. A proxy credential sharing the identity of this credential will be delegated to the GRAM protocol server.<br />
 <i>restriction_oids</i> A set of OID values indicating the data in the <i>restriction_buffers</i> parameter. This parameter may have the value GSS_C_NO_OID_SET if there are no restriction buffers.<br />
 <i>restriction_buffers</i> A set of binary data buffers which will be included in the delegated credential. The type of data in these buffers is determined by the OID values in <i>restriction_oids</i>. This parameter may have the value GSS_C_EMPTY_BUFFER_SET if there are no extra restrictions to be added to the credential.<br />
 <i>req_flags</i> A bitwise-or of GSSAPI flag values to use when delegating the credential using gss_init_delegation().<br />
 <i>time_req</i> An integer value indicating the length of time (in seconds) that the delegated credential should be valid for. This is an advisory parameter: no error will be returned if a credential with the requested lifetime can not be created.<br />
 <i>callback</i> A pointer to a function to call when the response to this message is received or the message exchange fails. This may be NULL, in which case no callback will be received, and the caller will be unable to verify whether the message was successfully received.<br />
 <i>callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>callback</i> as its first parameter. This may be NULL if the application has a NULL <i>callback</i> or does not require the pointer to establish its context in the callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_post_delegation()</code> returns GLOBUS_SUCCESS, initiates the message exchange, registers the function pointed to by <i>callback</i> to be called when the exchange completes or fails, and modifies the <i>handle</i> parameter if it is non-NULL. If an error occurs, its error code will be returned, the <i>handle</i> parameter will be uninitialized and the function pointed to be <i>callback</i> will not be called. In the case of a protocol or delegation failure, the callback function will be called with the <i>errorcode</i> parameter set to the error.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> There is no way to time out or cancel a service request that is begun with <code>globus_gram_protocol_post_delegation()</code>.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_protocol_reply()</code></dl>
<h3>int globus_gram_protocol_reply (<code>globus_gram_protocol_handle_t</code>handle, intcode, globus_byte_t *message, globus_size_tmessage_size)</h3>
<p> Reply to a GRAM protocol message. The <i></i><code>globus_gram_protocol_reply()</code> function sends a response message to a client which initiated a GRAM message exchange. The <i></i><code>globus_gram_protocol_reply()</code> function composes the message with an HTTP message frame and then sends it to the client which initiated the exchange. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A GRAM protocol handle which is used by this function to determine the network connection to use for this reply. This must be the same value as was passed as a parameter to the callback function registered with the <i></i><code>globus_gram_protocol_allow_attach()</code> function.<br />
 <i>code</i> The HTTP response code. The code should be one from the set described in RFC 2616.<br />
 <i>message</i> A pointer to a message string to be sent to the GRAM client. This is normally created by calling one of the GRAM Protocol <code>pack </code> functions. This message need not be NULL terminated as the length is passed in the <i>message_size</i> parameter.<br />
 <i>message_size</i> The length of the <i>message</i> string. Typically generated as one of the output parameters to one of the GRAM Protocol <code>pack </code> functions.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <i></i><code>globus_gram_protocol_reply()</code> returns GLOBUS_SUCCESS, frames the <i>message</i> with an HTTP header and initiates sending the message to the client. The caller must not try to use the value of the <i>handle</i> parameter after this function returns. If an error occurs, its integer error code will be returned.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No Resources</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_protocol_allow_attach()</code></dl>
<h3>int globus_gram_protocol_setup_attr (globus_io_attr_t *attr)</h3>
<p> Create default I/O attribute for GRAM. The <code>globus_gram_protocol_setup_attr()</code> function creates a new globus_io attribute containing the default set of values needed for communication between a GRAM client and a job manager. These attributes include:</p>
<dl>
<dt>&bull;</p>
<dd> SO_KEEPALIVE</p>
<dt>&bull;</p>
<dd> GSSAPI Mutual Authentication</p>
<dt>&bull;</p>
<dd> GSSAPI Self Authorization</p>
<dt>&bull;</p>
<dd> SSL-compatible message wrapping</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> A pointer to a <i>globus_io_attr_t</i> structure which will be initialized by this function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_setup_attr()</code> modifies the <i>attr</i> parameter to point to a new attribute and returns the value <i>GLOBUS_SUCCESS</i>. When this occurs, the caller must destroy the attribute when no longer needed by calling globus_io_tcpattr_destroy(). If an error occurs, its value will be returned and the attribute pointed to by the <i>attr</i> parameter will be set to an uninitialized state.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_CONNECTION_FAILED</i> Error initializing attribute</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gram_protocol from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Function Documentation</a></p>
<dd>
<dt><a href="#lbAS">Author</a></p>
<dd></dl>
