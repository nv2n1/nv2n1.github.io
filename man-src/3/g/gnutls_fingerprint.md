---
title: "gnutls_fingerprint(3)"
name: "gnutls_fingerprint"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_fingerprint/"
description: "gnutls_fingerprint – API function"
---

<h2>NAME</h2>
<p> gnutls_fingerprint &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_fingerprint(gnutls_digest_algorithm_t </code><i>algo</i><code>, const gnutls_datum_t * </code><i>data</i><code>, void * </code><i>result</i><code>, size_t * </code><i>result_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_digest_algorithm_t algo</p>
<dd> is a digest algorithm</p>
<dt>const gnutls_datum_t * data</p>
<dd> is the data</p>
<dt>void * result</p>
<dd> is the place where the result will be copied (may be null).</p>
<dt>size_t * result_size</p>
<dd> should hold the size of the result. The actual size of the returned result will also be copied there.</dl>
<h2>DESCRIPTION</h2>
<p> This function will calculate a fingerprint (actually a hash), of the given data. The result is not printable data. You should convert it to hex, or to something else printable. </p>
<p> This is the usual way to calculate a fingerprint of an X.509 DER encoded certificate. Note however that the fingerprint of an OpenPGP certificate is not just a hash and cannot be calculated with this function.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise an error code is returned.</p>
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
