---
title: "gnutls_certificate_set_openpgp_keyring_mem(3)"
name: "gnutls_certificate_set_openpgp_keyring_mem"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_openpgp_keyring_mem/"
description: "gnutls_certificate_set_openpgp_keyring_mem – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_openpgp_keyring_mem &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_certificate_set_openpgp_keyring_mem(gnutls_certificate_credentials_t </code><i>c</i><code>, const uint8_t * </code><i>data</i><code>, size_t </code><i>dlen</i><code>, gnutls_openpgp_crt_fmt_t </code><i>format</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t c</p>
<dd> A certificate credentials structure</p>
<dt>const uint8_t * data</p>
<dd> buffer with keyring data.</p>
<dt>size_t dlen</p>
<dd> length of data buffer.</p>
<dt>gnutls_openpgp_crt_fmt_t format</p>
<dd> the format of the keyring</dl>
<h2>DESCRIPTION</h2>
<p> The function is used to set keyrings that will be used internally by various OpenPGP functions. For example to find a key when it is needed for an operations. The keyring will also be used at the verification functions.</p>
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
