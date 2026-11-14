---
title: "gnutls_x509_crt_list_import(3)"
name: "gnutls_x509_crt_list_import"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_list_import/"
description: "gnutls_x509_crt_list_import – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_list_import &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_list_import(gnutls_x509_crt_t * </code><i>certs</i><code>, unsigned int * </code><i>cert_max</i><code>, const gnutls_datum_t * </code><i>data</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t * certs</p>
<dd> The structures to store the parsed certificate. Must not be initialized.</p>
<dt>unsigned int * cert_max</p>
<dd> Initially must hold the maximum number of certs. It will be updated with the number of certs available.</p>
<dt>const gnutls_datum_t * data</p>
<dd> The PEM encoded certificate.</p>
<dt>gnutls_x509_crt_fmt_t format</p>
<dd> One of DER or PEM.</p>
<dt>unsigned int flags</p>
<dd> must be (0) or an OR&#8217;d sequence of gnutls_certificate_import_flags.</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the given PEM encoded certificate list to the native gnutls_x509_crt_t format. The output will be stored in <i>certs</i> . They will be automatically initialized. </p>
<p> The flag <code>GNUTLS_X509_CRT_LIST_IMPORT_FAIL_IF_EXCEED</code> will cause import to fail if the certificates in the provided buffer are more than the available structures. The <code>GNUTLS_X509_CRT_LIST_FAIL_IF_UNSORTED</code> flag will cause the function to fail if the provided list is not sorted from subject to issuer. </p>
<p> If the Certificate is PEM encoded it should have a header of &quot;X509 CERTIFICATE&quot;, or &quot;CERTIFICATE&quot;.</p>
<h2>RETURNS</h2>
<p> the number of certificates read or a negative error value.</p>
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
