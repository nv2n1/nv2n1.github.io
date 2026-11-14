---
title: "gnutls_pubkey_import_privkey(3)"
name: "gnutls_pubkey_import_privkey"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pubkey_import_privkey/"
description: "gnutls_pubkey_import_privkey – API function"
---

<h2>NAME</h2>
<p> gnutls_pubkey_import_privkey &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_pubkey_import_privkey(gnutls_pubkey_t </code><i>key</i><code>, gnutls_privkey_t </code><i>pkey</i><code>, unsigned int </code><i>usage</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pubkey_t key</p>
<dd> The public key</p>
<dt>gnutls_privkey_t pkey</p>
<dd> The private key</p>
<dt>unsigned int usage</p>
<dd> GNUTLS_KEY_* key usage flags.</p>
<dt>unsigned int flags</p>
<dd> should be zero</dl>
<h2>DESCRIPTION</h2>
<p> Imports the public key from a private. This function will import the given public key to the abstract <code>gnutls_pubkey_t</code> structure.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 2.12.0</p>
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
