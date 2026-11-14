---
title: "gnutls_openpgp_set_recv_key_function(3)"
name: "gnutls_openpgp_set_recv_key_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_set_recv_key_function/"
description: "gnutls_openpgp_set_recv_key_function – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_set_recv_key_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>void gnutls_openpgp_set_recv_key_function(gnutls_session_t </code><i>session</i><code>, gnutls_openpgp_recv_key_func </code><i>func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> a TLS session</p>
<dt>gnutls_openpgp_recv_key_func func</p>
<dd> the callback</dl>
<h2>DESCRIPTION</h2>
<p> This funtion will set a key retrieval function for OpenPGP keys. This callback is only useful in server side, and will be used if the peer sent a key fingerprint instead of a full key. </p>
<p> The retrieved key must be allocated using <code>gnutls_malloc()</code>.</p>
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
