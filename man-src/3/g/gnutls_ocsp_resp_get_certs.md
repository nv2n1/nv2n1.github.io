---
title: "gnutls_ocsp_resp_get_certs(3)"
name: "gnutls_ocsp_resp_get_certs"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_resp_get_certs/"
description: "gnutls_ocsp_resp_get_certs – API function"
---

<h2>NAME</h2>
<p> gnutls_ocsp_resp_get_certs &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_resp_get_certs(gnutls_ocsp_resp_t </code><i>resp</i><code>, gnutls_x509_crt_t ** </code><i>certs</i><code>, size_t * </code><i>ncerts</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_resp_t resp</p>
<dd> should contain a <code>gnutls_ocsp_resp_t</code> structure</p>
<dt>gnutls_x509_crt_t ** certs</p>
<dd> newly allocated array with <code>gnutls_x509_crt_t</code> certificates</p>
<dt>size_t * ncerts</p>
<dd> output variable with number of allocated certs.</dl>
<h2>DESCRIPTION</h2>
<p> This function will extract the X.509 certificates found in the Basic OCSP Response. The <i>certs</i> output variable will hold a newly allocated zero-terminated array with X.509 certificates. </p>
<p> Every certificate in the array needs to be de-allocated with <code>gnutls_x509_crt_deinit()</code> and the array itself must be freed using <code>gnutls_free()</code>. </p>
<p> Both the <i>certs</i> and <i>ncerts</i> variables may be NULL. Then the function will work as normal but will not return the NULL:d information. This can be used to get the number of certificates only, or to just get the certificate array without its size.</p>
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
