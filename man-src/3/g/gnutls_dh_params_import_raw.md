---
title: "gnutls_dh_params_import_raw(3)"
name: "gnutls_dh_params_import_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_dh_params_import_raw/"
description: "gnutls_dh_params_import_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_dh_params_import_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_dh_params_import_raw(gnutls_dh_params_t </code><i>dh_params</i><code>, const gnutls_datum_t * </code><i>prime</i><code>, const gnutls_datum_t * </code><i>generator</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_dh_params_t dh_params</p>
<dd> Is a structure that will hold the prime numbers</p>
<dt>const gnutls_datum_t * prime</p>
<dd> holds the new prime</p>
<dt>const gnutls_datum_t * generator</p>
<dd> holds the new generator</dl>
<h2>DESCRIPTION</h2>
<p> This function will replace the pair of prime and generator for use in the Diffie-Hellman key exchange. The new parameters should be stored in the appropriate gnutls_datum.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
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
