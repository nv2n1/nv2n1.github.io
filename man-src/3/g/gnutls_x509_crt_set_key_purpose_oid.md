---
title: "gnutls_x509_crt_set_key_purpose_oid(3)"
name: "gnutls_x509_crt_set_key_purpose_oid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_set_key_purpose_oid/"
description: "gnutls_x509_crt_set_key_purpose_oid – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_set_key_purpose_oid &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_set_key_purpose_oid(gnutls_x509_crt_t </code><i>cert</i><code>, const void * </code><i>oid</i><code>, unsigned int </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> a certificate of type <code>gnutls_x509_crt_t</code></p>
<dt>const void * oid</p>
<dd> a pointer to a null terminated string that holds the OID</p>
<dt>unsigned int critical</p>
<dd> Whether this extension will be critical or not</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the key purpose OIDs of the Certificate. These are stored in the Extended Key Usage extension (2.5.29.37) See the GNUTLS_KP_* definitions for human readable names. </p>
<p> Subsequent calls to this function will append OIDs to the OID list.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
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
