---
title: "gnutls_certificate_server_set_request(3)"
name: "gnutls_certificate_server_set_request"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_server_set_request/"
description: "gnutls_certificate_server_set_request – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_server_set_request &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_certificate_server_set_request(gnutls_session_t </code><i>session</i><code>, gnutls_certificate_request_t </code><i>req</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_certificate_request_t req</p>
<dd> is one of GNUTLS_CERT_REQUEST, GNUTLS_CERT_REQUIRE</dl>
<h2>DESCRIPTION</h2>
<p> This function specifies if we (in case of a server) are going to send a certificate request message to the client. If <i>req</i> is GNUTLS_CERT_REQUIRE then the server will return an error if the peer does not provide a certificate. If you do not call this function then the client will not be asked to send a certificate.</p>
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
