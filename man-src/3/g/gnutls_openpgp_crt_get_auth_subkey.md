---
title: "gnutls_openpgp_crt_get_auth_subkey(3)"
name: "gnutls_openpgp_crt_get_auth_subkey"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_crt_get_auth_subkey/"
description: "gnutls_openpgp_crt_get_auth_subkey – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_crt_get_auth_subkey &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_crt_get_auth_subkey(gnutls_openpgp_crt_t </code><i>crt</i><code>, gnutls_openpgp_keyid_t </code><i>keyid</i><code>, unsigned int </code><i>flag</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_crt_t crt</p>
<dd> the structure that contains the OpenPGP public key.</p>
<dt>gnutls_openpgp_keyid_t keyid</p>
<dd> the struct to save the keyid.</p>
<dt>unsigned int flag</p>
<dd> Non-zero indicates that a valid subkey is always returned.</dl>
<h2>DESCRIPTION</h2>
<p> Returns the 64-bit keyID of the first valid OpenPGP subkey marked for authentication. If flag is non-zero and no authentication subkey exists, then a valid subkey will be returned even if it is not marked for authentication.</p>
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
