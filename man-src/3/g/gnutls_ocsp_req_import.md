---
title: "gnutls_ocsp_req_import(3)"
name: "gnutls_ocsp_req_import"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_req_import/"
description: "gnutls_ocsp_req_import – API function"
---

<h2>NAME</h2>
<p> gnutls_ocsp_req_import &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_req_import(gnutls_ocsp_req_t </code><i>req</i><code>, const gnutls_datum_t * </code><i>data</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_req_t req</p>
<dd> The structure to store the parsed request.</p>
<dt>const gnutls_datum_t * data</p>
<dd> DER encoded OCSP request.</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the given DER encoded OCSP request to the native <code>gnutls_ocsp_req_t</code> format. The output will be stored in<br />
&nbsp;<wbr><i>req</i>&nbsp;<wbr>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
