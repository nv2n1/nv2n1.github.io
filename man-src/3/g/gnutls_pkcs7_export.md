---
title: "gnutls_pkcs7_export(3)"
name: "gnutls_pkcs7_export"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs7_export/"
description: "gnutls_pkcs7_export – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs7_export &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_pkcs7_export(gnutls_pkcs7_t </code><i>pkcs7</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>, void * </code><i>output_data</i><code>, size_t * </code><i>output_data_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs7_t pkcs7</p>
<dd> Holds the pkcs7 structure</p>
<dt>gnutls_x509_crt_fmt_t format</p>
<dd> the format of output params. One of PEM or DER.</p>
<dt>void * output_data</p>
<dd> will contain a structure PEM or DER encoded</p>
<dt>size_t * output_data_size</p>
<dd> holds the size of output_data (and will be replaced by the actual size of parameters)</dl>
<h2>DESCRIPTION</h2>
<p> This function will export the pkcs7 structure to DER or PEM format. </p>
<p> If the buffer provided is not long enough to hold the output, then * <i>output_data_size</i> is updated and <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> will be returned. </p>
<p> If the structure is PEM encoded, it will have a header of &quot;BEGIN PKCS7&quot;.</p>
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
