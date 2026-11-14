---
title: "gnutls_x509_crt_get_extension_data2(3)"
name: "gnutls_x509_crt_get_extension_data2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_extension_data2/"
description: "gnutls_x509_crt_get_extension_data2 – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_extension_data2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_extension_data2(gnutls_x509_crt_t </code><i>cert</i><code>, unsigned </code><i>indx</i><code>, gnutls_datum_t * </code><i>data</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</p>
<dt>unsigned indx</p>
<dd> Specifies which extension OID to read. Use (0) to get the first one.</p>
<dt>gnutls_datum_t * data</p>
<dd> will contain the extension DER-encoded data</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the requested by the index extension data in the certificate. The extension data will be allocated using <code>gnutls_malloc()</code>. </p>
<p> Use <code>gnutls_x509_crt_get_extension_info()</code> to extract the OID.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned. If you have reached the last extension available <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> will be returned.</p>
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
