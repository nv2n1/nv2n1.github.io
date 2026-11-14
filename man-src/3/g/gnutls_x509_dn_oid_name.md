---
title: "gnutls_x509_dn_oid_name(3)"
name: "gnutls_x509_dn_oid_name"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_dn_oid_name/"
description: "gnutls_x509_dn_oid_name – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_dn_oid_name &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>const char * gnutls_x509_dn_oid_name(const char * </code><i>oid</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * oid</p>
<dd> holds an Object Identifier in a null terminated string</p>
<dt>unsigned int flags</p>
<dd> 0 or GNUTLS_X509_DN_OID_*</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the name of a known DN OID. If <code>GNUTLS_X509_DN_OID_RETURN_OID</code> is specified this function will return the given OID if no descriptive name has been found.</p>
<h2>RETURNS</h2>
<p> A null terminated string or NULL otherwise.</p>
<h2>SINCE</h2>
<p> 3.0</p>
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
