---
title: "gnutls_openpgp_keyring_import(3)"
name: "gnutls_openpgp_keyring_import"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_keyring_import/"
description: "gnutls_openpgp_keyring_import – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_keyring_import &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_keyring_import(gnutls_openpgp_keyring_t </code><i>keyring</i><code>, const gnutls_datum_t * </code><i>data</i><code>, gnutls_openpgp_crt_fmt_t </code><i>format</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_keyring_t keyring</p>
<dd> The structure to store the parsed key.</p>
<dt>const gnutls_datum_t * data</p>
<dd> The RAW or BASE64 encoded keyring.</p>
<dt>gnutls_openpgp_crt_fmt_t format</p>
<dd> One of <code>gnutls_openpgp_keyring_fmt</code> elements.</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the given RAW or Base64 encoded keyring to the native <code>gnutls_openpgp_keyring_t</code> format. The output will be stored in &#8216;keyring&#8217;.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an error code.</p>
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
