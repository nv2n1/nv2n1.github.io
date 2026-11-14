---
title: "gnutls_pkcs7_import(3)"
name: "gnutls_pkcs7_import"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs7_import/"
description: "gnutls_pkcs7_import – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs7_import &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_pkcs7_import(gnutls_pkcs7_t </code><i>pkcs7</i><code>, const gnutls_datum_t * </code><i>data</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs7_t pkcs7</p>
<dd> The structure to store the parsed PKCS7.</p>
<dt>const gnutls_datum_t * data</p>
<dd> The DER or PEM encoded PKCS7.</p>
<dt>gnutls_x509_crt_fmt_t format</p>
<dd> One of DER or PEM</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the given DER or PEM encoded PKCS7 to the native <code>gnutls_pkcs7_t</code> format. The output will be stored in<br />
&nbsp;<wbr><i>pkcs7</i>&nbsp;<wbr>. </p>
<p> If the PKCS7 is PEM encoded it should have a header of &quot;PKCS7&quot;.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
