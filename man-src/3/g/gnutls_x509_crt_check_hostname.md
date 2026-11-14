---
title: "gnutls_x509_crt_check_hostname(3)"
name: "gnutls_x509_crt_check_hostname"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_check_hostname/"
description: "gnutls_x509_crt_check_hostname – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_check_hostname &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_check_hostname(gnutls_x509_crt_t </code><i>cert</i><code>, const char * </code><i>hostname</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> should contain an gnutls_x509_crt_t structure</p>
<dt>const char * hostname</p>
<dd> A null terminated string that contains a DNS name</dl>
<h2>DESCRIPTION</h2>
<p> This function will check if the given certificate&#8217;s subject matches the given hostname. This is a basic implementation of the matching described in RFC6125, and takes into account wildcards, and the DNSName/IPAddress subject alternative name PKIX extension. </p>
<p> For details see also <code>gnutls_x509_crt_check_hostname2()</code>.</p>
<h2>RETURNS</h2>
<p> non-zero for a successful match, and zero on failure.</p>
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
