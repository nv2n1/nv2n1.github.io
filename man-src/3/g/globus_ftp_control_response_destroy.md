---
title: "globus_ftp_control_response_destroy(3)"
name: "globus_ftp_control_response_destroy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_control_response_destroy/"
description: "GridFTP Control Client –"
---

<h2 class="name">NAME</h2>
<p> GridFTP Control Client &#8211; </p>
<p> Control Client.</p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_control_handle_init</code> (globus_ftp_control_handle_t *handle)<br />
 <i>Initialize a globus ftp handle. </i><br />
 globus_result_t <code>globus_ftp_control_handle_destroy</code> (globus_ftp_control_handle_t *handle)<br />
 <i>Destroy a globus ftp handle. </i><br />
 globus_result_t <code>globus_ftp_control_connect</code> (globus_ftp_control_handle_t *handle, char *host, unsigned short port, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Create a new control connection to an FTP server. </i><br />
 globus_result_t <code>globus_ftp_control_response_destroy</code> (globus_ftp_control_response_t *response)<br />
 <i>Free the memory associated with a response. </i><br />
 globus_result_t <code>globus_ftp_control_response_copy</code> (globus_ftp_control_response_t *src, globus_ftp_control_response_t *dest)<br />
 <i>Copy a response structure. </i><br />
 globus_result_t <code>globus_ftp_control_authenticate</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_auth_info_t</code> *auth_info, globus_bool_t use_auth, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Authenticate the user to the FTP server. </i><br />
 globus_result_t <code>globus_ftp_control_authenticate_ex</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_auth_info_t</code> *auth_info, globus_bool_t use_auth, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Authenticate the user to the FTP server. </i><br />
 globus_result_t <code>globus_ftp_control_send_command</code> (globus_ftp_control_handle_t *handle, const char *cmdspec, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg,&#8230;)<br />
 <i>Send an FTP protocol command. </i><br />
 globus_result_t <code>globus_ftp_control_abort</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Send a GridFTP ABORT. </i><br />
 globus_result_t <code>globus_ftp_control_quit</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Send a GridFTP QUIT. </i><br />
 globus_result_t <code>globus_ftp_control_force_close</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Force a control connection to close. </i><br />
 globus_result_t <code>globus_ftp_control_auth_info_init</code> (<code>globus_ftp_control_auth_info_t</code> *auth_info, gss_cred_id_t credential_handle, globus_bool_t encrypt, char *user, char *password, char *account, char *subject)<br />
 <i>Initialize authentication information. </i><br />
 int <code>globus_ftp_control_auth_info_compare</code> (<code>globus_ftp_control_auth_info_t</code> *auth_info_1, <code>globus_ftp_control_auth_info_t</code> *auth_info_2)<br />
 <i>Compare authentication information. </i><br />
 globus_result_t <code>globus_ftp_control_client_get_connection_info_ex</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t *local_info, globus_ftp_control_host_port_t *remote_info)<br />
 <i>Not documented yet. </i><br />
 globus_result_t <code>globus_ftp_control_ipv6_allow</code> (globus_ftp_control_handle_t *handle, globus_bool_t allow)<br />
 <i>Not documented yet. </i></p>
<h2>Detailed Description</h2>
<p> Control Client. </p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_control_abort (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_response_callback_t</code>callback, void *callback_arg)</h3>
<p> Send a GridFTP ABORT. This function is used to send the ABORT message to the FTP server. The ABORT message is sent out-of-band, and terminates any current data transfer in progress. </p>
<p> As a result of the ABORT, the data channels used by this control channel will be closed. The data command callback will be issued with either a completion reply, or a transfer aborted reply. The ABORT callback will also be invoked, with the server&#8217;s response to the abort command. </p>
<p> Any attempts to register buffers for read or write after an ABORT has been sent will fail with a &#8216;no transfer in progress&#8217; error. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a GridFTP control handle. The ABORT command is issued to the server over the control channel associated with this handle.<br />
 <i>callback</i> The function to be called once the authentication process is complete or when an error occurs.<br />
 <i>callback_arg</i> User supplied argument to the callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Success</p>
<dt>&bull;</p>
<dd> Null handle</p>
<dt>&bull;</p>
<dd> No transfer in progress</dl>
</dl>
<p> <code>Callback errors:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> protocol error</p>
<dt>&bull;</p>
<dd> eof</dl>
</dl>
<p> <code>Expected callback response values:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 226 Abort successful.</p>
<dt>&bull;</p>
<dd> 500 Syntax error, command unrecognized.</dl>
</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The server may send other responses.</dl>
<h3>int globus_ftp_control_auth_info_compare (<code>globus_ftp_control_auth_info_t</code> *auth_info_1, <code>globus_ftp_control_auth_info_t</code> *auth_info_2)</h3>
<p> Compare authentication information. This is helper function compares two authentication information structures and return zero if the two structures are deemed equal and a non-zero value otherwise. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>auth_info_1</i> The first authentication structure<br />
 <i>auth_info_2</i> The second authentication structure</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 0 if the structures are equal</p>
<dt>&bull;</p>
<dd> !0 if the structures differ or an error occurred</dl>
</dl>
<h3>globus_result_t globus_ftp_control_auth_info_init (<code>globus_ftp_control_auth_info_t</code> *auth_info, gss_cred_id_tcredential_handle, globus_bool_tencrypt, char *user, char *password, char *account, char *subject)</h3>
<p> Initialize authentication information. This is helper function initializes a authentication information structure with the values contained in the second to fifth arguments, which may be GLOBUS_NULL. No memory is allocated in this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>auth_info</i> The authentication structure to initialize.<br />
 <i>credential_handle</i> The credential to use for authentication. This may be GSS_C_NO_CREDENTIAL to use the user&#8217;s default credential.<br />
 <i>encrypt</i> Boolean whether or not to encrypt the control channel for this handle.<br />
 <i>user</i> The user name<br />
 <i>password</i> The password for the user name<br />
 <i>account</i> The account for the user name/password<br />
 <i>subject</i> The GSSAPI subject name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Error object</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<h3>globus_result_t globus_ftp_control_authenticate (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_auth_info_t</code> *auth_info, globus_bool_tuse_auth, <code>globus_ftp_control_response_callback_t</code>callback, void *callback_arg)</h3>
<p> Authenticate the user to the FTP server. This will perform the authentication handshake with the FTP server. Depending on which parameters are non-NULL, the authentication may involve GSSAPI credentials, a username, a password, and an account name. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Do we want to add attribute arguments for:</p>
<dl>
<dt>&bull;</p>
<dd> specifying type of delegation</p>
<dt>&bull;</p>
<dd> gsswrap control messages for integrity or confidentiality</dl>
</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a unauthenticated GridFTP control handle. In the case of GSS authentication the GSS security context is stored in this structure.<br />
 <i>auth_info</i> This structure is used to pass the following information:</p>
<dl>
<dt>&bull;</p>
<dd> user The user&#8217;s name for login purposes. If this string is &#8216;anonymous&#8217;, &#8216;ftp&#8217;, GLOBUS_NULL or &#8216;:globus-mapping:&#8217; then the password argument is optional. If this string is GLOBUS_NULL or &#8216;:globus-mapping:&#8217; and gss_auth is true then the users login is looked by the FTP server host.</p>
<dt>&bull;</p>
<dd> password The password for the above user argument. If the user argument is &#8216;anonymous&#8217; or &#8216;ftp&#8217; or if gss_auth is true this string may be GLOBUS_NULL.</p>
<dt>&bull;</p>
<dd> account This parameter is optional. If not used it should be set to GLOBUS_NULL. It might be needed by firewalls.</p>
<dt>&bull;</p>
<dd> auth_gssapi_subject The GSSAPI subject name of the server you are connecting to. If this is GLOBUS_NULL, and the gss_auth parameter is set to GLOBUS_TRUE, then the name will default to the host name.</dl>
<p> <i>use_auth</i> If set to GLOBUS_TRUE the above argument indicates that GSS authentication should be used, otherwise cleartext user/password authentication is used.<br />
 <i>callback</i> The function to be called once the authentication process is complete or when an error occurs.<br />
 <i>callback_arg</i> User supplied argument to the callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> Null handle</p>
<dt>&bull;</p>
<dd> Invalid handle</p>
<dt>&bull;</p>
<dd> Handle already authenticated</dl>
</dl>
<p> <code>Callback errors:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> authentication failed</p>
<dt>&bull;</p>
<dd> protocol error</p>
<dt>&bull;</p>
<dd> eof</dl>
</dl>
<p> <code>Expected callback response values:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 230 User logged in, proceed.</p>
<dt>&bull;</p>
<dd> 232 User logged in, authorized by security data exchange.</p>
<dt>&bull;</p>
<dd> 234 Security data exchange complete.</p>
<dt>&bull;</p>
<dd> 331 User name okay, need password.</p>
<dt>&bull;</p>
<dd> 332 Need account for login.</p>
<dt>&bull;</p>
<dd> 336 Username okay, need password. Challenge is &#8216;&#8230;.&#8217;</p>
<dt>&bull;</p>
<dd> 431 Need some unavailable resource to process security.</p>
<dt>&bull;</p>
<dd> 500 Syntax error, command unrecognized.</p>
<dt>&bull;</p>
<dd> 530 Not logged in.</dl>
</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The server may send other responses. </p>
<p> The function <code>globus_ftp_control_authenticate_ex()</code> is identical except that the auth_info-&gt;req_flags is used. If delegation flags or any flags other than GSS_C_MUTUAL_FLAG and GSS_C_CONF_FLAG are desired, they must be set explicitly. It is the caller&#8217;s responsibility to ensure that req_flags only contains valid flags.</dl>
<h3>globus_result_t globus_ftp_control_authenticate_ex (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_auth_info_t</code> *auth_info, globus_bool_tuse_auth, <code>globus_ftp_control_response_callback_t</code>callback, void *callback_arg)</h3>
<p> Authenticate the user to the FTP server. This will perform the authentication handshake with the FTP server. Depending on which parameters are non-NULL, the authentication may involve GSSAPI credentials, a username, a password, and an account name. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Do we want to add attribute arguments for:</p>
<dl>
<dt>&bull;</p>
<dd> specifying type of delegation</p>
<dt>&bull;</p>
<dd> gsswrap control messages for integrity or confidentiality</dl>
</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a unauthenticated GridFTP control handle. In the case of GSS authentication the GSS security context is stored in this structure.<br />
 <i>auth_info</i> This structure is used to pass the following information:</p>
<dl>
<dt>&bull;</p>
<dd> user The user&#8217;s name for login purposes. If this string is &#8216;anonymous&#8217;, &#8216;ftp&#8217;, GLOBUS_NULL or &#8216;:globus-mapping:&#8217; then the password argument is optional. If this string is GLOBUS_NULL or &#8216;:globus-mapping:&#8217; and gss_auth is true then the users login is looked by the FTP server host.</p>
<dt>&bull;</p>
<dd> password The password for the above user argument. If the user argument is &#8216;anonymous&#8217; or &#8216;ftp&#8217; or if gss_auth is true this string may be GLOBUS_NULL.</p>
<dt>&bull;</p>
<dd> account This parameter is optional. If not used it should be set to GLOBUS_NULL. It might be needed by firewalls.</p>
<dt>&bull;</p>
<dd> auth_gssapi_subject The GSSAPI subject name of the server you are connecting to. If this is GLOBUS_NULL, and the gss_auth parameter is set to GLOBUS_TRUE, then the name will default to the host name.</dl>
<p> <i>use_auth</i> If set to GLOBUS_TRUE the above argument indicates that GSS authentication should be used, otherwise cleartext user/password authentication is used.<br />
 <i>callback</i> The function to be called once the authentication process is complete or when an error occurs.<br />
 <i>callback_arg</i> User supplied argument to the callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> Null handle</p>
<dt>&bull;</p>
<dd> Invalid handle</p>
<dt>&bull;</p>
<dd> Handle already authenticated</dl>
</dl>
<p> <code>Callback errors:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> authentication failed</p>
<dt>&bull;</p>
<dd> protocol error</p>
<dt>&bull;</p>
<dd> eof</dl>
</dl>
<p> <code>Expected callback response values:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 230 User logged in, proceed.</p>
<dt>&bull;</p>
<dd> 232 User logged in, authorized by security data exchange.</p>
<dt>&bull;</p>
<dd> 234 Security data exchange complete.</p>
<dt>&bull;</p>
<dd> 331 User name okay, need password.</p>
<dt>&bull;</p>
<dd> 332 Need account for login.</p>
<dt>&bull;</p>
<dd> 336 Username okay, need password. Challenge is &#8216;&#8230;.&#8217;</p>
<dt>&bull;</p>
<dd> 431 Need some unavailable resource to process security.</p>
<dt>&bull;</p>
<dd> 500 Syntax error, command unrecognized.</p>
<dt>&bull;</p>
<dd> 530 Not logged in.</dl>
</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The server may send other responses. </p>
<p> The function <code>globus_ftp_control_authenticate_ex()</code> is identical except that the auth_info-&gt;req_flags is used. If delegation flags or any flags other than GSS_C_MUTUAL_FLAG and GSS_C_CONF_FLAG are desired, they must be set explicitly. It is the caller&#8217;s responsibility to ensure that req_flags only contains valid flags.</dl>
<h3>globus_result_t globus_ftp_control_connect (globus_ftp_control_handle_t *handle, char *host, unsigned shortport, <code>globus_ftp_control_response_callback_t</code>callback, void *callback_arg)</h3>
<p> Create a new control connection to an FTP server. This function is used to initiate an FTP control connection. It creates the socket to the FTP server. When the connection is made to the server, and the server&#8217;s identification string is received, the callback function will be invoked. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a initialized FTP control handle. This handle will be used for all subsequent FTP control operations.<br />
 <i>host</i> The hostname of the FTP server.<br />
 <i>port</i> The TCP port number of the FTP server.<br />
 <i>callback</i> A function to be called once the connection to the server is established, and a response has been read.<br />
 <i>callback_arg</i> Parameter to the callback function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> Null handle</p>
<dt>&bull;</p>
<dd> Null host</p>
<dt>&bull;</p>
<dd> Illegal port number</p>
<dt>&bull;</p>
<dd> Null callback</p>
<dt>&bull;</p>
<dd> Cannot resolve hostname</p>
<dt>&bull;</p>
<dd> Cannot create socket</dl>
</dl>
<p> <code>Callback errors:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> connection refused</p>
<dt>&bull;</p>
<dd> protocol error</p>
<dt>&bull;</p>
<dd> eof</dl>
</dl>
<p> <code>Expected callback response values:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 120 Service ready in nnn minutes.</p>
<dt>&bull;</p>
<dd> 220 Service ready for new user.</p>
<dt>&bull;</p>
<dd> 421 Service not available, closing control connection.</p>
<dt>&bull;</p>
<dd> 500 Syntax error, command unrecognized.</dl>
</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The server may send other responses.</dl>
<h3>globus_result_t globus_ftp_control_force_close (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_response_callback_t</code>callback, void *callback_arg)</h3>
<p> Force a control connection to close. Force a close of the control connection without waiting for outstanding commands to complete and without sending QUIT. </p>
<p> This function is used to close the control channel to the FTP server. Once the final response callback passed to this function is invoked, the control handle can no longer be used for any GridFTP control operations. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Since this function waits until all other callbacks are completed before calling it&#8217;s own callback it may not be called in a blocking fashion from another callback.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a GridFTP control handle. The quit message is issued to the server over the control channel associated with this handle.<br />
 <i>callback</i> The function to be called once the authentication process is complete or when an error occurs.<br />
 <i>callback_arg</i> User supplied argument to the callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Success</p>
<dt>&bull;</p>
<dd> Null handle</dl>
</dl>
<p> <code>Callback errors:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> failure</dl>
</dl>
<p> <code>Expected callback response values:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_NULL</dl>
</dl>
<h3>globus_result_t globus_ftp_control_handle_destroy (globus_ftp_control_handle_t *handle)</h3>
<p> Destroy a globus ftp handle. This function will free up all dynamically allocated memory associated with a given globus ftp handle. It will also remove the handle from a list used by the module activation/deactivation functions. This function should only be called after a call to either globus_ftp_control_force_close or globus_ftp_control_quit. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to destroy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> invalid handle</p>
<dt>&bull;</p>
<dd> handle is still in connected state</dl>
</dl>
<h3>globus_result_t globus_ftp_control_handle_init (globus_ftp_control_handle_t *handle)</h3>
<p> Initialize a globus ftp handle. This function will set up (i.e. initialize all mutexes and variables) a globus ftp handle. It will also enter the handle in a list used by the module activation/deactivation functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to initialize.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</p>
<dt>&bull;</p>
<dd> error object</dl>
</dl>
<h3>globus_result_t globus_ftp_control_quit (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_response_callback_t</code>callback, void *callback_arg)</h3>
<p> Send a GridFTP QUIT. This function is used to close the control channel to the FTP server. There should be no transfer commands in progress when this is called. Once the final response callback passed to this function is invoked, the control handle can no longer be used for any GridFTP control operations. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Need to further define behavior for when a QUIT happens during a transfer or command is in progress. </p>
<p> Since this function waits until all other callbacks are completed before calling it&#8217;s own callback it may not be called in a blocking fashion from another callback.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a GridFTP control handle. The quit message is issued to the server over the control channel associated with this handle.<br />
 <i>callback</i> The function to be called once the authentication process is complete or when an error occurs.<br />
 <i>callback_arg</i> User supplied argument to the callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Success</p>
<dt>&bull;</p>
<dd> Null handle</p>
<dt>&bull;</p>
<dd> Command in progress</dl>
</dl>
<p> <code>Callback errors:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> protocol error</p>
<dt>&bull;</p>
<dd> eof</dl>
</dl>
<p> <code>Expected callback response values:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 221 Service closing control connection.</p>
<dt>&bull;</p>
<dd> 500 Syntax error, command unrecognized.</dl>
</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The server may send other responses.</dl>
<h3>globus_result_t globus_ftp_control_response_copy (globus_ftp_control_response_t *src, globus_ftp_control_response_t *dest)</h3>
<p> Copy a response structure. This is a helper function which copies one response structure to another. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>src</i> This parameter indicates the response structure to copy<br />
 <i>dest</i> This parameter specifies the target response structure</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Error object</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<h3>globus_result_t globus_ftp_control_response_destroy (globus_ftp_control_response_t *response)</h3>
<p> Free the memory associated with a response. This is a helper function which frees the memory associated with a response structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>response</i> This parameter indicates the response structure to destroy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Error object</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<h3>globus_result_t globus_ftp_control_send_command (globus_ftp_control_handle_t *handle, const char *cmdspec, <code>globus_ftp_control_response_callback_t</code>callback, void *callback_arg, &#8230;)</h3>
<p> Send an FTP protocol command. This function is used to send an FTP command, and register a handler to receive the FTP reply (or replies, if an intermediate one is sent). When the control channel is gss authenticated, the message and the reply will be automatically gss wrapped/unwrapped. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a GridFTP control handle. The command described by the cmdspec is issued to the server over the control channel associated with this handle.<br />
 <i>cmdspec</i> A printf-style format string containing the text of the command to send to the server. The optional parameters to the format string are passed after the callback_arg in the function invocation.<br />
 <i>callback</i> The function to be called once the authentication process is complete or when an error occurs.<br />
 <i>callback_arg</i> User supplied argument to the callback function<br />
 <i>&#8230;</i> Parameters which will be substituted into the % escapes in the cmdspec string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Success</p>
<dt>&bull;</p>
<dd> Null handle</p>
<dt>&bull;</p>
<dd> Command already in progress</dl>
</dl>
<p> <code>Callback errors:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> protocol error</p>
<dt>&bull;</p>
<dd> eof</dl>
</dl>
<p> <code>Expected callback response values:</code></p>
<dl>
<dt>
<dd> Any defined in RFC 959, 2228, 2389, draft-ietf-ftpext-mlst-10, or the <code>protocol extensions</code> document.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_control from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAS">Author</a></p>
<dd></dl>
