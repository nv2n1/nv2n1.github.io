---
title: "gnutls_session_set_premaster(3)"
name: "gnutls_session_set_premaster"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_session_set_premaster/"
description: "gnutls_session_set_premaster – API function"
---

<h2>NAME</h2>
<p> gnutls_session_set_premaster &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_session_set_premaster(gnutls_session_t </code><i>session</i><code>, unsigned int </code><i>entity</i><code>, gnutls_protocol_t </code><i>version</i><code>, gnutls_kx_algorithm_t </code><i>kx</i><code>, gnutls_cipher_algorithm_t </code><i>cipher</i><code>, gnutls_mac_algorithm_t </code><i>mac</i><code>, gnutls_compression_method_t </code><i>comp</i><code>, const gnutls_datum_t * </code><i>master</i><code>, const gnutls_datum_t * </code><i>session_id</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>unsigned int entity</p>
<dd> GNUTLS_SERVER or GNUTLS_CLIENT</p>
<dt>gnutls_protocol_t version</p>
<dd> the TLS protocol version</p>
<dt>gnutls_kx_algorithm_t kx</p>
<dd> the key exchange method</p>
<dt>gnutls_cipher_algorithm_t cipher</p>
<dd> the cipher</p>
<dt>gnutls_mac_algorithm_t mac</p>
<dd> the MAC algorithm</p>
<dt>gnutls_compression_method_t comp</p>
<dd> the compression method</p>
<dt>const gnutls_datum_t * master</p>
<dd> the master key to use</p>
<dt>const gnutls_datum_t * session_id</p>
<dd> the session identifier</dl>
<h2>DESCRIPTION</h2>
<p> This function sets the premaster secret in a session. This is a function intended for exceptional uses. Do not use this function unless you are implementing a legacy protocol. Use <code>gnutls_session_set_data()</code> instead.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise an error code is returned.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></p>
<dd> </code></dl>
<h2>Index</h2>
