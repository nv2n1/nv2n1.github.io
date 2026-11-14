---
title: "gnutls_x509_privkey_verify_data(3)"
name: "gnutls_x509_privkey_verify_data"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_privkey_verify_data/"
description: "gnutls_x509_privkey_verify_data – Verify the signed data using private key"
---

<h2>NAME</h2>
<p> gnutls_x509_privkey_verify_data &#8211; Verify the signed data using private key</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/x509.h">gnutls/x509.h</a>&gt;</code> </p>
<p> <code>int gnutls_x509_privkey_verify_data(gnutls_x509_privkey_t </code><i>key</i><code>, unsigned int </code><i>flags</i><code>, const gnutls_datum_t * </code><i>data</i><code>, const gnutls_datum_t * </code><i>signature</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_privkey_t key</p>
<dd> Holds the key</p>
<dt>unsigned int flags</p>
<dd> should be 0 for now</p>
<dt>const gnutls_datum_t * data</p>
<dd> holds the data to be signed</p>
<dt>const gnutls_datum_t * signature</p>
<dd> contains the signature</dl>
<h2>DESCRIPTION</h2>
<p> This function will verify the given signed data, using the parameters in the private key.</p>
<h2>RETURNS</h2>
<p> In case of a verification failure 0 is returned, and 1 on success.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnutls [at] gnu.org&gt;. GnuTLS home page: <a rel="nofollow" href="http://www.gnu.org/software/gnutls/">http://www.gnu.org/software/gnutls/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Free Software Foundation.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gnutls</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gnutls</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
