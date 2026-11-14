---
title: "gnutls_x509_crl_iter_crt_serial(3)"
name: "gnutls_x509_crl_iter_crt_serial"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_iter_crt_serial/"
description: "gnutls_x509_crl_iter_crt_serial – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_iter_crt_serial &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_iter_crt_serial(gnutls_x509_crl_t </code><i>crl</i><code>, gnutls_x509_crl_iter_t * </code><i>iter</i><code>, unsigned char * </code><i>serial</i><code>, size_t * </code><i>serial_size</i><code>, time_t * </code><i>t</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_t crl</p>
<dd> should contain a <code>gnutls_x509_crl_t</code> structure</p>
<dt>gnutls_x509_crl_iter_t * iter</p>
<dd> A pointer to an iterator (initially the iterator should be <code>NULL</code>)</p>
<dt>unsigned char * serial</p>
<dd> where the serial number will be copied</p>
<dt>size_t * serial_size</p>
<dd> initially holds the size of serial</p>
<dt>time_t * t</p>
<dd> if non null, will hold the time this certificate was revoked</dl>
<h2>DESCRIPTION</h2>
<p> This function performs the same as <code>gnutls_x509_crl_get_crt_serial()</code>, but reads sequentially and keeps state in the iterator between calls. That allows it to provide better performance in sequences with many elements (50000+). </p>
<p> When past the last element is accessed <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> is returned and the iterator is reset. </p>
<p> After use, the iterator must be deinitialized using <code>gnutls_x509_crl_iter_deinit()</code>.</p>
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
