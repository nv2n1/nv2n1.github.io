---
title: "gnutls_ocsp_status_request_is_checked(3)"
name: "gnutls_ocsp_status_request_is_checked"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_status_request_is_checked/"
description: "gnutls_ocsp_status_request_is_checked – API function"
---

<h2>NAME</h2>
<p> gnutls_ocsp_status_request_is_checked &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_status_request_is_checked(gnutls_session_t </code><i>session</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a gnutls session</p>
<dt>unsigned int flags</p>
<dd> should be zero</dl>
<h2>DESCRIPTION</h2>
<p> Check whether an OCSP status response was included in the handshake and whether it was checked and valid (not too old or superseded). This is a helper function when needing to decide whether to perform an OCSP validity check on the peer&#8217;s certificate. Must be called after <code>gnutls_certificate_verify_peers3()</code> is called.</p>
<h2>RETURNS</h2>
<p> non zero it was valid, or a zero if it wasn&#8217;t sent, or sent and was invalid.</p>
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
