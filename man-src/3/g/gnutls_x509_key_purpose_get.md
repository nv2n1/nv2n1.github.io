---
title: "gnutls_x509_key_purpose_get(3)"
name: "gnutls_x509_key_purpose_get"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_key_purpose_get/"
description: "gnutls_x509_key_purpose_get – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_key_purpose_get &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_x509_key_purpose_get(gnutls_x509_key_purposes_t </code><i>p</i><code>, unsigned </code><i>idx</i><code>, gnutls_datum_t * </code><i>oid</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_key_purposes_t p</p>
<dd> The key purposes structure</p>
<dt>unsigned idx</p>
<dd> The index of the key purpose to retrieve</p>
<dt>gnutls_datum_t * oid</p>
<dd> Will hold the object identifier of the key purpose (to be treated as constant)</dl>
<h2>DESCRIPTION</h2>
<p> This function will retrieve the specified by the index key purpose in the purposes structure. The object identifier will be a null terminated string.</p>
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
