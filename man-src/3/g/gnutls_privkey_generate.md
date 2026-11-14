---
title: "gnutls_privkey_generate(3)"
name: "gnutls_privkey_generate"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_generate/"
description: "gnutls_privkey_generate – API function"
---

<h2>NAME</h2>
<p> gnutls_privkey_generate &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_privkey_generate(gnutls_privkey_t </code><i>pkey</i><code>, gnutls_pk_algorithm_t </code><i>algo</i><code>, unsigned int </code><i>bits</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t pkey</p>
<dd> The private key</p>
<dt>gnutls_pk_algorithm_t algo</p>
<dd> is one of the algorithms in <code>gnutls_pk_algorithm_t</code>.</p>
<dt>unsigned int bits</p>
<dd> the size of the modulus</p>
<dt>unsigned int flags</p>
<dd> unused for now. Must be 0.</dl>
<h2>DESCRIPTION</h2>
<p> This function will generate a random private key. Note that this function must be called on an empty private key. </p>
<p> Note that when generating an elliptic curve key, the curve can be substituted in the place of the bits parameter using the <code>GNUTLS_CURVE_TO_BITS()</code> macro. </p>
<p> Do not set the number of bits directly, use <code>gnutls_sec_param_to_pk_bits()</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.3.0</p>
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
