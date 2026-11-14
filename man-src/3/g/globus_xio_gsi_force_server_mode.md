---
title: "globus_xio_gsi_force_server_mode(3)"
name: "globus_xio_gsi_force_server_mode"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_gsi_force_server_mode/"
description: "Globus XIO GSI Driver –"
---

<p>Globus XIO GSI Driver &#8211; </p>
<h3>Typedefs</h3>
<p>typedef void(* <code>globus_xio_gsi_delegation_init_callback_t</code> )(globus_result_t result, void *user_arg) </p>
<p> typedef void(* <code>globus_xio_gsi_delegation_accept_callback_t</code> )(globus_result_t result, gss_cred_id_t delegated_cred, OM_uint32 time_rec, void *user_arg) </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_gsi_error_t</code> { <code>GLOBUS_XIO_GSI_ERROR_INVALID_PROTECTION_LEVEL</code>, <code>GLOBUS_XIO_GSI_ERROR_WRAP_GSSAPI</code>, <code>GLOBUS_XIO_GSI_ERROR_EMPTY_TARGET_NAME</code>, <code>GLOBUS_XIO_GSI_ERROR_EMPTY_HOST_NAME</code>, <code>GLOBUS_XIO_GSI_AUTHORIZATION_FAILED</code>, <code>GLOBUS_XIO_GSI_ERROR_TOKEN_TOO_BIG</code> } </p>
<p> enum <code>globus_xio_gsi_cmd_t</code> { <code>GLOBUS_XIO_GSI_SET_CREDENTIAL</code>, <code>GLOBUS_XIO_GSI_GET_CREDENTIAL</code>, <code>GLOBUS_XIO_GSI_SET_GSSAPI_REQ_FLAGS</code>, <code>GLOBUS_XIO_GSI_GET_GSSAPI_REQ_FLAGS</code>, <code>GLOBUS_XIO_GSI_SET_PROXY_MODE</code>, <code>GLOBUS_XIO_GSI_GET_PROXY_MODE</code>, <code>GLOBUS_XIO_GSI_SET_AUTHORIZATION_MODE</code>, <code>GLOBUS_XIO_GSI_GET_AUTHORIZATION_MODE</code>, <code>GLOBUS_XIO_GSI_SET_DELEGATION_MODE</code>, <code>GLOBUS_XIO_GSI_GET_DELEGATION_MODE</code>, <code>GLOBUS_XIO_GSI_SET_SSL_COMPATIBLE</code>, <code>GLOBUS_XIO_GSI_SET_ANON</code>, <code>GLOBUS_XIO_GSI_SET_WRAP_MODE</code>, <code>GLOBUS_XIO_GSI_GET_WRAP_MODE</code>, <code>GLOBUS_XIO_GSI_SET_BUFFER_SIZE</code>, <code>GLOBUS_XIO_GSI_GET_BUFFER_SIZE</code>, <code>GLOBUS_XIO_GSI_SET_PROTECTION_LEVEL</code>, <code>GLOBUS_XIO_GSI_GET_PROTECTION_LEVEL</code>, <code>GLOBUS_XIO_GSI_GET_TARGET_NAME</code>, <code>GLOBUS_XIO_GSI_SET_TARGET_NAME</code>, <code>GLOBUS_XIO_GSI_GET_CONTEXT</code>, <code>GLOBUS_XIO_GSI_GET_DELEGATED_CRED</code>, <code>GLOBUS_XIO_GSI_GET_PEER_NAME</code>, <code>GLOBUS_XIO_GSI_GET_LOCAL_NAME</code>, <code>GLOBUS_XIO_GSI_INIT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_REGISTER_INIT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_ACCEPT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_REGISTER_ACCEPT_DELEGATION</code>, <code>GLOBUS_XIO_GSI_FORCE_SERVER_MODE</code>, <code>GLOBUS_XIO_GSI_SET_ALLOW_MISSING_SIGNING_POLICY</code>, <code>GLOBUS_XIO_GSI_GET_ALLOW_MISSING_SIGNING_POLICY</code> } </p>
<p> enum <code>globus_xio_gsi_protection_level_t</code> { <code>GLOBUS_XIO_GSI_PROTECTION_LEVEL_NONE</code>, <code>GLOBUS_XIO_GSI_PROTECTION_LEVEL_INTEGRITY</code>, <code>GLOBUS_XIO_GSI_PROTECTION_LEVEL_PRIVACY</code> } </p>
<p> enum <code>globus_xio_gsi_delegation_mode_t</code> { <code>GLOBUS_XIO_GSI_DELEGATION_MODE_NONE</code>, <code>GLOBUS_XIO_GSI_DELEGATION_MODE_LIMITED</code>, <code>GLOBUS_XIO_GSI_DELEGATION_MODE_FULL</code> } </p>
<p> enum <code>globus_xio_gsi_proxy_mode_t</code> { <code>GLOBUS_XIO_GSI_PROXY_MODE_FULL</code>, <code>GLOBUS_XIO_GSI_PROXY_MODE_LIMITED</code>, <code>GLOBUS_XIO_GSI_PROXY_MODE_MANY</code> } </p>
<p> enum <code>globus_xio_gsi_authorization_mode_t</code> { <code>GLOBUS_XIO_GSI_NO_AUTHORIZATION</code>, <code>GLOBUS_XIO_GSI_SELF_AUTHORIZATION</code>, <code>GLOBUS_XIO_GSI_IDENTITY_AUTHORIZATION</code>, <code>GLOBUS_XIO_GSI_HOST_AUTHORIZATION</code> } </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_CREDENTIAL</code>, gss_cred_id_t credential) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_SET_CREDENTIAL</code>, gss_cred_id_t credential) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_CREDENTIAL</code>, gss_cred_id_t *credential) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_GET_CREDENTIAL</code>, gss_cred_id_t *credential) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_GSSAPI_REQ_FLAGS</code>, OM_uint32 req_flags) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_GSSAPI_REQ_FLAGS</code>, OM_uint32 *req_flags) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_PROXY_MODE</code>, <code>globus_xio_gsi_proxy_mode_t</code> proxy_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_PROXY_MODE</code>, <code>globus_xio_gsi_proxy_mode_t</code> *proxy_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_AUTHORIZATION_MODE</code>, <code>globus_xio_gsi_authorization_mode_t</code> authz_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_AUTHORIZATION_MODE</code>, <code>globus_xio_gsi_authorization_mode_t</code> *authz_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_DELEGATION_MODE</code>, <code>globus_xio_gsi_delegation_mode_t</code> delegation_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_DELEGATION_MODE</code>, <code>globus_xio_gsi_delegation_mode_t</code> *delegation_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_SSL_COMPATIBLE</code>, globus_bool_t ssl_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_ANON</code>, globus_bool_t anon_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_WRAP_MODE</code>, globus_bool_t wrap_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_WRAP_MODE</code>, globus_bool_t *wrap_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_BUFFER_SIZE</code>, globus_size_t buffer_size) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_BUFFER_SIZE</code>, globus_size_t *buffer_size) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_PROTECTION_LEVEL</code>, <code>globus_xio_gsi_protection_level_t</code> protection_level) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_PROTECTION_LEVEL</code>, <code>globus_xio_gsi_protection_level_t</code> *protection_level) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_TARGET_NAME</code>, gss_name_t *target_name) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_TARGET_NAME</code>, gss_name_t target_name) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_GET_CONTEXT</code>, gss_ctx_id_t *context) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_GET_DELEGATED_CRED</code>, gss_cred_id_t *credential) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_GET_PEER_NAME</code>, gss_name_t *peer_name) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_GET_LOCAL_NAME</code>, gss_name_t *local_name) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_INIT_DELEGATION</code>, gss_cred_id_t credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_REGISTER_INIT_DELEGATION</code>, gss_cred_id_t credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req, <code>globus_xio_gsi_delegation_init_callback_t</code> callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_ACCEPT_DELEGATION</code>, gss_cred_id_t *credential, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req) </p>
<p> globus_result_t <code>globus_xio_gsi_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GSI_REGISTER_ACCEPT_DELEGATION</code>, gss_OID_set restriction_oids, gss_buffer_set_t restriction_buffers, OM_uint32 time_req, <code>globus_xio_gsi_delegation_accept_callback_t</code> callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_FORCE_SERVER_MODE</code>, globus_bool_t server_mode) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_SET_ALLOW_MISSING_SIGNING_POLICY</code>, globus_bool_t allow) </p>
<p> globus_result_t <code>globus_xio_gsi_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GSI_GET_ALLOW_MISSING_SIGNING_POLICY</code>, globus_bool_t *allow) </p>
<h2>Detailed Description</h2>
<h2>Opening/Closing</h2>
<p>An XIO handle with the gsi driver can be created with either globus_xio_handle_create () or globus_xio_server_register_accept (). </p>
<p> If the handle is created with globus_xio_server_register_accept (), the globus_xio_register_open () call will proceed to accept a GSSAPI security context. Upon successful completion of the open (after the open callback has been called) the application may proceed to read or write data associated with the GSI session. </p>
<p> If the handle is created with globus_xio_handle_create (), then the XIO handle will implement the client-side (init) of the GSSAPI call sequence and establish a security context with the accepting side indicated by the contact_string passed to globus_xio_register_open ().</p>
<h2>Reading/Writing</h2>
<p>The GSI driver behaves similar to the underlying transport driver with respect to reads and writes, except for the try-read and try-write operations (ie. waitforbytes ==0) which always return immediately. This is due to the fact that the security layer needs to read and write tokens of a certain minimal size and thus needs to rely on the underlying transport to handle greater than 0 reads/write which is not possible in &#8216;try&#8217; mode.</p>
<h2>Server</h2>
<p>globus_xio_server_create() causes a new transport-specific listener socket to be created to handle new GSI connections. globus_xio_server_register_accept() will accept a new connection for processing. globus_xio_server_register_close() cleans up the internal resources associated with the http server and calls close on the listener. </p>
<p> All accepted handles inherit all GSI-specific attributes set in the attr to globus_xio_server_create(), but can be overridden with the attr to globus_xio_register_open(). Furthermore, accepted handles will use the GSSAPI accept security context call unless explicitly overridden during the globus_xio_register_open() call ( GLOBUS_XIO_GSI_FORCE_SERVER_MODE).</p>
<h2>Environment Variables</h2>
<p>The gsi driver uses the following environment variables</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>X509_USER_PROXY</p>
<dt>&bull;</p>
<dd>X509_USER_CERT</p>
<dt>&bull;</p>
<dd>X509_USER_KEY</p>
<dt>&bull;</p>
<dd>X509_CERT_DIR</dl>
<p> For details see Globus: GSI Environment Variables</p>
<h2>Attributes and Cntls</h2>
<p>GSI driver specific attrs and cntls </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>globus_xio_attr_cntl () </p>
<p> globus_xio_handle_cntl ()</dl>
<h2>Error Types</h2>
<p>The GSI driver uses mostly GSSAPI calls, so it generally just wraps the underlying GSSAPI errors or uses generic XIO errors. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>globus_xio_driver_error_match () </p>
<p> globus_error_gssapi_match () </p>
<p> globus_error_match_openssl_error ()</dl>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_xio_gsi_delegation_accept_callback_t)(globus_result_t result, gss_cred_id_t delegated_cred, OM_uint32 time_rec, void *user_arg)</h3>
<p>Globus XIO GSI init delegation callback</p>
<h3>typedef void(* globus_xio_gsi_delegation_init_callback_t)(globus_result_t result, void *user_arg)</h3>
<p>Globus XIO GSI init delegation callback</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_gsi_authorization_mode_t</code></h3>
<p>Globus XIO GSI authorization modes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_GSI_NO_AUTHORIZATION </i></p>
<dd>Do not perform any authorization. This will cause a error when used in conjunction with delegation on the init/client side.</p>
<dt><i>GLOBUS_XIO_GSI_SELF_AUTHORIZATION </i></p>
<dd>Authorize the peer if the peer has the same identity as ourselves</p>
<dt><i>GLOBUS_XIO_GSI_IDENTITY_AUTHORIZATION </i></p>
<dd>Authorize the peer if the peer identity matches the identity set in the target name.</p>
<dt><i>GLOBUS_XIO_GSI_HOST_AUTHORIZATION </i></p>
<dd>Authorize the peer if the identity of the peer matches the identity of the peer hostname.</dl>
<h3>enum <code>globus_xio_gsi_cmd_t</code></h3>
<p>GSI driver specific cntls </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_GSI_SET_CREDENTIAL </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code>, <code>globus_xio_gsi_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_CREDENTIAL </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code>, <code>globus_xio_gsi_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_GSSAPI_REQ_FLAGS </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_GSSAPI_REQ_FLAGS </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_PROXY_MODE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_PROXY_MODE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_AUTHORIZATION_MODE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_AUTHORIZATION_MODE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_DELEGATION_MODE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_DELEGATION_MODE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_SSL_COMPATIBLE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_ANON </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_WRAP_MODE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_WRAP_MODE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_BUFFER_SIZE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_BUFFER_SIZE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_PROTECTION_LEVEL </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_PROTECTION_LEVEL </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_TARGET_NAME </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_TARGET_NAME </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_CONTEXT </i></p>
<dd>See usage for: <code>globus_xio_gsi_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_DELEGATED_CRED </i></p>
<dd>See usage for: <code>globus_xio_gsi_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_PEER_NAME </i></p>
<dd>See usage for: <code>globus_xio_gsi_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_LOCAL_NAME </i></p>
<dd>See usage for: <code>globus_xio_gsi_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_INIT_DELEGATION </i></p>
<dd>See usage for: <code>globus_xio_gsi_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_REGISTER_INIT_DELEGATION </i></p>
<dd>See usage for: <code>globus_xio_gsi_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_ACCEPT_DELEGATION </i></p>
<dd>See usage for: <code>globus_xio_gsi_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_REGISTER_ACCEPT_DELEGATION </i></p>
<dd>See usage for: <code>globus_xio_gsi_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_FORCE_SERVER_MODE </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_SET_ALLOW_MISSING_SIGNING_POLICY </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GSI_GET_ALLOW_MISSING_SIGNING_POLICY </i></p>
<dd>See usage for: <code>globus_xio_gsi_attr_cntl </code></dl>
<h3>enum <code>globus_xio_gsi_delegation_mode_t</code></h3>
<p>Globus XIO GSI delegation modes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_GSI_DELEGATION_MODE_NONE </i></p>
<dd>No delegation</p>
<dt><i>GLOBUS_XIO_GSI_DELEGATION_MODE_LIMITED </i></p>
<dd>Delegate a limited proxy</p>
<dt><i>GLOBUS_XIO_GSI_DELEGATION_MODE_FULL </i></p>
<dd>Delegate a full proxy</dl>
<h3>enum <code>globus_xio_gsi_error_t</code></h3>
<p>GSI driver specific error types </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_GSI_ERROR_INVALID_PROTECTION_LEVEL </i></p>
<dd>Indicates that the established context does not meet the required protection level</p>
<dt><i>GLOBUS_XIO_GSI_ERROR_WRAP_GSSAPI </i></p>
<dd>Wraps a GSSAPI error</p>
<dt><i>GLOBUS_XIO_GSI_ERROR_EMPTY_TARGET_NAME </i></p>
<dd>Indicates that GLOBUS_XIO_GSI_IDENTITY_AUTHORIZATION is set but that the target name is empty</p>
<dt><i>GLOBUS_XIO_GSI_ERROR_EMPTY_HOST_NAME </i></p>
<dd>Indicates that GLOBUS_XIO_GSI_HOST_AUTHORIZATION is set but that no host name is available</p>
<dt><i>GLOBUS_XIO_GSI_AUTHORIZATION_FAILED </i></p>
<dd>Indicates that the peer is not authorized</p>
<dt><i>GLOBUS_XIO_GSI_ERROR_TOKEN_TOO_BIG </i></p>
<dd>Indicates the token being read is too big. Usually happens when someone tries to establish a non secure session with a endpoint that expects security</dl>
<h3>enum <code>globus_xio_gsi_protection_level_t</code></h3>
<p>Globus XIO GSI protection levels </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_GSI_PROTECTION_LEVEL_NONE </i></p>
<dd>No security</p>
<dt><i>GLOBUS_XIO_GSI_PROTECTION_LEVEL_INTEGRITY </i></p>
<dd>Messages are signed</p>
<dt><i>GLOBUS_XIO_GSI_PROTECTION_LEVEL_PRIVACY </i></p>
<dd>Messages are signed and encrypted</dl>
<h3>enum <code>globus_xio_gsi_proxy_mode_t</code></h3>
<p>Globus XIO GSI proxy modes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_GSI_PROXY_MODE_FULL </i></p>
<dd>Accept only full proxies</p>
<dt><i>GLOBUS_XIO_GSI_PROXY_MODE_LIMITED </i></p>
<dd>Accept full proxies and limited proxies if they are the only limited proxy in the cert chain.</p>
<dt><i>GLOBUS_XIO_GSI_PROXY_MODE_MANY </i></p>
<dd>Accept both full and limited proxies unconditionally</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_CREDENTIAL</code>, gss_cred_id_tcredential)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the credential to be used </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>credential</i> The credential to set. The credential structure needs to remain valid for the lifetime of any XIO data structure it is used by.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>If this is called with the handle_cntl, there must be no outstanding operations on the handle.</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_GET_CREDENTIAL</code>, gss_cred_id_t *credential)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the credential to be used </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>credential</i> The credential that is currently set. This will only return a credential if a credential was explicitly set prior to this call. It will not return any credential automatically acquired during context initialization.</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_GSSAPI_REQ_FLAGS</code>, OM_uint32req_flags)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the GSSAPI req_flags to be used </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>req_flags</i> The req_flags to set</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_GET_GSSAPI_REQ_FLAGS</code>, OM_uint32 *req_flags)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the GSSAPI req_flags to be used </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>req_flags</i> The req flags currently in effect</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_PROXY_MODE</code>, <code>globus_xio_gsi_proxy_mode_t</code>proxy_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the proxy mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>proxy_mode</i> The proxy mode to set</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Changing the proxy mode changes the req_flags</dl>
<p> string opt: proxy=&#8217;many&#8217;|&#8217;full&#8217;|&#8217;limited&#8217;</p>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_GET_PROXY_MODE</code>, <code>globus_xio_gsi_proxy_mode_t</code> *proxy_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the proxy mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>proxy_mode</i> The proxy mode that is currently in effect</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Changing the proxy mode changes the req_flags</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_AUTHORIZATION_MODE</code>, <code>globus_xio_gsi_authorization_mode_t</code>authz_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the authorization mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>authz_mode</i> The authorization mode to set</dl>
<p> string opt: auth=&#8217;none&#8217;|&#8217;self&#8217;|&#8217;host&#8217;|&#8217;id&#8217;</p>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_GET_AUTHORIZATION_MODE</code>, <code>globus_xio_gsi_authorization_mode_t</code> *authz_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the authorization mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>authz_mode</i> The authorization mode that is currently in effect</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_DELEGATION_MODE</code>, <code>globus_xio_gsi_delegation_mode_t</code>delegation_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the delegation mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>delegation_mode</i> The delegation mode to use</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Changing the delegation mode changes the req_flags</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_GET_DELEGATION_MODE</code>, <code>globus_xio_gsi_delegation_mode_t</code> *delegation_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the delegation mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>delegation_mode</i> The delegation mode currently in effect</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_SSL_COMPATIBLE</code>, globus_bool_tssl_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Make the on the wire protocol SSL compatible. </p>
<p> This implies no wrapping of security tokens and no delegation </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ssl_mode</i> The ssl compatibility mode to use</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Changing the ssl compatibility mode changes the req_flags</dl>
<p> string opt: ssl_compatible=&#8217;true&#8217;|&#8217;false&#8217;</p>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_ANON</code>, globus_bool_tanon_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Do anonymous authentication </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>anon_mode</i> The ssl compatibility mode to use</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Changing the ssl compatibility mode changes the req_flags and the wrapping mode</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_WRAP_MODE</code>, globus_bool_twrap_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the wrapping mode </p>
<p> This mode determines whether tokens will be wrapped with a Globus IO style header or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>wrap_mode</i> The wrapping mode to use</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_GET_WRAP_MODE</code>, globus_bool_t *wrap_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the wrapping mode </p>
<p> This mode determines whether tokens will be wrapped with a Globus IO style header or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>wrap_mode</i> The wrapping mode currently in use.</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_BUFFER_SIZE</code>, globus_size_tbuffer_size)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the read buffer size </p>
<p> The read buffer is used for buffering wrapped data, is initialized with a default size of 128K and scaled dynamically to always be able to fit whole tokens. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buffer_size</i> The size of the read buffer</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_GET_BUFFER_SIZE</code>, globus_size_t *buffer_size)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the read buffer size </p>
<p> The read buffer is used for buffering wrapped data, is initialized with a default size of 128K and scaled dynamically to always be able to fit whole tokens. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buffer_size</i> The size of the read buffer</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_PROTECTION_LEVEL</code>, <code>globus_xio_gsi_protection_level_t</code>protection_level)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the protection level </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>protection_level</i> The protection level to set</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Changing the proxy mode changes the req_flags</dl>
<p> string opt: protection=&#8217;none&#8217;|&#8217;private&#8217;|&#8217;integrity&#8217;</p>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_GET_PROTECTION_LEVEL</code>, <code>globus_xio_gsi_protection_level_t</code> *protection_level)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the protection level </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>protection_level</i> The current protection level</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_GET_TARGET_NAME</code>, gss_name_t *target_name)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the expected peer name </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>target_name</i> The expected peer name</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_TARGET_NAME</code>, gss_name_ttarget_name)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the expected peer name </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>target_name</i> The expected peer name</dl>
<p> string opt: subject=<i>string</i></p>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_FORCE_SERVER_MODE</code>, globus_bool_tserver_mode)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Force the server mode setting. </p>
<p> This explicitly sets the directionality of context establishment and delegation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>server_mode</i> The server mode.</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_SET_ALLOW_MISSING_SIGNING_POLICY</code>, globus_bool_tallow)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the allow missing signing policy flag </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>allow</i> The flag setting to use</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Changing this flag changes the req_flags</dl>
<h3>globus_result_t globus_xio_gsi_attr_cntl (attr, driver, <code>GLOBUS_XIO_GSI_GET_ALLOW_MISSING_SIGNING_POLICY</code>, globus_bool_t *allow)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the allow missing signing policy flag </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>allow</i> The flag currently set</dl>
<h3>globus_result_t globus_xio_gsi_handle_cntl (handle, driver, <code>GLOBUS_XIO_GSI_SET_CREDENTIAL</code>, gss_cred_id_tcredential)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the credential to be used </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>credential</i> The credential to set. The credential structure needs to remain valid for the lifetime of any XIO data structure it is used by.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>If this is called with the handle_cntl, there must be no outstanding operations on the handle.</dl>
<h3>globus_result_t globus_xio_gsi_handle_cntl (handle, driver, <code>GLOBUS_XIO_GSI_GET_CREDENTIAL</code>, gss_cred_id_t *credential)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the credential to be used </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>credential</i> The credential that is currently set. This will only return a credential if a credential was explicitly set prior to this call. It will not return any credential automatically acquired during context initialization.</dl>
<h3>globus_result_t globus_xio_gsi_handle_cntl (handle, driver, <code>GLOBUS_XIO_GSI_GET_CONTEXT</code>, gss_ctx_id_t *context)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the GSS context </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The GSS context</dl>
<h3>globus_result_t globus_xio_gsi_handle_cntl (handle, driver, <code>GLOBUS_XIO_GSI_GET_DELEGATED_CRED</code>, gss_cred_id_t *credential)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the delegated credential </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>credential</i> The delegated credential</dl>
<h3>globus_result_t globus_xio_gsi_handle_cntl (handle, driver, <code>GLOBUS_XIO_GSI_GET_PEER_NAME</code>, gss_name_t *peer_name)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the name of the peer </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>peer_name</i> The GSS name of the peer.</dl>
<h3>globus_result_t globus_xio_gsi_handle_cntl (handle, driver, <code>GLOBUS_XIO_GSI_GET_LOCAL_NAME</code>, gss_name_t *local_name)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the GSS name associated with the local credentials </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>local_name</i> The GSS name of the local credentials</dl>
<h3>globus_result_t globus_xio_gsi_handle_cntl (handle, driver, <code>GLOBUS_XIO_GSI_INIT_DELEGATION</code>, gss_cred_id_tcredential, gss_OID_setrestriction_oids, gss_buffer_set_trestriction_buffers, OM_uint32time_req)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Initialize delegation-at-any-time process </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>credential</i> The GSS credential to delegate<br />
 <i>restriction_oids</i> The OIDs for X.509 extensions to embed in the delegated credential<br />
 <i>restriction_buffers</i> The corresponding bodies for the X.509 extensions<br />
 <i>time_req</i> The lifetime of the delegated credential</dl>
