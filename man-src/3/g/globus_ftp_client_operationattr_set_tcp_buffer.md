---
title: "globus_ftp_client_operationattr_set_tcp_buffer(3)"
name: "globus_ftp_client_operationattr_set_tcp_buffer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_operationattr_set_tcp_buffer/"
description: "FTP Operation Attributes –"
---

<h2 class="name">NAME</h2>
<p> FTP Operation Attributes &#8211; </p>
<h3>Data Structures</h3>
<p> struct <code>globus_i_ftp_client_range_t</code><br />
 <i>Byte range report.</i> </p>
<p> This structure contains information about a single extent of data stored on an FTP server. A report structure is generated from each part of an extended-block mode restart marker message from an FTP server. &quot;</p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 <code>globus_i_ftp_client_operationattr_t</code> * <code>globus_ftp_client_operationattr_t</code>&quot;<br />
 <i>Operation Attributes.</i> </p>
<p> FTP Client attributes are used to control the parameters needed to access an URL using the FTP protocol. Attributes are created and manipulated using the functions in the <code>attributes </code> section of the library. &quot;</p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_init</code> (<code>globus_ftp_client_operationattr_t</code> *attr) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_destroy</code> (<code>globus_ftp_client_operationattr_t</code> *attr) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_delayed_pasv</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t delayed_pasv) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_copy</code> (<code>globus_ftp_client_operationattr_t</code> *dst, const <code>globus_ftp_client_operationattr_t</code> *src) </p>
<h3>Storage Module</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_storage_module</code> (<code>globus_ftp_client_operationattr_t</code> *attr, const char *module_name, const char *module_args) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_storage_module</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, char **module_name, char **module_args) </p>
<h3>Custom Data Channel Driver Stack</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_net_stack</code> (<code>globus_ftp_client_operationattr_t</code> *attr, const char *driver_list) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_net_stack</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, char **driver_list) </p>
<h3>Custom Server File Driver Stack</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_disk_stack</code> (<code>globus_ftp_client_operationattr_t</code> *attr, const char *driver_list) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_disk_stack</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, char **driver_list) </p>
<h3>Parallelism</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_parallelism</code> (<code>globus_ftp_client_operationattr_t</code> *attr, const globus_ftp_control_parallelism_t *parallelism) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_parallelism</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_parallelism_t *parallelism) </p>
<h3>allocate</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_allocate</code> (<code>globus_ftp_client_operationattr_t</code> *attr, const globus_off_t allocated_size) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_allocate</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_off_t *allocated_size) </p>
<h3>authz_assert</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_authz_assert</code> (<code>globus_ftp_client_operationattr_t</code> *attr, const char *authz_assert, globus_bool_t cache_authz_assert) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_authz_assert</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, char **authz_assert, globus_bool_t *cache_authz_assert) </p>
<h3>Striped Data Movement</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_striped</code> (<code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t striped) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_striped</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t *striped) </p>
<h3>Striped File Layout</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_layout</code> (<code>globus_ftp_client_operationattr_t</code> *attr, const globus_ftp_control_layout_t *layout) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_layout</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_layout_t *layout) </p>
<h3>TCP Buffer</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_tcp_buffer</code> (<code>globus_ftp_client_operationattr_t</code> *attr, const globus_ftp_control_tcpbuffer_t *tcp_buffer) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_tcp_buffer</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_tcpbuffer_t *tcp_buffer) </p>
<h3>File Type</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_type</code> (<code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_type_t type) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_type</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_type_t *type) </p>
<h3>Transfer Mode</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_mode</code> (<code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_mode_t mode) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_mode</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_mode_t *mode) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_list_uses_data_mode</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t list_uses_data_mode) </p>
<h3>Authorization</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_authorization</code> (<code>globus_ftp_client_operationattr_t</code> *attr, gss_cred_id_t credential, const char *user, const char *password, const char *account, const char *subject) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_authorization</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, gss_cred_id_t *credential, char **user, char **password, char **account, char **subject) </p>
<h3>Data Channel Authentication</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_dcau</code> (<code>globus_ftp_client_operationattr_t</code> *attr, const globus_ftp_control_dcau_t *dcau) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_dcau</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_dcau_t *dcau) </p>
<h3>Data Channel Protection</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_data_protection</code> (<code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_protection_t protection) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_data_protection</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_protection_t *protection) </p>
<h3>Data Channel Security Context</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_data_security</code> (<code>globus_ftp_client_operationattr_t</code> *attr, int type, void *credential) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_data_security</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, int *type, void **credential) </p>
<h3>Control Channel Protection</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_control_protection</code> (<code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_protection_t protection) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_control_protection</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_protection_t *protection) </p>
<h3>Append</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_append</code> (<code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t append) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_append</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t *append) </p>
<h3>IPv6</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_allow_ipv6</code> (<code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t allow_ipv6) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_allow_ipv6</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t *allow_ipv6) </p>
<h3>Read into a Single Buffer</h3>
<p> globus_result_t <code>globus_ftp_client_operationattr_set_read_all</code> (<code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t read_all, <code>globus_ftp_client_data_callback_t</code> intermediate_callback, void *intermediate_callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_operationattr_get_read_all</code> (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t *read_all, <code>globus_ftp_client_data_callback_t</code> *intermediate_callback, void **intermediate_callback_arg) </p>
<h2>Detailed Description</h2>
<p> Operation attributes are used to control the security and performance of an FTP operation. These features are often dependent on the capabilities of the FTP server which you are going to access.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>globus_i_ftp_client_operationattr_t</code>* <code>globus_ftp_client_operationattr_t</code></h3>
<p> Operation Attributes. </p>
<p> FTP Client attributes are used to control the parameters needed to access an URL using the FTP protocol. Attributes are created and manipulated using the functions in the <code>attributes </code> section of the library. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_operationattr_init()</code>, <code>globus_ftp_client_operationattr_destroy()</code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_operationattr_copy (<code>globus_ftp_client_operationattr_t</code> *dst, const <code>globus_ftp_client_operationattr_t</code> *src)</h3>
<p> Create a duplicate of an attribute set. </p>
<p> The duplicated attribute set has a deep copy of all data in the attribute set, so the original may be destroyed, while the copy is still valid. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dst</i> The attribute set to be initialized to the same values as src.<br />
 <i>src</i> The original attribute set to duplicate.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_destroy (<code>globus_ftp_client_operationattr_t</code> *attr)</h3>
<p> Destroy an FTP client attribute set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> A pointer to the attribute to destroy.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_init (<code>globus_ftp_client_operationattr_t</code> *attr)</h3>
<p> Initialize an FTP client attribute set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> A pointer to the new attribute set.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_allocate (<code>globus_ftp_client_operationattr_t</code> *attr, const globus_off_tallocated_size)</h3>
<p> Set/Get the allocate attribute for an ftp client attribute set. </p>
<p> This attribute lets the user set a size to be passed to the server before a put operation. </p>
<p> This attribute is ignored for get operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>allocated_size</i> The size to direct server to allocate.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_allow_ipv6 (<code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_tallow_ipv6)</h3>
<p> Set/Get the allow ipv6 attribute for an ftp client attribute set. </p>
<p> This attribute allows client library to make use of ipv6 when possible. </p>
<p> Use of this is currently very experimental. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>allow_ipv6</i> GLOBUS_TRUE to allow ipv6 or GLOBUS_FALSE to disallow(default)</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_append (<code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_tappend)</h3>
<p> Set/Get the append attribute for an ftp client attribute set. </p>
<p> This attribute allows the user to append to a file on an FTP server, instead of replacing the existing file when doing a <code>globus_ftp_client_put()</code> or globus_ftp_client_transfer(). </p>
<p> This attribute is ignored on the retrieving side of a transfer, or a <code>globus_ftp_client_get()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>append</i> The value of append attribute.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_authorization (<code>globus_ftp_client_operationattr_t</code> *attr, gss_cred_id_tcredential, const char *user, const char *password, const char *account, const char *subject)</h3>
<p> Set/Get the authorization attribute for an ftp client attribute set. </p>
<p> This attribute allows the user to pass authentication information to the ftp client library. This information is used to authenticate with the ftp server. </p>
<p> The Globus FTP client library supports authentication using either the GSSAPI, or standard plaintext username and passwords. The type of authentication is determined by the URL scheme which is used for the individual get, put, or 3rd party transfer calls. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>credential</i> The credential to use for authenticating with a GSIFTP server. This may be GSS_C_NO_CREDENTIAL to use the default credential.<br />
 <i>user</i> The user name to send to the FTP server. When doing a gsiftp transfer, this may be set to NULL, and the default globusmap entry for the user&#8217;s GSI identity will be usd.<br />
 <i>password</i> The password to send to the FTP server. When doing a gsiftp transfer, this may be set to NULL.<br />
 <i>account</i> The account to use for the data transfer. Most FTP servers do not require this.<br />
 <i>subject</i> The subject name of the FTP server. This is only used when doing a gsiftp transfer, and then only when the security subject name does not match the hostname of the server (ie, when the server is being run by a user).</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_authz_assert (<code>globus_ftp_client_operationattr_t</code> *attr, const char *authz_assert, globus_bool_tcache_authz_assert)</h3>
<p> Set/Get the authz_assert attribute for an ftp client attribute set. </p>
<p> This attribute lets the user set an AUTHORIZATION assertion to be passed to the server </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>authz_assert</i> The AUTHORIZATION assertion.<br />
 <i>cache_authz_assert</i> Boolean that specifies whether to cache this assertion for subsequent operations</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_control_protection (<code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_protection_tprotection)</h3>
<p> Set/Get the control channel protection attribute for an ftp client attribute set. </p>
<p> The control channel protection attribute allows the user to decide whether to encrypt or integrity check the command session between the client and the FTP server. This attribute is only relevant if used with a gsiftp URL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>protection</i> The value of control channel protection attribute.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The clear and safe protection levels are treated identically, with the client integrity checking all commands. The confidential and private protection levels are treated identically, with the client encrypting all commands.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_data_protection (<code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_protection_tprotection)</h3>
<p> Set/Get the data channel protection attribute for an ftp client attribute set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>protection</i> The value of data channel protection attribute.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Only safe and private protection levels are supported by gsiftp.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_data_security (<code>globus_ftp_client_operationattr_t</code> *attr, inttype, void *credential)</h3>
<p> Set/Get the data channel security context type and credential. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>type</i> The type of credential. Currently only &#8216;P&#8217; is supported, and requires a gss_cred_id_t for the credential.<br />
 <i>credential</i> A credential appropriate for the type specified.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_dcau (<code>globus_ftp_client_operationattr_t</code> *attr, const globus_ftp_control_dcau_t *dcau)</h3>
<p> Set/Get the data channel authentication attribute for an ftp client attribute set. </p>
<p> Data channel authentication is a GridFTP extension, and may not be supported by all servers. If a server supports it, then the default is to delegate a credential to the server, and authenticate all data channels with that delegated credential. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>dcau</i> The value of data channel authentication attribute.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_delayed_pasv (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_tdelayed_pasv)</h3>
<p> Set/Get whether or not delayed passive should be used </p>
<p> This attribute allows the user to enable delayed passive so the server can provide the passive address after it knows the filename to be transferred. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>delayed_pasv</i> globus_bool_t</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Delayed passive is a GridFTP extension, and may not be supported on all FTP servers.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_disk_stack (<code>globus_ftp_client_operationattr_t</code> *attr, const char *driver_list)</h3>
<p> Set/Get the gridftp xio driver stack used for the file storage. </p>
<p> This attribute allows the user to control which xio drivers will be used for file DSI only. This is an experimental feature of the gridftp server. Only works for third party transfers. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>driver_list</i> driver list in the following format: driver1[:driver1opts][,driver2[:driver2opts]][&#8230;]. The string &#8216;default&#8217; will reset the stack list to the server default.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is a GridFTP extension, and may not be supported on all FTP servers.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_layout (<code>globus_ftp_client_operationattr_t</code> *attr, const globus_ftp_control_layout_t *layout)</h3>
<p> Set/Get the layout attribute for an ftp client attribute set. </p>
<p> This attribute allows the user to control the layout of a file being transferred to a striped Grid-FTP server. The striping layout defines what regions of a file will be stored on each stripe of a multiple-striped ftp server. </p>
<p> The layout attribute is used only when the data is being stored on the server (on a put or 3rd party transfer). This attribute is ignored for stream mode data transfers. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>layout</i> The value of layout attribute.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd>
&nbsp;<wbr><code>globus_ftp_client_operationattr_set_parallelism()</code>,&nbsp;<wbr><code>globus_ftp_client_operationattr_set_mode()</code></dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is a Grid-FTP extension, and may not be supported on all FTP servers.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_list_uses_data_mode (const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_tlist_uses_data_mode)</h3>
<p> Set/Get whether or not list data will use the current data mode </p>
<p> This attribute allows the user to allow list data to be transferred using the current data channel mode. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>list_uses_data_mode</i> globus_bool_t</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> List data transfers in nonstandard modes is a Grid-FTP extension, and may not be supported on all FTP servers.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_mode (<code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_mode_tmode)</h3>
<p> Set/Get the file transfer mode attribute for an ftp client attribute set. </p>
<p> This attribute allows the user to choose the data channel protocol used to transfer a file. There are two modes supported by this library: stream mode and extended block mode. </p>
<p> Stream mode is a file transfer mode where all data is sent over a single TCP socket, without any data framing. In stream mode, data will arrive in sequential order. This mode is supported by nearly all FTP servers. </p>
<p> Extended block mode is a file transfer mode where data can be sent over multiple parallel connections and to multiple data storage nodes to provide a high-performance data transfer. In extended block mode, data may arrive out-of-order. ASCII type files are not supported in extended block mode. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>mode</i> The value of mode attribute</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd>
&nbsp;<wbr><code>globus_ftp_client_operationattr_set_parallelism()</code>,&nbsp;<wbr><code>globus_ftp_client_operationattr_set_layout()</code></dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Extended block mode is a Grid-FTP extension, and may not be supported on all FTP servers.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_net_stack (<code>globus_ftp_client_operationattr_t</code> *attr, const char *driver_list)</h3>
<p> Set/Get the gridftp xio driver stack used for the data channel. </p>
<p> This attribute allows the user to control which xio drivers will be used for data transport. The driver MUST be installed and allowed by the server or the transfer/get/put will result in an error. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>driver_list</i> driver list in the following format: driver1[:driver1opts][,driver2[:driver2opts]][&#8230;]. The string &#8216;default&#8217; will reset the stack list to the server default.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is a GridFTP extension, and may not be supported on all FTP servers.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_parallelism (<code>globus_ftp_client_operationattr_t</code> *attr, const globus_ftp_control_parallelism_t *parallelism)</h3>
<p> Set/Get the parallelism attribute for an ftp client attribute set. </p>
<p> This attribute allows the user to control the level of parallelism to be used on an extended block mode file transfer. Currently, only a &#8216;fixed&#8217; parallelism level is supported. This is interpreted by the FTP server as the number of parallel data connections to be allowed for each stripe of data. Currently, only the &#8216;fixed&#8217; parallelism type is </p>
<p> This attribute is ignored in stream mode. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>parallelism</i> The value of parallelism attribute.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd>
&nbsp;<wbr><code>globus_ftp_client_operationattr_set_layout()</code>,&nbsp;<wbr><code>globus_ftp_client_operationattr_set_mode()</code></dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is a Grid-FTP extension, and may not be supported on all FTP servers.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_read_all (<code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_tread_all, <code>globus_ftp_client_data_callback_t</code>intermediate_callback, void *intermediate_callback_arg)</h3>
<p> Set/Get the read_all attribute for an ftp client attribute set. </p>
<p> This attribute allows the user to pass in a single buffer to receive all of the data for the current transfer. This buffer must be large enough to hold all of the data for the transfer. Only one buffer may be registered with <code>globus_ftp_client_register_read()</code> when this attribute is used for a get. </p>
<p> In extended block mode, this attribute will cause data to be stored directly into the buffer from multiple streams without any extra data copies. </p>
<p> If the user sets the intermediate callback to a non-null value, this function will be called whenever an intermediate sub-section of the data is received into the buffer. </p>
<p> This attribute is ignored for <code>globus_ftp_client_put()</code> or <code>globus_ftp_client_third_party_transfer()</code> operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>read_all</i> The value of read_all attribute.<br />
 <i>intermediate_callback</i> Callback to be invoked when a subsection of the data has been retreived. This callback may be GLOBUS_NULL, if the user only wants to be notified when the data transfer is completed.<br />
 <i>intermediate_callback_arg</i> User data to be passed to the intermediate callback function.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_storage_module (<code>globus_ftp_client_operationattr_t</code> *attr, const char *module_name, const char *module_args)</h3>
<p> Set/Get the gridftp storage module (DSI). </p>
<p> This attribute allows the user to control what backend module they use with the gridftp server. The module MUST be implemented by the server or the transfer/get/put will result in an error. </p>
<p> This attribute is ignored in stream mode. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>module_name</i> The backend storage module name<br />
 <i>module_args</i> The backend storage module parameters</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is a Grid-FTP extension, and may not be supported on all FTP servers.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_striped (<code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_tstriped)</h3>
<p> Set/Get the striped attribute for an ftp client attribute set. </p>
<p> This attribute allows the user to force the client library to used the FTP commands to do a striped data transfer, even when the user has not requested a specific file layout via the layout attribute. This is useful when transferring files between servers which use the server side processing commands ERET or ESTO to transform data and send it to particular stripes on the destination server. </p>
<p> The layout attribute is used only when the data is being stored the server (on a put or 3rd party transfer). This attribute is ignored for stream mode data transfers. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>striped</i> The value of striped attribute.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_operationattr_set_parallelism()</code>, <code>globus_ftp_client_operationattr_set_layout()</code> <code>globus_ftp_client_operationattr_set_mode()</code></dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is a Grid-FTP extension, and may not be supported on all FTP servers.</dl>
<h3>globus_result_t globus_ftp_client_operationattr_set_tcp_buffer (<code>globus_ftp_client_operationattr_t</code> *attr, const globus_ftp_control_tcpbuffer_t *tcp_buffer)</h3>
<p> Set/Get the TCP buffer attribute for an ftp client attribute set. </p>
<p> This attribute allows the user to control the TCP buffer size used for all data channels used in a file transfer. The size of the TCP buffer can make a significant impact on the performance of a file transfer. The user may set the buffer to either a system-dependent default value, or to a fixed value. </p>
<p> The actual implementation of this attribute is designed to be as widely interoperable as possible. In addition to supporting the SBUF command described in the GridFTP protocol extensions document, it also supports other commands and site commands which are used by other servers to set TCP buffer sizes. These are</p>
<dl>
<dt>&bull;</p>
<dd> SITE RETRBUFSIZE</p>
<dt>&bull;</p>
<dd> SITE RBUFSZ</p>
<dt>&bull;</p>
<dd> SITE RBUFSIZ</p>
<dt>&bull;</p>
<dd> SITE STORBUFIZE</p>
<dt>&bull;</p>
<dd> SITE SBUFSZ</p>
<dt>&bull;</p>
<dd> SITE SBUFSIZ</p>
<dt>&bull;</p>
<dd> SITE BUFSIZE</dl>
<p> This attribute is affects any type of data transfer done with the ftp client library. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>tcp_buffer</i> The value of tcp_buffer attribute.</dl>
<p>&nbsp;<wbr></p>
<h3>globus_result_t globus_ftp_client_operationattr_set_type (<code>globus_ftp_client_operationattr_t</code> *attr, globus_ftp_control_type_ttype)</h3>
<p> Set/Get the file representation type attribute for an ftp client attribute set. </p>
<p> This attribute allows the user to choose the file type used for an FTP file transfer. The file may be transferred as either ASCII or a binary image. </p>
<p> When transferring an ASCII file, the data will be transformed in the following way</p>
<dl>
<dt>&bull;</p>
<dd> the high-order bit will be set to zero</p>
<dt>&bull;</p>
<dd> end-of line characters will be converted to a CRLF pair for the data transfer, and then converted to native format before being returned to the user&#8217;s data callbacks.</dl>
<p> The default type for the ftp client library is binary. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>type</i> The value of type attribute.</dl>
<p>&nbsp;<wbr></p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBB">Function Documentation</a></p>
<dd>
<dt><a href="#lbCA">Author</a></p>
<dd></dl>
