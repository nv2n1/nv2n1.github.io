---
title: "gnutls_ocsp_resp_get_responder(3)"
name: "gnutls_ocsp_resp_get_responder"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_resp_get_responder/"
description: "gnutls_ocsp_resp_get_responder – API function"
---

<h2>NAME</h2>
<p> gnutls_ocsp_resp_get_responder &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_resp_get_responder(gnutls_ocsp_resp_t </code><i>resp</i><code>, gnutls_datum_t * </code><i>dn</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_resp_t resp</p>
<dd> should contain a <code>gnutls_ocsp_resp_t</code> structure</p>
<dt>gnutls_datum_t * dn</p>
<dd> newly allocated buffer with name</dl>
<h2>DESCRIPTION</h2>
<p> This function will extract the name of the Basic OCSP Response in the provided buffer. The name will be in the form &quot;C=xxxx,O=yyyy,CN=zzzz&quot; as described in RFC2253. The output string will be ASCII or UTF-8 encoded, depending on the certificate data. </p>
<p> The caller needs to deallocate memory by calling <code>gnutls_free()</code> on<br />
&nbsp;<wbr><i>dn</i>&nbsp;<wbr>-&gt;data.</p>
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
