---
title: "gnutls_pkcs11_privkey_export_pubkey(3)"
name: "gnutls_pkcs11_privkey_export_pubkey"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_privkey_export_pubkey/"
description: "gnutls_pkcs11_privkey_export_pubkey – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_privkey_export_pubkey &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_privkey_export_pubkey(gnutls_pkcs11_privkey_t </code><i>pkey</i><code>, gnutls_x509_crt_fmt_t </code><i>fmt</i><code>, gnutls_datum_t * </code><i>data</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs11_privkey_t pkey</dt>
<dd> The private key</dd>
<dt>gnutls_x509_crt_fmt_t fmt</dt>
<dd> the format of output params. PEM or DER.</dd>
<dt>gnutls_datum_t * data</dt>
<dd> will hold the public key</dd>
<dt>unsigned int flags</dt>
<dd> should be zero</dd></dl>
<h2>DESCRIPTION</h2>
<p> This function will extract the public key (modulus and public exponent) from the private key specified by the <i>url</i> private key. This public key will be stored in <i>pubkey</i> in the format specified by <i>fmt</i> . <i>pubkey</i> should be deinitialized using <code>gnutls_free()</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.3.7</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
<h2>Index</h2>
