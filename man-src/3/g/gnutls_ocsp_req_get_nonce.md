---
title: "gnutls_ocsp_req_get_nonce(3)"
name: "gnutls_ocsp_req_get_nonce"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_req_get_nonce/"
description: "gnutls_ocsp_req_get_nonce – API function"
---

<h2>NAME</h2>
<p> gnutls_ocsp_req_get_nonce &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_req_get_nonce(gnutls_ocsp_req_t </code><i>req</i><code>, unsigned int * </code><i>critical</i><code>, gnutls_datum_t * </code><i>nonce</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_req_t req</p>
<dd> should contain a <code>gnutls_ocsp_req_t</code> structure</p>
<dt>unsigned int * critical</p>
<dd> whether nonce extension is marked critical, or NULL</p>
<dt>gnutls_datum_t * nonce</p>
<dd> will hold newly allocated buffer with nonce data</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the OCSP request nonce extension data. </p>
<p> The caller needs to deallocate memory by calling <code>gnutls_free()</code> on<br />
&nbsp;<wbr><i>nonce</i>&nbsp;<wbr>-&gt;data.</p>
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
