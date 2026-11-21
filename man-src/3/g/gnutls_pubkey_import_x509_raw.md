---

title: "gnutls_pubkey_import_x509_raw(3)"
name: "gnutls_pubkey_import_x509_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pubkey_import_x509_raw/"
description: "gnutls_pubkey_import_x509_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_pubkey_import_x509_raw &#8211; API function</p>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_pubkey_import_x509_raw(gnutls_pubkey_t </code><i>pkey</i><code>, const gnutls_datum_t * </code><i>data</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pubkey_t pkey</dt>
<dd> The public key</dd>
<dt>const gnutls_datum_t * data</dt>
<dd> The public key data to be imported</dd>
<dt>gnutls_x509_crt_fmt_t format</dt>
<dd> The format of the public key</dd>
<dt>unsigned int flags</dt>
<dd> should be zero</dd></dl>
<p> This function will import the given public key to the abstract <code>gnutls_pubkey_t</code> structure.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.1.3</p>
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
