---
title: "gnutls_privkey_status(3)"
name: "gnutls_privkey_status"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_status/"
description: "gnutls_privkey_status – API function"
---

<h2>NAME</h2>
<p> gnutls_privkey_status &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_privkey_status(gnutls_privkey_t </code><i>key</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t key</p>
<dd> Holds the key</dl>
<h2>DESCRIPTION</h2>
<p> Checks the status of the private key token. This function is an actual wrapper over <code>gnutls_pkcs11_privkey_status()</code>, and if the private key is a PKCS <code>11</code> token it will check whether it is inserted or not.</p>
<h2>RETURNS</h2>
<p> this function will return non-zero if the token holding the private key is still available (inserted), and zero otherwise.</p>
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
