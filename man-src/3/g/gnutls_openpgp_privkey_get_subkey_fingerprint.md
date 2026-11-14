---
title: "gnutls_openpgp_privkey_get_subkey_fingerprint(3)"
name: "gnutls_openpgp_privkey_get_subkey_fingerprint"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_privkey_get_subkey_fingerprint/"
description: "gnutls_openpgp_privkey_get_subkey_fingerprint – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_privkey_get_subkey_fingerprint &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_privkey_get_subkey_fingerprint(gnutls_openpgp_privkey_t </code><i>key</i><code>, unsigned int </code><i>idx</i><code>, void * </code><i>fpr</i><code>, size_t * </code><i>fprlen</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_privkey_t key</p>
<dd> the raw data that contains the OpenPGP secret key.</p>
<dt>unsigned int idx</p>
<dd> the subkey index</p>
<dt>void * fpr</p>
<dd> the buffer to save the fingerprint, must hold at least 20 bytes.</p>
<dt>size_t * fprlen</p>
<dd> the integer to save the length of the fingerprint.</dl>
<h2>DESCRIPTION</h2>
<p> Get the fingerprint of an OpenPGP subkey. Depends on the algorithm, the fingerprint can be 16 or 20 bytes.</p>
<h2>RETURNS</h2>
<p> On success, 0 is returned, or an error code.</p>
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
