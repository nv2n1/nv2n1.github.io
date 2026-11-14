---
title: "globus_gass_transfer_error_already_registered(3)"
name: "globus_gass_transfer_error_already_registered"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_error_already_registered/"
description: "globus_gass_transfer.h – GASS transfer."
---

<p>globus_gass_transfer.h &#8211; GASS transfer.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GASS_TRANSFER_MODULE</code> </p>
<p> #define <code>GLOBUS_GASS_TRANSFER_LENGTH_UNKNOWN</code> </p>
<p> #define <code>GLOBUS_GASS_TRANSFER_TIMESTAMP_UNKNOWN</code> </p>
<h3>Typedefs</h3>
<p>typedef void(* <code>globus_gass_transfer_close_callback_t</code> )(void *callback_arg, globus_gass_transfer_listener_t listener) </p>
<p> typedef void(* <code>globus_gass_transfer_listen_callback_t</code> )(void *callback_arg, globus_gass_transfer_listener_t listener) </p>
<p> typedef void(* <code>globus_gass_transfer_bytes_callback_t</code> )(void *arg, <code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t length, globus_bool_t last_data) </p>
<h3>Enumerations</h3>
<p>enum <code>globus_gass_transfer_request_type_t</code> { <code>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_INVALID</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_GET</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_PUT</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_APPEND</code> } </p>
<p> enum <code>globus_gass_transfer_request_status_t</code> { <code>GLOBUS_GASS_TRANSFER_REQUEST_INVALID</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_STARTING</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_PENDING</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_FAILED</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_REFERRED</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_DENIED</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_DONE</code> } </p>
<p> enum { <code>GLOBUS_GASS_TRANSFER_ERROR_BAD_PORT</code> = 2, <code>GLOBUS_GASS_TRANSFER_ERROR_INTERNAL_ERROR</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_BAD_URL</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_NOT_SUPPORTED</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_MALLOC_FAILED</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_NOT_INITIALIZED</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_NOT_REGISTERED</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_NOT_FOUND</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_TOO_LARGE</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_REQUEST_FAILED</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_DONE</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_ALREADY_REGISTERED</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_OPEN_FAILED</code>, <code>GLOBUS_GASS_TRANSFER_ERROR_TRANSFER_FAILED</code> } </p>
<p> enum </p>
<h3>Functions</h3>
<p>int <code>globus_gass_transfer_register_get</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_gass_transfer_callback_t callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_get</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url) </p>
<p> int <code>globus_gass_transfer_register_put</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_t length, globus_gass_transfer_callback_t callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_put</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_t length) </p>
<p> int <code>globus_gass_transfer_register_append</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_t length, globus_gass_transfer_callback_t callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_append</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_t length) </p>
<p> int <code>globus_gass_transfer_create_listener</code> (globus_gass_transfer_listener_t *listener, globus_gass_transfer_listenerattr_t *attr, char *scheme) </p>
<p> int <code>globus_gass_transfer_close_listener</code> (globus_gass_transfer_listener_t listener, <code>globus_gass_transfer_close_callback_t</code> callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_register_listen</code> (globus_gass_transfer_listener_t listener, <code>globus_gass_transfer_listen_callback_t</code> callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_register_accept</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, globus_gass_transfer_listener_t listener, globus_gass_transfer_callback_t callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_refer</code> (<code>globus_gass_transfer_request_t</code> request, char **urls, globus_size_t num_urls) </p>
<p> int <code>globus_gass_transfer_authorize</code> (<code>globus_gass_transfer_request_t</code> request, globus_size_t total_length) </p>
<p> int <code>globus_gass_transfer_deny</code> (<code>globus_gass_transfer_request_t</code> request, int reason, char *message) </p>
<p> char * <code>globus_gass_transfer_listener_get_base_url</code> (globus_gass_transfer_listener_t listener) </p>
<p> void * <code>globus_gass_transfer_listener_get_user_pointer</code> (globus_gass_transfer_listener_t listener) </p>
<p> int <code>globus_gass_transfer_listener_set_user_pointer</code> (globus_gass_transfer_listener_t listener, void *user_pointer) </p>
<p> int <code>globus_gass_transfer_send_bytes</code> (<code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t send_length, globus_bool_t last_data, <code>globus_gass_transfer_bytes_callback_t</code> callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_receive_bytes</code> (<code>globus_gass_transfer_request_t</code> request, globus_byte_t *bytes, globus_size_t max_length, globus_size_t wait_for_length, <code>globus_gass_transfer_bytes_callback_t</code> callback, void *user_arg) </p>
<p> globus_object_t * <code>globus_gass_transfer_requestattr_initialize</code> (globus_object_t *obj, char *proxy_url, globus_size_t block_size, globus_gass_transfer_file_mode_t file_mode, globus_bool_t connection_reuse) </p>
<p> globus_object_t * <code>globus_gass_transfer_socket_requestattr_initialize</code> (globus_object_t *obj, char *proxy_url, globus_size_t block_size, globus_gass_transfer_file_mode_t file_mode, globus_bool_t connection_reuse, int sndbuf, int rcvbuf, globus_bool_t nodelay) </p>
<p> globus_object_t * <code>globus_gass_transfer_secure_requestattr_initialize</code> (globus_object_t *obj, char *proxy_url, globus_size_t block_size, globus_gass_transfer_file_mode_t file_mode, globus_bool_t connection_reuse, int sndbuf, int rcvbuf, globus_bool_t nodelay, globus_gass_transfer_authorization_t authorization, char *subject) </p>
<p> globus_object_t * <code>globus_gass_transfer_listenerattr_initialize</code> (globus_object_t *obj, int backlog, unsigned short port) </p>
<h2>Detailed Description</h2>
<p>GASS transfer. </p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_GASS_TRANSFER_LENGTH_UNKNOWN</h3>
<p>Value for files we don&#8217;t know the length of.</p>
<h3>#define GLOBUS_GASS_TRANSFER_TIMESTAMP_UNKNOWN</h3>
<p>Value for timestamps we don&#8217;t know the value of.</p>
<h2>Enumeration Type Documentation</h2>
<h3>anonymous enum</h3>
<p>GASS error codes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_BAD_PORT </i></p>
<dd>Invalid port in URL</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_INTERNAL_ERROR </i></p>
<dd>Something bad occurred while processing the request</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_BAD_URL </i></p>
<dd>Unparsable URL</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_NOT_SUPPORTED </i></p>
<dd>Invalid file open mode in the GASS File library</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED </i></p>
<dd>Operation not supported by GASS for this type of URL</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_MALLOC_FAILED </i></p>
<dd>Out of memory</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_NOT_INITIALIZED </i></p>
<dd>Uninitialized or invalid handle</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER </i></p>
<dd>NULL pointer passed as parameter</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_NOT_REGISTERED </i></p>
<dd>GASS Server not yet registered</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_NOT_FOUND </i></p>
<dd>URL not in cache</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE </i></p>
<dd>Invalid use of a GASS handle</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_TOO_LARGE </i></p>
<dd>Bytes array exceeds GASS request size</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_REQUEST_FAILED </i></p>
<dd>GASS Transfer request did not complete successfully</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_DONE </i></p>
<dd>GASS handle already closed before this operation began</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_ALREADY_REGISTERED </i></p>
<dd>GASS handle already registered for processing</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_OPEN_FAILED </i></p>
<dd>Could not open local file</p>
<dt><i>GLOBUS_GASS_TRANSFER_ERROR_TRANSFER_FAILED </i></p>
<dd>A protocol error or client-initiated failure has occurred</dl>
<h3>anonymous enum</h3>
<p>Default buffer length for the globus_gass_transfer_assist library.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gass_transfer from the source code.</p>
