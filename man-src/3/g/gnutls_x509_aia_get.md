---
title: "gnutls_x509_aia_get(3)"
name: "gnutls_x509_aia_get"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_aia_get/"
description: "gnutls_x509_aia_get – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_aia_get &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_x509_aia_get(gnutls_x509_aia_t </code><i>aia</i><code>, unsigned int </code><i>seq</i><code>, gnutls_datum_t * </code><i>oid</i><code>, unsigned * </code><i>san_type</i><code>, gnutls_datum_t * </code><i>san</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_aia_t aia</p>
<dd> The authority info access structure</p>
<dt>unsigned int seq</p>
<dd> specifies the sequence number of the access descriptor (0 for the first one, 1 for the second etc.)</p>
<dt>gnutls_datum_t * oid</p>
<dd> the type of available data; to be treated as constant.</p>
<dt>unsigned * san_type</p>
<dd> Will hold the type of the name of <code>gnutls_subject_alt_names_t</code> (may be null).</p>
<dt>gnutls_datum_t * san</p>
<dd> the access location name; to be treated as constant (may be null).</dl>
<h2>DESCRIPTION</h2>
<p> This function reads from the Authority Information Access structure. </p>
<p> The <i>seq</i> input parameter is used to indicate which member of the sequence the caller is interested in. The first member is 0, the second member 1 and so on. When the <i>seq</i> value is out of bounds, <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> is returned. </p>
<p> Typically <i>oid</i> is <code>GNUTLS_OID_AD_CAISSUERS</code> or <code>GNUTLS_OID_AD_OCSP</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.3.0</p>
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
