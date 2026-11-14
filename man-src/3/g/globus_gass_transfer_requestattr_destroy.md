---
title: "globus_gass_transfer_requestattr_destroy(3)"
name: "globus_gass_transfer_requestattr_destroy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_requestattr_destroy/"
description: "Request Attributes –"
---

<h2 class="name">NAME</h2>
<p> Request Attributes &#8211; </p>
<h3>Functions</h3>
<p> int <code>globus_gass_transfer_requestattr_init</code> (globus_gass_transfer_requestattr_t *attr, char *url_scheme) </p>
<p> int <code>globus_gass_transfer_requestattr_destroy</code> (globus_gass_transfer_requestattr_t *attr) </p>
<h3>Proxy Server</h3>
<p> int <code>globus_gass_transfer_requestattr_set_proxy_url</code> (globus_gass_transfer_requestattr_t *attr, char *proxy_url) </p>
<p> int <code>globus_gass_transfer_requestattr_get_proxy_url</code> (globus_gass_transfer_requestattr_t *attr, char **proxy_url) </p>
<h3>Block Size</h3>
<p> int <code>globus_gass_transfer_requestattr_set_block_size</code> (globus_gass_transfer_requestattr_t *attr, globus_size_t block_size) </p>
<p> int <code>globus_gass_transfer_requestattr_get_block_size</code> (globus_gass_transfer_requestattr_t *attr, globus_size_t *block_size) </p>
<h3>File Mode</h3>
<p> int <code>globus_gass_transfer_requestattr_set_file_mode</code> (globus_gass_transfer_requestattr_t *attr, globus_gass_transfer_file_mode_t file_mode) </p>
<p> int <code>globus_gass_transfer_requestattr_get_file_mode</code> (globus_gass_transfer_requestattr_t *attr, globus_gass_transfer_file_mode_t *file_mode) </p>
<h3>Connection Reuse</h3>
<p> int <code>globus_gass_transfer_requestattr_set_connection_reuse</code> (globus_gass_transfer_requestattr_t *attr, globus_bool_t connection_reuse) </p>
<p> int <code>globus_gass_transfer_requestattr_get_connection_reuse</code> (globus_gass_transfer_requestattr_t *attr, globus_bool_t *connection_reuse) </p>
<h3>Socket Send Buffer Size</h3>
<p> int <code>globus_gass_transfer_requestattr_set_socket_sndbuf</code> (globus_gass_transfer_requestattr_t *attr, int sndbuf) </p>
<p> int <code>globus_gass_transfer_requestattr_get_socket_sndbuf</code> (globus_gass_transfer_requestattr_t *attr, int *sndbuf) </p>
<h3>Receive Socket Buffer</h3>
<p> int <code>globus_gass_transfer_requestattr_set_socket_rcvbuf</code> (globus_gass_transfer_requestattr_t *attr, int rcvbuf) </p>
<p> int <code>globus_gass_transfer_requestattr_get_socket_rcvbuf</code> (globus_gass_transfer_requestattr_t *attr, int *rcvbuf) </p>
<h3>TCP Nodelay</h3>
<p> int <code>globus_gass_transfer_requestattr_set_socket_nodelay</code> (globus_gass_transfer_requestattr_t *attr, globus_bool_t nodelay) </p>
<p> int <code>globus_gass_transfer_requestattr_get_socket_nodelay</code> (globus_gass_transfer_requestattr_t *attr, globus_bool_t *nodelay) </p>
<h3>Authorization</h3>
<p> int <code>globus_gass_transfer_secure_requestattr_set_authorization</code> (globus_gass_transfer_requestattr_t *attr, globus_gass_transfer_authorization_t mode, char *subject) </p>
<p> int <code>globus_gass_transfer_secure_requestattr_get_authorization</code> (globus_gass_transfer_requestattr_t *attr, globus_gass_transfer_authorization_t *mode, char **subject) </p>
<h2>Detailed Description</h2>
<p> The GASS Transfer library uses Globus objects to provide an extensible way of creating protocol-specific attributes.</p>
<h2>Function Documentation</h2>
<h3>int globus_gass_transfer_requestattr_destroy (globus_gass_transfer_requestattr_t *attr)</h3>
<p> Destroy a request attribute. </p>
<p> This function destroys the attribute set specified in <i>attr</i>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to be destroyed.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully destroyed.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h3>int globus_gass_transfer_requestattr_init (globus_gass_transfer_requestattr_t *attr, char *url_scheme)</h3>
<p> Initialize a request attribute. </p>
<p> This function initializes the <i>attr</i> to contain a new protocol-specific request attribute. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to be initialized.<br />
 <i>url_scheme</i> The scheme which which the attribute will be used for.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully initialized.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> Either <i>attr</i> or <i>url_scheme</i> was GLOBUS_NULL.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> No protocol module currently registered with GASS Transfer Library handles URLs with the specified <i>url_scheme</i>.</dl>
