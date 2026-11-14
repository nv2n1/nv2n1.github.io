---
title: "gnutls_privkey_sign_raw_data(3)"
name: "gnutls_privkey_sign_raw_data"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_sign_raw_data/"
description: "gnutls_privkey_sign_raw_data – API function"
---

<h2>NAME</h2>
<p> gnutls_privkey_sign_raw_data &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_privkey_sign_raw_data(gnutls_privkey_t </code><i>key</i><code>, unsigned </code><i>flags</i><code>, const gnutls_datum_t * </code><i>data</i><code>, gnutls_datum_t * </code><i>signature</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t key</p>
<dd> Holds the key</p>
<dt>unsigned flags</p>
<dd> should be zero</p>
<dt>const gnutls_datum_t * data</p>
<dd> holds the data to be signed</p>
<dt>gnutls_datum_t * signature</p>
<dd> will contain the signature allocate with <code>gnutls_malloc()</code></dl>
<h2>DESCRIPTION</h2>
<p> This function will sign the given data using a signature algorithm supported by the private key. Note that this is a low-level function and does not apply any preprocessing or hash on the signed data. For example on an RSA key the input <i>data</i> should be of the DigestInfo PKCS <code>1</code> 1.5 format. Use it only if you know what are you doing. </p>
<p> Note this function is equivalent to using the <code>GNUTLS_PRIVKEY_SIGN_FLAG_TLS1_RSA</code> flag with <code>gnutls_privkey_sign_hash()</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.1.10</p>
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
