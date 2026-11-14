---
title: "gnutls_openpgp_crt_get_subkey_revoked_status(3)"
name: "gnutls_openpgp_crt_get_subkey_revoked_status"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_crt_get_subkey_revoked_status/"
description: "gnutls_openpgp_crt_get_subkey_revoked_status – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_crt_get_subkey_revoked_status &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_crt_get_subkey_revoked_status(gnutls_openpgp_crt_t </code><i>key</i><code>, unsigned int </code><i>idx</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_crt_t key</p>
<dd> the structure that contains the OpenPGP public key.</p>
<dt>unsigned int idx</p>
<dd> is the subkey index</dl>
<h2>DESCRIPTION</h2>
<p> Get subkey revocation status. A negative error code indicates an error.</p>
<h2>RETURNS</h2>
<p> true (1) if the key has been revoked, or false (0) if it has not.</p>
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
