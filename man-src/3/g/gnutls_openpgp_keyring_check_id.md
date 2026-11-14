---
title: "gnutls_openpgp_keyring_check_id(3)"
name: "gnutls_openpgp_keyring_check_id"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_keyring_check_id/"
description: "gnutls_openpgp_keyring_check_id – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_keyring_check_id &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_keyring_check_id(gnutls_openpgp_keyring_t </code><i>ring</i><code>, const gnutls_openpgp_keyid_t </code><i>keyid</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_keyring_t ring</p>
<dd> holds the keyring to check against</p>
<dt>const gnutls_openpgp_keyid_t keyid</p>
<dd> will hold the keyid to check for.</p>
<dt>unsigned int flags</p>
<dd> unused (should be 0)</dl>
<h2>DESCRIPTION</h2>
<p> Check if a given key ID exists in the keyring.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success (if keyid exists) and a negative error code on failure.</p>
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
