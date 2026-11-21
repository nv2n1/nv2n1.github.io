---
title: "gnutls_x509_privkey_import2(3)"
name: "gnutls_x509_privkey_import2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_privkey_import2/"
description: "gnutls_x509_privkey_import2 – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_privkey_import2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_privkey_import2(gnutls_x509_privkey_t </code><i>key</i><code>, const gnutls_datum_t * </code><i>data</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>, const char * </code><i>password</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_privkey_t key</dt>
<dd> The structure to store the parsed key</dd>
<dt>const gnutls_datum_t * data</dt>
<dd> The DER or PEM encoded key.</dd>
<dt>gnutls_x509_crt_fmt_t format</dt>
<dd> One of DER or PEM</dd>
<dt>const char * password</dt>
<dd> A password (optional)</dd>
<dt>unsigned int flags</dt>
<dd> an ORed sequence of gnutls_pkcs_encrypt_flags_t</dd></dl>
<h2>DESCRIPTION</h2>
<p> This function will import the given DER or PEM encoded key, to the native <code>gnutls_x509_privkey_t</code> format, irrespective of the input format. The input format is auto-detected. </p>
<p> The supported formats are basic unencrypted key, PKCS8, PKCS12, and the openssl format. </p>
<p> If the provided key is encrypted but no password was given, then <code>GNUTLS_E_DECRYPTION_FAILED</code> is returned.</p>
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
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
