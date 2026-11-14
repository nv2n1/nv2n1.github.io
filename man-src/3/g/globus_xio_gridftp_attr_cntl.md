---
title: "globus_xio_gridftp_attr_cntl(3)"
name: "globus_xio_gridftp_attr_cntl"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_gridftp_attr_cntl/"
description: "globus_xio_gridftp_driver.h – XIO GRIDFTP Client Driver."
---

<h2 class="name">NAME</h2>
<p> globus_xio_gridftp_driver.h &#8211; XIO GRIDFTP Client Driver.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_xio_system.h&#8217;<br />
 #include &#8216;globus_common.h&#8217; </p>
<h3>Typedefs</h3>
<p> typedef enum<br />
 <code>globus_l_xio_gridftp_mode_e</code> <code>globus_l_xio_gridftp_mode_t</code>&quot; </p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_gridftp_error_type_t</code> { <code>GLOBUS_XIO_GRIDFTP_ERROR_ATTR</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_SEEK</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_READ</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_WRITE</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_READ</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_WRITE</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_PARTIAL_XFER</code> } </p>
<p> enum <code>globus_xio_gridftp_cmd_t</code> { <code>GLOBUS_XIO_GRIDFTP_SEEK</code>, <code>GLOBUS_XIO_GRIDFTP_SET_HANDLE</code>, <code>GLOBUS_XIO_GRIDFTP_GET_HANDLE</code>, <code>GLOBUS_XIO_GRIDFTP_SET_APPEND</code>, <code>GLOBUS_XIO_GRIDFTP_GET_APPEND</code>, <code>GLOBUS_XIO_GRIDFTP_SET_ERET</code>, <code>GLOBUS_XIO_GRIDFTP_GET_ERET</code>, <code>GLOBUS_XIO_GRIDFTP_SET_ESTO</code>, <code>GLOBUS_XIO_GRIDFTP_GET_ESTO</code>, <code>GLOBUS_XIO_GRIDFTP_SET_PARTIAL_TRANSFER</code>, <code>GLOBUS_XIO_GRIDFTP_GET_PARTIAL_TRANSFER</code>, <code>GLOBUS_XIO_GRIDFTP_SET_NUM_STREAMS</code>, <code>GLOBUS_XIO_GRIDFTP_GET_NUM_STREAMS</code>, <code>GLOBUS_XIO_GRIDFTP_SET_TCP_BUFFER</code>, <code>GLOBUS_XIO_GRIDFTP_GET_TCP_BUFFER</code>, <code>GLOBUS_XIO_GRIDFTP_SET_MODE</code>, <code>GLOBUS_XIO_GRIDFTP_GET_MODE</code>, <code>GLOBUS_XIO_GRIDFTP_SET_AUTH</code>, <code>GLOBUS_XIO_GRIDFTP_GET_AUTH</code>, <code>GLOBUS_XIO_GRIDFTP_SET_DCAU</code>, <code>GLOBUS_XIO_GRIDFTP_GET_DCAU</code>, <code>GLOBUS_XIO_GRIDFTP_SET_DATA_PROTECTION</code>, <code>GLOBUS_XIO_GRIDFTP_GET_DATA_PROTECTION</code>, <code>GLOBUS_XIO_GRIDFTP_SET_CONTROL_PROTECTION</code>, <code>GLOBUS_XIO_GRIDFTP_GET_CONTROL_PROTECTION</code> } </p>
<p> enum <code>globus_l_xio_gridftp_mode_e</code> </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_xio_gridftp_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GRIDFTP_SEEK</code>, globus_off_t seek_offset) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_HANDLE</code>, globus_ftp_client_handle_t *ftp_handle) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_HANDLE</code>, globus_ftp_client_handle_t **ftp_handle_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_APPEND</code>, globus_bool_t append) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_APPEND</code>, globus_bool_t *append_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_ERET</code>, const char *eret_alg_str) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_ERET</code>, char **eret_alg_str_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_ESTO</code>, const char *esto_alg_str) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_ESTO</code>, char **esto_alg_str_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_PARTIAL_TRANSFER</code>, globus_bool_t partial_xfer) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_PARTIAL_TRANSFER</code>, globus_bool_t *partial_xfer_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_NUM_STREAMS</code>, int num_streams) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_NUM_STREAMS</code>, int *num_streams_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_TCP_BUFFER</code>, int buf_size) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_TCP_BUFFER</code>, int *buf_size_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_MODE</code>, int mode) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_MODE</code>, int *mode_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_AUTH</code>, gss_cred_id_t credential, const char *user, const char *password, const char *account, const char *subject) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_AUTH</code>, gss_cred_id_t *credential_out, const char **user_out, const char **password_out, const char **account_out, const char **subject_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_DCAU</code>, int dcau_mode) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_DCAU</code>, int *dcau_mode_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_DATA_PROTECTION</code>, int protection) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_DATA_PROTECTION</code>, int *protection_out) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_CONTROL_PROTECTION</code>, int protection) </p>
<p> globus_result_t <code>globus_xio_gridftp_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_CONTROL_PROTECTION</code>, int *protection_out) </p>
<h2>Detailed Description</h2>
<p> XIO GRIDFTP Client Driver. </p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_HANDLE</code>, globus_ftp_client_handle_t *ftp_handle)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the ftp client handle to use. </p>
<p> Do not create a new ftp client handle, use this handle instead. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ftp_handle</i> Specifies the pointer to globus ftp client handle. Note: this handle will not be destroyed.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_HANDLE</code>, globus_ftp_client_handle_t **ftp_handle_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the ftp client handle on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ftp_handle_out</i> The ftp client handle pointer will be stored here. If none is set, NULL will be set.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_APPEND</code>, globus_bool_tappend)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Enable or disable opening the file in append mode. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>append</i> GLOBUS_TRUE to enable, GLOBUS_FALSE to disable (default).</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_APPEND</code>, globus_bool_t *append_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the append flag on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>append_out</i> The append flag will be stored here.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_ERET</code>, const char *eret_alg_str)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the ERET algorithm string. This string contains information needed to invoke a server-specific data reduction algorithm on the file being retrieved. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>eret_alg_str</i> Specifies the ERET algorithm string.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_ERET</code>, char **eret_alg_str_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the ERET algorithm string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>eret_alg_str_out</i> The ERET algorithm string will be stored here. It is the responsibility of the user to free the memory allocated for this string.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_ESTO</code>, const char *esto_alg_str)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the ESTO algorithm string. This string contains information needed to invoke a server-specific data reduction algorithm on the file being stored. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>esto_alg_str</i> Specifies the ESTO algorithm string.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_ESTO</code>, char **esto_alg_str_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the ESTO algorithm string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>esto_alg_str_out</i> The ESTO algorithm string will be stored here. It is the responsibility of the user to free the memory allocated for this string.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_PARTIAL_TRANSFER</code>, globus_bool_tpartial_xfer)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Enable or disable partial transfer (associate a transfer with each read/write) on the GridFTP handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>partial_xfer</i> GLOBUS_TRUE to enable, GLOBUS_FALSE to disable (default).</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_PARTIAL_TRANSFER</code>, globus_bool_t *partial_xfer_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the partial transfer flag on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>partial_xfer_out</i> The partial xfer flag will be stored here.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_NUM_STREAMS</code>, intnum_streams)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the number of TCP streams to be used between the client and the server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>num_streams</i> Specifies the number of streams to use.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_NUM_STREAMS</code>, int *num_streams_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the number of TCP streams on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>num_streams_out</i> The stream count will be stored here.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_TCP_BUFFER</code>, intbuf_size)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the TCP socket send/recv buffer size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buf_size</i> The send/recv buffer size in bytes to use. (default is system specific)</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_TCP_BUFFER</code>, int *buf_size_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the TCP socket send/recv buffer size on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buf_size_out</i> The send/recv buffer size will be stored here.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_MODE</code>, intmode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the transmission mode used for data transfer </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mode</i> Specifies the data transmission mode. (default is stream mode)</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_l_xio_gridftp_mode_t</code></dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_MODE</code>, int *mode_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the data transmission mode on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mode_out</i> The data transmission mode will be stored here.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_l_xio_gridftp_mode_t</code></dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_AUTH</code>, gss_cred_id_tcredential, const char *user, const char *password, const char *account, const char *subject)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the authentication information used to authenticate with the GridFTP server </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>credential</i> The credential to use for authenticating with a GridFTP server. This may be GSS_C_NO_CREDENTIAL to use the default credential.<br />
 <i>user</i> The user name to send to the GridFTP server. When doing a GSI transfer, this may be set to NULL, and the default gridmap entry for the user&#8217;s GSI identity will be used<br />
 <i>password</i> The password to send to the GridFTP server. When doing a GSI transfer, this may be set to NULL.<br />
 <i>account</i> The account to use for the data transfer.<br />
 <i>subject</i> The subject name of the GridFTP server. This is only used when doing a GSI transfer, and then only when the security subject name does not match the hostname of the server (ie, when the server is being run by a user).</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_AUTH</code>, gss_cred_id_t *credential_out, const char **user_out, const char **password_out, const char **account_out, const char **subject_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the authentication information on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>credential_out</i> The credential will be stored here.<br />
 <i>user_out</i> The user name will be stored here.<br />
 <i>password_out</i> The password will be stored here.<br />
 <i>account_out</i> The account information will be stored here.<br />
 <i>subject_out</i> The subject name will be stored here.</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_DCAU</code>, intdcau_mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the mode of authentication to be performed on GridFTP data channels. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dcau_mode</i> Specifies the authentication mode.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_l_xio_gridftp_dcau_mode_t</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_DCAU</code>, int *dcau_mode_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the data channel authentication mode on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dcau_mode_out</i> The data channel authentication mode will be stored here.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_l_xio_gridftp_dcau_mode_t</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_DATA_PROTECTION</code>, intprotection)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set protection level on the data channel. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>protection</i> Specifies the protection level.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_l_xio_gridftp_protection_t</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_DATA_PROTECTION</code>, int *protection_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the data channel protection level on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>protection_out</i> The data channel protection level will be stored here.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_l_xio_gridftp_dcau_mode_t</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_SET_CONTROL_PROTECTION</code>, intprotection)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set protection level on the control channel. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>protection</i> Specifies the protection level.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_l_xio_gridftp_protection_t</dl>
<h3>globus_result_t globus_xio_gridftp_attr_cntl (attr, driver, <code>GLOBUS_XIO_GRIDFTP_GET_CONTROL_PROTECTION</code>, int *protection_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the control channel protection level on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>protection_out</i> The control channel protection level will be stored here.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_l_xio_gridftp_protection_t</dl>
<h3>globus_result_t globus_xio_gridftp_handle_cntl (handle, driver, <code>GLOBUS_XIO_GRIDFTP_SEEK</code>, globus_off_tseek_offset)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Reposition the offset of the file being read/written. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>seek_offset</i> Specifies the desired offset.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio_gridftp_driver from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBH">Author</a></p>
<dd></dl>
