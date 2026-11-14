---
title: "gnutls_rsa_params_import_pkcs1(3)"
name: "gnutls_rsa_params_import_pkcs1"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_rsa_params_import_pkcs1/"
description: "gnutls_rsa_params_import_pkcs1 – API function"
---

<h2>NAME</h2>
<p> gnutls_rsa_params_import_pkcs1 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_rsa_params_import_pkcs1(gnutls_rsa_params_t </code><i>params</i><code>, const gnutls_datum_t * </code><i>pkcs1_params</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_rsa_params_t params</p>
<dd> A structure where the parameters will be copied to</p>
<dt>const gnutls_datum_t * pkcs1_params</p>
<dd> should contain a PKCS1 RSAPrivateKey structure PEM or DER encoded</p>
<dt>gnutls_x509_crt_fmt_t format</p>
<dd> the format of params. PEM or DER.</dl>
<h2>DESCRIPTION</h2>
<p> This function will extract the RSAPrivateKey found in a PKCS1 formatted structure. </p>
<p> If the structure is PEM encoded, it should have a header of &quot;BEGIN RSA PRIVATE KEY&quot;.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an negative error code.</p>
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
