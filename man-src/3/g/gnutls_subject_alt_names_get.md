---
title: "gnutls_subject_alt_names_get(3)"
name: "gnutls_subject_alt_names_get"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_subject_alt_names_get/"
description: "gnutls_subject_alt_names_get – API function"
---

<h2>NAME</h2>
<p> gnutls_subject_alt_names_get &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_subject_alt_names_get(gnutls_subject_alt_names_t </code><i>sans</i><code>, unsigned int </code><i>seq</i><code>, unsigned int * </code><i>san_type</i><code>, gnutls_datum_t * </code><i>san</i><code>, gnutls_datum_t * </code><i>othername_oid</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_subject_alt_names_t sans</p>
<dd> The alternative names structure</p>
<dt>unsigned int seq</p>
<dd> The index of the name to get</p>
<dt>unsigned int * san_type</p>
<dd> Will hold the type of the name (of <code>gnutls_subject_alt_names_t</code>)</p>
<dt>gnutls_datum_t * san</p>
<dd> The alternative name data (should be treated as constant)</p>
<dt>gnutls_datum_t * othername_oid</p>
<dd> The object identifier if <i>san_type</i> is <code>GNUTLS_SAN_OTHERNAME</code> (should be treated as constant)</dl>
<h2>DESCRIPTION</h2>
<p> This function will return a specific alternative name as stored in the <i>sans</i> structure. The returned values should be treated as constant and valid for the lifetime of <i>sans</i> .</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> if the index is out of bounds, otherwise a negative error value.</p>
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
