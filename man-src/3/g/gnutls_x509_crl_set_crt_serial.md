---
title: "gnutls_x509_crl_set_crt_serial(3)"
name: "gnutls_x509_crl_set_crt_serial"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_set_crt_serial/"
description: "gnutls_x509_crl_set_crt_serial – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_set_crt_serial &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_set_crt_serial(gnutls_x509_crl_t </code><i>crl</i><code>, const void * </code><i>serial</i><code>, size_t </code><i>serial_size</i><code>, time_t </code><i>revocation_time</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_t crl</p>
<dd> should contain a gnutls_x509_crl_t structure</p>
<dt>const void * serial</p>
<dd> The revoked certificate&#8217;s serial number</p>
<dt>size_t serial_size</p>
<dd> Holds the size of the serial field.</p>
<dt>time_t revocation_time</p>
<dd> The time this certificate was revoked</dl>
<h2>DESCRIPTION</h2>
<p> This function will set a revoked certificate&#8217;s serial number to the CRL.</p>
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
