---
title: "gnutls_x509_crl_get_extension_data(3)"
name: "gnutls_x509_crl_get_extension_data"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_get_extension_data/"
description: "gnutls_x509_crl_get_extension_data – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_get_extension_data &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_get_extension_data(gnutls_x509_crl_t </code><i>crl</i><code>, int </code><i>indx</i><code>, void * </code><i>data</i><code>, size_t * </code><i>sizeof_data</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_t crl</p>
<dd> should contain a <code>gnutls_x509_crl_t</code> structure</p>
<dt>int indx</p>
<dd> Specifies which extension OID to send. Use (0) to get the first one.</p>
<dt>void * data</p>
<dd> a pointer to a structure to hold the data (may be null)</p>
<dt>size_t * sizeof_data</p>
<dd> initially holds the size of <i>oid</i></dl>
<h2>DESCRIPTION</h2>
<p> This function will return the requested extension data in the CRL. The extension data will be stored as a string in the provided buffer. </p>
<p> Use <code>gnutls_x509_crl_get_extension_info()</code> to extract the OID and critical flag. Use <code>gnutls_x509_crl_get_extension_info()</code> instead, if you want to get data indexed by the extension OID rather than sequence.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code in case of an error. If your have reached the last extension available <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> will be returned.</p>
<h2>SINCE</h2>
<p> 2.8.0</p>
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
