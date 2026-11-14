---
title: "gnutls_x509_crq_get_dn2(3)"
name: "gnutls_x509_crq_get_dn2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_get_dn2/"
description: "gnutls_x509_crq_get_dn2 – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_get_dn2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_get_dn2(gnutls_x509_crq_t </code><i>crq</i><code>, gnutls_datum_t * </code><i>dn</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> should contain a <code>gnutls_x509_crq_t</code> structure</p>
<dt>gnutls_datum_t * dn</p>
<dd> a pointer to a structure to hold the name</dl>
<h2>DESCRIPTION</h2>
<p> This function will allocate buffer and copy the name of the Certificate request. The name will be in the form &quot;C=xxxx,O=yyyy,CN=zzzz&quot; as described in RFC4514. The output string will be ASCII or UTF-8 encoded, depending on the certificate data.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value. and a negative error code on error.</p>
<h2>SINCE</h2>
<p> 3.1.10</p>
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
