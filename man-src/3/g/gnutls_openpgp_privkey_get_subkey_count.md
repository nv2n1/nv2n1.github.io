---
title: "gnutls_openpgp_privkey_get_subkey_count(3)"
name: "gnutls_openpgp_privkey_get_subkey_count"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_privkey_get_subkey_count/"
description: "gnutls_openpgp_privkey_get_subkey_count – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_privkey_get_subkey_count &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_privkey_get_subkey_count(gnutls_openpgp_privkey_t </code><i>key</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_privkey_t key</p>
<dd> is an OpenPGP key</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the number of subkeys present in the given OpenPGP certificate.</p>
<h2>RETURNS</h2>
<p> the number of subkeys, or a negative error code on error.</p>
<h2>SINCE</h2>
<p> 2.4.0</p>
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
