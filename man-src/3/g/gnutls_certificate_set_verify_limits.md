---
title: "gnutls_certificate_set_verify_limits(3)"
name: "gnutls_certificate_set_verify_limits"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_verify_limits/"
description: "gnutls_certificate_set_verify_limits – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_verify_limits &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_certificate_set_verify_limits(gnutls_certificate_credentials_t </code><i>res</i><code>, unsigned int </code><i>max_bits</i><code>, unsigned int </code><i>max_depth</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t res</p>
<dd> is a gnutls_certificate_credentials structure</p>
<dt>unsigned int max_bits</p>
<dd> is the number of bits of an acceptable certificate (default 8200)</p>
<dt>unsigned int max_depth</p>
<dd> is maximum depth of the verification of a certificate chain (default 5)</dl>
<h2>DESCRIPTION</h2>
<p> This function will set some upper limits for the default verification function, <code>gnutls_certificate_verify_peers2()</code>, to avoid denial of service attacks. You can set them to zero to disable limits.</p>
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
