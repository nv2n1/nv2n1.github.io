---
title: "gnutls_credentials_set(3)"
name: "gnutls_credentials_set"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_credentials_set/"
description: "gnutls_credentials_set – API function"
---

<h2>NAME</h2>
<p> gnutls_credentials_set &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_credentials_set(gnutls_session_t </code><i>session</i><code>, gnutls_credentials_type_t </code><i>type</i><code>, void * </code><i>cred</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_credentials_type_t type</p>
<dd> is the type of the credentials</p>
<dt>void * cred</p>
<dd> is a pointer to a structure.</dl>
<h2>DESCRIPTION</h2>
<p> Sets the needed credentials for the specified type. Eg username, password &#8211; or public and private keys etc. The <i>cred</i> parameter is a structure that depends on the specified type and on the current session (client or server). </p>
<p> In order to minimize memory usage, and share credentials between several threads gnutls keeps a pointer to cred, and not the whole cred structure. Thus you will have to keep the structure allocated until you call <code>gnutls_deinit()</code>. </p>
<p> For <code>GNUTLS_CRD_ANON</code>, <i>cred</i> should be <code>gnutls_anon_client_credentials_t</code> in case of a client. In case of a server it should be <code>gnutls_anon_server_credentials_t</code>. </p>
<p> For <code>GNUTLS_CRD_SRP</code>, <i>cred</i> should be <code>gnutls_srp_client_credentials_t</code> in case of a client, and <code>gnutls_srp_server_credentials_t</code>, in case of a server. </p>
<p> For <code>GNUTLS_CRD_CERTIFICATE</code>, <i>cred</i> should be <code>gnutls_certificate_credentials_t</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
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
