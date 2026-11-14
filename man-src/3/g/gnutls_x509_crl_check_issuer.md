---
title: "gnutls_x509_crl_check_issuer(3)"
name: "gnutls_x509_crl_check_issuer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_check_issuer/"
description: "gnutls_x509_crl_check_issuer – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_check_issuer &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_check_issuer(gnutls_x509_crl_t </code><i>crl</i><code>, gnutls_x509_crt_t </code><i>issuer</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_t crl</p>
<dd> is the CRL to be checked</p>
<dt>gnutls_x509_crt_t issuer</p>
<dd> is the certificate of a possible issuer</dl>
<h2>DESCRIPTION</h2>
<p> This function will check if the given CRL was issued by the given issuer certificate.</p>
<h2>RETURNS</h2>
<p> true (1) if the given CRL was issued by the given issuer, and false (0) if not.</p>
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
