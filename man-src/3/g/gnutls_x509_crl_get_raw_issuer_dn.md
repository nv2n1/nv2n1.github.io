---
title: "gnutls_x509_crl_get_raw_issuer_dn(3)"
name: "gnutls_x509_crl_get_raw_issuer_dn"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_get_raw_issuer_dn/"
description: "gnutls_x509_crl_get_raw_issuer_dn – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_get_raw_issuer_dn &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_get_raw_issuer_dn(gnutls_x509_crl_t </code><i>crl</i><code>, gnutls_datum_t * </code><i>dn</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_t crl</p>
<dd> should contain a gnutls_x509_crl_t structure</p>
<dt>gnutls_datum_t * dn</p>
<dd> will hold the starting point of the DN</dl>
<h2>DESCRIPTION</h2>
<p> This function will return a pointer to the DER encoded DN structure and the length.</p>
<h2>RETURNS</h2>
<p> a negative error code on error, and (0) on success.</p>
<h2>SINCE</h2>
<p> 2.12.0</p>
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
