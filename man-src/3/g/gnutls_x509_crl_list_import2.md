---
title: "gnutls_x509_crl_list_import2(3)"
name: "gnutls_x509_crl_list_import2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_list_import2/"
description: "gnutls_x509_crl_list_import2 – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_list_import2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_list_import2(gnutls_x509_crl_t ** </code><i>crls</i><code>, unsigned int * </code><i>size</i><code>, const gnutls_datum_t * </code><i>data</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_t ** crls</p>
<dd> The structures to store the parsed crl list. Must not be initialized.</p>
<dt>unsigned int * size</p>
<dd> It will contain the size of the list.</p>
<dt>const gnutls_datum_t * data</p>
<dd> The PEM encoded CRL.</p>
<dt>gnutls_x509_crt_fmt_t format</p>
<dd> One of DER or PEM.</p>
<dt>unsigned int flags</p>
<dd> must be (0) or an OR&#8217;d sequence of gnutls_certificate_import_flags.</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the given PEM encoded CRL list to the native gnutls_x509_crl_t format. The output will be stored in <i>crls</i> . They will be automatically initialized. </p>
<p> If the Certificate is PEM encoded it should have a header of &quot;X509 CRL&quot;.</p>
<h2>RETURNS</h2>
<p> the number of certificates read or a negative error value.</p>
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
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></p>
<dd> </code></dl>
<h2>Index</h2>
