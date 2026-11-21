---

title: "gnutls_pubkey_export_ecc_raw(3)"
name: "gnutls_pubkey_export_ecc_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pubkey_export_ecc_raw/"
description: "gnutls_pubkey_export_ecc_raw – API function"
---

<p> gnutls_pubkey_export_ecc_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_pubkey_export_ecc_raw(gnutls_pubkey_t </code><i>key</i><code>, gnutls_ecc_curve_t * </code><i>curve</i><code>, gnutls_datum_t * </code><i>x</i><code>, gnutls_datum_t * </code><i>y</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pubkey_t key</dt>
<dd> Holds the public key</dd>
<dt>gnutls_ecc_curve_t * curve</dt>
<dd> will hold the curve</dd>
<dt>gnutls_datum_t * x</dt>
<dd> will hold x</dd>
<dt>gnutls_datum_t * y</dt>
<dd> will hold y</dd></dl>
<h2>DESCRIPTION</h2>
<p> This function will export the ECC public key&#8217;s parameters found in the given certificate. The new parameters will be allocated using <code>gnutls_malloc()</code> and will be stored in the appropriate datum.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, otherwise a negative error code.</p>
<h2>SINCE</h2>
<p> 3.0</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
