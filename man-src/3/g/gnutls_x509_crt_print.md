---
title: "gnutls_x509_crt_print(3)"
name: "gnutls_x509_crt_print"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_print/"
description: "gnutls_x509_crt_print – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_print &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_print(gnutls_x509_crt_t </code><i>cert</i><code>, gnutls_certificate_print_formats_t </code><i>format</i><code>, gnutls_datum_t * </code><i>out</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> The structure to be printed</p>
<dt>gnutls_certificate_print_formats_t format</p>
<dd> Indicate the format to use</p>
<dt>gnutls_datum_t * out</p>
<dd> Newly allocated datum with null terminated string.</dl>
<h2>DESCRIPTION</h2>
<p> This function will pretty print a X.509 certificate, suitable for display to a human. </p>
<p> If the format is <code>GNUTLS_CRT_PRINT_FULL</code> then all fields of the certificate will be output, on multiple lines. The <code>GNUTLS_CRT_PRINT_ONELINE</code> format will generate one line with some selected fields, which is useful for logging purposes. </p>
<p> The output <i>out</i> needs to be deallocated using <code>gnutls_free()</code>.</p>
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
