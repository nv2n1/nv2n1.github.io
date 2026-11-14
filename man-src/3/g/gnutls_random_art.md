---
title: "gnutls_random_art(3)"
name: "gnutls_random_art"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_random_art/"
description: "gnutls_random_art – API function"
---

<h2>NAME</h2>
<p> gnutls_random_art &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_random_art(gnutls_random_art_t </code><i>type</i><code>, const char * </code><i>key_type</i><code>, unsigned int </code><i>key_size</i><code>, void * </code><i>fpr</i><code>, size_t </code><i>fpr_size</i><code>, gnutls_datum_t * </code><i>art</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_random_art_t type</p>
<dd> The type of the random art (for now only <code>GNUTLS_RANDOM_ART_OPENSSH</code> is supported)</p>
<dt>const char * key_type</p>
<dd> The type of the key (RSA, DSA etc.)</p>
<dt>unsigned int key_size</p>
<dd> The size of the key in bits</p>
<dt>void * fpr</p>
<dd> The fingerprint of the key</p>
<dt>size_t fpr_size</p>
<dd> The size of the fingerprint</p>
<dt>gnutls_datum_t * art</p>
<dd> The returned random art</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert a given fingerprint to an &quot;artistic&quot; image. The returned image is allocated using <code>gnutls_malloc()</code>.</p>
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
