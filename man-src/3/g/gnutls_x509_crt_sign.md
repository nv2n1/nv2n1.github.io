---
title: "gnutls_x509_crt_sign(3)"
name: "gnutls_x509_crt_sign"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_sign/"
description: "gnutls_x509_crt_sign – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_sign &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_sign(gnutls_x509_crt_t </code><i>crt</i><code>, gnutls_x509_crt_t </code><i>issuer</i><code>, gnutls_x509_privkey_t </code><i>issuer_key</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t crt</p>
<dd> a certificate of type <code>gnutls_x509_crt_t</code></p>
<dt>gnutls_x509_crt_t issuer</p>
<dd> is the certificate of the certificate issuer</p>
<dt>gnutls_x509_privkey_t issuer_key</p>
<dd> holds the issuer&#8217;s private key</dl>
<h2>DESCRIPTION</h2>
<p> This function is the same a <code>gnutls_x509_crt_sign2()</code> with no flags, and SHA1 as the hash algorithm.</p>
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