<h3>globus_result_t globus_xio_gsi_handle_cntl (handle, driver, <code>GLOBUS_XIO_GSI_REGISTER_INIT_DELEGATION</code>, gss_cred_id_tcredential, gss_OID_setrestriction_oids, gss_buffer_set_trestriction_buffers, OM_uint32time_req, <code>globus_xio_gsi_delegation_init_callback_t</code>callback, void *callback_arg)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Initialize non-blocking delegation-at-any-time process </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>credential</i> The GSS credential to delegate<br />
 <i>restriction_oids</i> The OIDS for X.509 extensions to embed in the delegated credential<br />
 <i>restriction_buffers</i> The corresponding bodies for the X.509 extensions<br />
 <i>time_req</i> The lifetime of the delegated credential<br />
 <i>callback</i> The callback to call when the operation completes<br />
 <i>callback_arg</i> The arguments to pass to the callback</dl>
<h3>globus_result_t globus_xio_gsi_handle_cntl (handle, driver, <code>GLOBUS_XIO_GSI_ACCEPT_DELEGATION</code>, gss_cred_id_t *credential, gss_OID_setrestriction_oids, gss_buffer_set_trestriction_buffers, OM_uint32time_req)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Accept delegation-at-any-time process </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>credential</i> The delegated GSS credential<br />
 <i>restriction_oids</i> The OIDS for X.509 extensions to embed in the delegated credential<br />
 <i>restriction_buffers</i> The corresponding bodies for the X.509 extensions<br />
 <i>time_req</i> The requested lifetime of the delegated credential</dl>
<h3>globus_result_t globus_xio_gsi_handle_cntl (handle, driver, <code>GLOBUS_XIO_GSI_REGISTER_ACCEPT_DELEGATION</code>, gss_OID_setrestriction_oids, gss_buffer_set_trestriction_buffers, OM_uint32time_req, <code>globus_xio_gsi_delegation_accept_callback_t</code>callback, void *callback_arg)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Accept non-blocking delegation-at-any-time process </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>restriction_oids</i> The OIDS for X.509 extensions to embed in the delegated credential<br />
 <i>restriction_buffers</i> The corresponding bodies for the X.509 extensions<br />
 <i>time_req</i> The lifetime of the delegated credential<br />
 <i>callback</i> The callback to call when the operation completes<br />
 <i>callback_arg</i> The arguments to pass to the callback</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio_gsi_driver from the source code.</p>
