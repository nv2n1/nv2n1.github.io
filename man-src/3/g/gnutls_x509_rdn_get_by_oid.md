---
title: "gnutls_x509_rdn_get_by_oid(3)"
name: "gnutls_x509_rdn_get_by_oid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_rdn_get_by_oid/"
description: "gnutls_x509_rdn_get_by_oid – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_rdn_get_by_oid &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_rdn_get_by_oid(const gnutls_datum_t * </code><i>idn</i><code>, const char * </code><i>oid</i><code>, int </code><i>indx</i><code>, unsigned int </code><i>raw_flag</i><code>, void * </code><i>buf</i><code>, size_t * </code><i>buf_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const gnutls_datum_t * idn</p>
<dd> should contain a DER encoded RDN sequence</p>
<dt>const char * oid</p>
<dd> an Object Identifier</p>
<dt>int indx</p>
<dd> In case multiple same OIDs exist in the RDN indicates which to send. Use 0 for the first one.</p>
<dt>unsigned int raw_flag</p>
<dd> If non-zero then the raw DER data are returned.</p>
<dt>void * buf</p>
<dd> a pointer to a structure to hold the peer&#8217;s name</p>
<dt>size_t * buf_size</p>
<dd> holds the size of <i>buf</i></dl>
<h2>DESCRIPTION</h2>
<p> This function will return the name of the given Object identifier, of the RDN sequence. The name will be encoded using the rules from RFC4514.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, or <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> is returned and * <i>buf_size</i> is updated if the provided buffer is not long enough, otherwise a negative error value.</p>
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
