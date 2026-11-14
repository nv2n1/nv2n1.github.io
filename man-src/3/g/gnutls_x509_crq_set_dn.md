---
title: "gnutls_x509_crq_set_dn(3)"
name: "gnutls_x509_crq_set_dn"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_set_dn/"
description: "gnutls_x509_crq_set_dn – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_set_dn &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_set_dn(gnutls_x509_crq_t </code><i>crq</i><code>, const char * </code><i>dn</i><code>, const char ** </code><i>err</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> a certificate of type <code>gnutls_x509_crq_t</code></p>
<dt>const char * dn</p>
<dd> a comma separated DN string (RFC4514)</p>
<dt>const char ** err</p>
<dd> indicates the error position (if any)</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the DN on the provided certificate. The input string should be plain ASCII or UTF-8 encoded.</p>
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
