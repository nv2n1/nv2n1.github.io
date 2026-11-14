---
title: "gnutls_x509_crt_get_subject_alt_othername_oid(3)"
name: "gnutls_x509_crt_get_subject_alt_othername_oid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_subject_alt_othername_oid/"
description: "gnutls_x509_crt_get_subject_alt_othername_oid – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_subject_alt_othername_oid &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_subject_alt_othername_oid(gnutls_x509_crt_t </code><i>cert</i><code>, unsigned int </code><i>seq</i><code>, void * </code><i>oid</i><code>, size_t * </code><i>oid_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</p>
<dt>unsigned int seq</p>
<dd> specifies the sequence number of the alt name (0 for the first one, 1 for the second etc.)</p>
<dt>void * oid</p>
<dd> is the place where the otherName OID will be copied to</p>
<dt>size_t * oid_size</p>
<dd> holds the size of ret.</dl>
<h2>DESCRIPTION</h2>
<p> This function will extract the type OID of an otherName Subject Alternative Name, contained in the given certificate, and return the type as an enumerated element. </p>
<p> This function is only useful if <code>gnutls_x509_crt_get_subject_alt_name()</code> returned <code>GNUTLS_SAN_OTHERNAME</code>. </p>
<p> If <i>oid</i> is null then only the size will be filled. The <i>oid</i> returned will be null terminated, although <i>oid_size</i> will not account for the trailing null.</p>
<h2>RETURNS</h2>
<p> the alternative subject name type on success, one of the enumerated gnutls_x509_subject_alt_name_t. For supported OIDs, it will return one of the virtual (GNUTLS_SAN_OTHERNAME_*) types, e.g. <code>GNUTLS_SAN_OTHERNAME_XMPP</code>, and <code>GNUTLS_SAN_OTHERNAME</code> for unknown OIDs. It will return <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> if<br />
&nbsp;<wbr><i>ian_size</i>&nbsp;<wbr>is not large enough to hold the value.&nbsp;<wbr>&nbsp;<wbr>In that case<br />
&nbsp;<wbr><i>ian_size</i>&nbsp;<wbr>will be updated with the required size.&nbsp;<wbr>&nbsp;<wbr>If the certificate does not have an Alternative name with the specified sequence number and with the otherName type then <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> is returned.</p>
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
