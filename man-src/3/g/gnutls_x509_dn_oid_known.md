---
title: "gnutls_x509_dn_oid_known(3)"
name: "gnutls_x509_dn_oid_known"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_dn_oid_known/"
description: "gnutls_x509_dn_oid_known – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_dn_oid_known &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_dn_oid_known(const char * </code><i>oid</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * oid</p>
<dd> holds an Object Identifier in a null terminated string</dl>
<h2>DESCRIPTION</h2>
<p> This function will inform about known DN OIDs. This is useful since functions like <code>gnutls_x509_crt_set_dn_by_oid()</code> use the information on known OIDs to properly encode their input. Object Identifiers that are not known are not encoded by these functions, and their input is stored directly into the ASN.1 structure. In that case of unknown OIDs, you have the responsibility of DER encoding your data.</p>
<h2>RETURNS</h2>
<p> 1 on known OIDs and 0 otherwise.</p>
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
