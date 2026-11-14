---
title: "gnutls_x509_crq_get_dn_oid(3)"
name: "gnutls_x509_crq_get_dn_oid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_get_dn_oid/"
description: "gnutls_x509_crq_get_dn_oid – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_get_dn_oid &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_get_dn_oid(gnutls_x509_crq_t </code><i>crq</i><code>, int </code><i>indx</i><code>, void * </code><i>oid</i><code>, size_t * </code><i>sizeof_oid</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> should contain a gnutls_x509_crq_t structure</p>
<dt>int indx</p>
<dd> Specifies which DN OID to get. Use (0) to get the first one.</p>
<dt>void * oid</p>
<dd> a pointer to a structure to hold the name (may be <code>NULL</code>)</p>
<dt>size_t * sizeof_oid</p>
<dd> initially holds the size of <i>oid</i></dl>
<h2>DESCRIPTION</h2>
<p> This function will extract the requested OID of the name of the certificate request subject, specified by the given index.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> if the provided buffer is not long enough, and in that case the * <i>sizeof_oid</i> will be updated with the required size. On success 0 is returned.</p>
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
