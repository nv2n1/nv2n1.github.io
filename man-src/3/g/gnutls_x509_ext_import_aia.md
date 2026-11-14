---
title: "gnutls_x509_ext_import_aia(3)"
name: "gnutls_x509_ext_import_aia"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_ext_import_aia/"
description: "gnutls_x509_ext_import_aia – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_ext_import_aia &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_x509_ext_import_aia(const gnutls_datum_t * </code><i>ext</i><code>, gnutls_x509_aia_t </code><i>aia</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const gnutls_datum_t * ext</p>
<dd> The DER-encoded extension data</p>
<dt>gnutls_x509_aia_t aia</p>
<dd> The authority info access structure</p>
<dt>unsigned int flags</p>
<dd> should be zero</dl>
<h2>DESCRIPTION</h2>
<p> This function extracts the Authority Information Access (AIA) extension from the provided DER-encoded data; see RFC 5280 section 4.2.2.1 for more information on the extension. The AIA extension holds a sequence of AccessDescription (AD) data.</p>
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
