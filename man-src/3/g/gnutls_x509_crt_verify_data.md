---
title: "gnutls_x509_crt_verify_data(3)"
name: "gnutls_x509_crt_verify_data"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_verify_data/"
description: "gnutls_x509_crt_verify_data – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_verify_data &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_verify_data(gnutls_x509_crt_t </code><i>crt</i><code>, unsigned int </code><i>flags</i><code>, const gnutls_datum_t * </code><i>data</i><code>, const gnutls_datum_t * </code><i>signature</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t crt</p>
<dd> Holds the certificate</p>
<dt>unsigned int flags</p>
<dd> should be 0 for now</p>
<dt>const gnutls_datum_t * data</p>
<dd> holds the data to be signed</p>
<dt>const gnutls_datum_t * signature</p>
<dd> contains the signature</dl>
<h2>DESCRIPTION</h2>
<p> This function will verify the given signed data, using the parameters from the certificate. </p>
<p> Deprecated. This function cannot be easily used securely. Use <code>gnutls_pubkey_verify_data2()</code> instead.</p>
<h2>RETURNS</h2>
<p> In case of a verification failure <code>GNUTLS_E_PK_SIG_VERIFY_FAILED</code> is returned, and zero or positive code on success.</p>
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
