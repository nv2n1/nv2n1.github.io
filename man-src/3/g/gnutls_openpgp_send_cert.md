---
title: "gnutls_openpgp_send_cert(3)"
name: "gnutls_openpgp_send_cert"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_send_cert/"
description: "gnutls_openpgp_send_cert – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_send_cert &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_openpgp_send_cert(gnutls_session_t </code><i>session</i><code>, gnutls_openpgp_crt_status_t </code><i>status</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a pointer to a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_openpgp_crt_status_t status</p>
<dd> is one of GNUTLS_OPENPGP_CERT, or GNUTLS_OPENPGP_CERT_FINGERPRINT</dl>
<h2>DESCRIPTION</h2>
<p> This function will order gnutls to send the key fingerprint instead of the key in the initial handshake procedure. This should be used with care and only when there is indication or knowledge that the server can obtain the client&#8217;s key.</p>
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
