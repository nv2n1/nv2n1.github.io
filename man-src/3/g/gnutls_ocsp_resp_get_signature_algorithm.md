---
title: "gnutls_ocsp_resp_get_signature_algorithm(3)"
name: "gnutls_ocsp_resp_get_signature_algorithm"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_resp_get_signature_algorithm/"
description: "gnutls_ocsp_resp_get_signature_algorithm – API function"
---

<h2>NAME</h2>
<p> gnutls_ocsp_resp_get_signature_algorithm &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_resp_get_signature_algorithm(gnutls_ocsp_resp_t </code><i>resp</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_resp_t resp</p>
<dd> should contain a <code>gnutls_ocsp_resp_t</code> structure</dl>
<h2>DESCRIPTION</h2>
<p> This function will return a value of the <code>gnutls_sign_algorithm_t</code> enumeration that is the signature algorithm that has been used to sign the OCSP response.</p>
<h2>RETURNS</h2>
<p> a <code>gnutls_sign_algorithm_t</code> value, or a negative error code on error.</p>
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