<h3>int globus_gass_transfer_requestattr_set_block_size (globus_gass_transfer_requestattr_t *attr, globus_size_tblock_size)</h3>
<p> Set/Get the block size attribute for a GASS transfer attribute set. </p>
<p> This attribute allows the user to suggest a preferred block size of a server to handle a URL request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>block_size</i> The data block size that should be used to process requests with this attribute set.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully updated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h3>int globus_gass_transfer_requestattr_set_connection_reuse (globus_gass_transfer_requestattr_t *attr, globus_bool_tconnection_reuse)</h3>
<p> Set/Get the connection reuse attribute for a GASS transfer attribute set. </p>
<p> This attribute allows the user to control whether the connection associated with a GASS Transfer request should be reused after the file transfer has completed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>connection_reuse</i> The value of the connection reuse attribute.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully updated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h3>int globus_gass_transfer_requestattr_set_file_mode (globus_gass_transfer_requestattr_t *attr, globus_gass_transfer_file_mode_tfile_mode)</h3>
<p> Set/Get the file mode attribute for a GASS transfer attribute set. </p>
<p> This attribute allows the user to control whether the file will be transferred in ASCII or binary file mode. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>file_mode</i> The value of the file mode attribute.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully updated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h3>int globus_gass_transfer_requestattr_set_proxy_url (globus_gass_transfer_requestattr_t *attr, char *proxy_url)</h3>
<p> Set/Get the proxy server attribute for a GASS transfer attribute set. </p>
<p> This attribute allows the user to use a proxy server to handle a URL request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to be modified<br />
 <i>proxy_url</i> The new value of the proxy_url attribute. This may be GLOBUS_NULL if no proxy is to be used to access URLs with this attribute set.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully updated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h3>int globus_gass_transfer_requestattr_set_socket_nodelay (globus_gass_transfer_requestattr_t *attr, globus_bool_tnodelay)</h3>
<p> Set/Get the TCP nodelay attribute for a GASS transfer attribute set. </p>
<p> This attribute allows the user to control the socket receive buffer associated with a GASS Transfer request should be reused after the file transfer has completed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>nodelay</i> The value of the nodelay attribute.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully updated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h3>int globus_gass_transfer_requestattr_set_socket_rcvbuf (globus_gass_transfer_requestattr_t *attr, intrcvbuf)</h3>
<p> Set/Get the receive buffer size attribute for a GASS transfer attribute set. </p>
<p> This attribute allows the user to control the socket receive buffer associated with a GASS Transfer request should be reused after the file transfer has completed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>rcvbuf</i> The value of the socket buffer.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully updated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h3>int globus_gass_transfer_requestattr_set_socket_sndbuf (globus_gass_transfer_requestattr_t *attr, intsndbuf)</h3>
<p> Set/Get the send buffer size attribute for a GASS transfer attribute set. </p>
<p> This attribute allows the user to control the socket send buffer associated with a GASS Transfer request should be reused after the file transfer has completed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>sndbuf</i> The value of the socket buffer.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully updated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h3>int globus_gass_transfer_secure_requestattr_set_authorization (globus_gass_transfer_requestattr_t *attr, globus_gass_transfer_authorization_tmode, char *subject)</h3>
<p> Set/Get the authorization attribute for a GASS transfer attribute set. </p>
<p> This attribute allows the user to control what type of authorization should be done when GASS Transfer requests are processed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>mode</i> The authorization mode to use.<br />
 <i>subject</i> The subject name of the authorized subject, if <i>mode</i> is GLOBUS_GASS_TRANSFER_AUTHORIZE_SUBJECT</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully updated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
