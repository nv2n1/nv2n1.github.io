---
title: "gnutls_openpgp_crt_verify_ring(3)"
name: "gnutls_openpgp_crt_verify_ring"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_crt_verify_ring/"
description: "gnutls_openpgp_crt_verify_ring – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_crt_verify_ring &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_crt_verify_ring(gnutls_openpgp_crt_t </code><i>key</i><code>, gnutls_openpgp_keyring_t </code><i>keyring</i><code>, unsigned int </code><i>flags</i><code>, unsigned int * </code><i>verify</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_crt_t key</p>
<dd> the structure that holds the key.</p>
<dt>gnutls_openpgp_keyring_t keyring</p>
<dd> holds the keyring to check against</p>
<dt>unsigned int flags</p>
<dd> unused (should be 0)</p>
<dt>unsigned int * verify</p>
<dd> will hold the certificate verification output.</dl>
<h2>DESCRIPTION</h2>
<p> Verify all signatures in the key, using the given set of keys (keyring). </p>
<p> The key verification output will be put in <i>verify</i> and will be one or more of the <code>gnutls_certificate_status_t</code> enumerated elements bitwise or&#8217;d. </p>
<p> Note that this function does not verify using any &quot;web of trust&quot;. You may use GnuPG for that purpose, or any other external PGP application.</p>
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
