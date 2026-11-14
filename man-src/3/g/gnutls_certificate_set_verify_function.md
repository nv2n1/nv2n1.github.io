---
title: "gnutls_certificate_set_verify_function(3)"
name: "gnutls_certificate_set_verify_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_verify_function/"
description: "gnutls_certificate_set_verify_function – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_verify_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_certificate_set_verify_function(gnutls_certificate_credentials_t </code><i>cred</i><code>, gnutls_certificate_verify_function * </code><i>func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t cred</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</p>
<dt>gnutls_certificate_verify_function * func</p>
<dd> is the callback function</dl>
<h2>DESCRIPTION</h2>
<p> This function sets a callback to be called when peer&#8217;s certificate has been received in order to verify it on receipt rather than doing after the handshake is completed. </p>
<p> The callback&#8217;s function prototype is: int (*callback)(gnutls_session_t); </p>
<p> If the callback function is provided then gnutls will call it, in the handshake, just after the certificate message has been received. To verify or obtain the certificate the <code>gnutls_certificate_verify_peers2()</code>, <code>gnutls_certificate_type_get()</code>, <code>gnutls_certificate_get_peers()</code> functions can be used. </p>
<p> The callback function should return 0 for the handshake to continue or non-zero to terminate.</p>
<h2>SINCE</h2>
<p> 2.10.0</p>
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
