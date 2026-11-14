---
title: "gnutls_privkey_import_dsa_raw(3)"
name: "gnutls_privkey_import_dsa_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_import_dsa_raw/"
description: "gnutls_privkey_import_dsa_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_privkey_import_dsa_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_privkey_import_dsa_raw(gnutls_privkey_t </code><i>key</i><code>, const gnutls_datum_t * </code><i>p</i><code>, const gnutls_datum_t * </code><i>q</i><code>, const gnutls_datum_t * </code><i>g</i><code>, const gnutls_datum_t * </code><i>y</i><code>, const gnutls_datum_t * </code><i>x</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t key</p>
<dd> The structure to store the parsed key</p>
<dt>const gnutls_datum_t * p</p>
<dd> holds the p</p>
<dt>const gnutls_datum_t * q</p>
<dd> holds the q</p>
<dt>const gnutls_datum_t * g</p>
<dd> holds the g</p>
<dt>const gnutls_datum_t * y</p>
<dd> holds the y</p>
<dt>const gnutls_datum_t * x</p>
<dd> holds the x</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the given DSA raw parameters to the native <code>gnutls_privkey_t</code> format. The output will be stored in <i>key</i> .</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
