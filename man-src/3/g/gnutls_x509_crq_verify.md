---
title: "gnutls_x509_crq_verify(3)"
name: "gnutls_x509_crq_verify"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_verify/"
description: "gnutls_x509_crq_verify – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_verify &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_verify(gnutls_x509_crq_t </code><i>crq</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> is the crq to be verified</p>
<dt>unsigned int flags</p>
<dd> Flags that may be used to change the verification algorithm. Use OR of the gnutls_certificate_verify_flags enumerations.</dl>
<h2>DESCRIPTION</h2>
<p> This function will verify self signature in the certificate request and return its status.</p>
<h2>RETURNS</h2>
<p> In case of a verification failure <code>GNUTLS_E_PK_SIG_VERIFY_FAILED</code> is returned, and zero or positive code on success. </p>
<p> Since 2.12.0</p>
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
