---
title: "gnutls_x509_crt_get_subject(3)"
name: "gnutls_x509_crt_get_subject"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_subject/"
description: "gnutls_x509_crt_get_subject – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_subject &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_subject(gnutls_x509_crt_t </code><i>cert</i><code>, gnutls_x509_dn_t * </code><i>dn</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</p>
<dt>gnutls_x509_dn_t * dn</p>
<dd> output variable with pointer to uint8_t DN.</dl>
<h2>DESCRIPTION</h2>
<p> Return the Certificate&#8217;s Subject DN as a <code>gnutls_x509_dn_t</code> data type, that can be decoded using <code>gnutls_x509_dn_get_rdn_ava()</code>. </p>
<p> Note that <i>dn</i> should be treated as constant. Because it points into the <i>cert</i> object, you should not use <i>dn</i> after <i>cert</i> is deallocated.</p>
<h2>RETURNS</h2>
<p> Returns 0 on success, or an error code.</p>
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
