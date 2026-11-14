---
title: "gnutls_alpn_set_protocols(3)"
name: "gnutls_alpn_set_protocols"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_alpn_set_protocols/"
description: "gnutls_alpn_set_protocols – API function"
---

<h2>NAME</h2>
<p> gnutls_alpn_set_protocols &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_alpn_set_protocols(gnutls_session_t </code><i>session</i><code>, const gnutls_datum_t * </code><i>protocols</i><code>, unsigned </code><i>protocols_size</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const gnutls_datum_t * protocols</p>
<dd> is the protocol names to add.</p>
<dt>unsigned protocols_size</p>
<dd> the number of protocols to add.</p>
<dt>unsigned int flags</p>
<dd> zero or <code>GNUTLS_ALPN_</code>*</dl>
<h2>DESCRIPTION</h2>
<p> This function is to be used by both clients and servers, to declare the supported ALPN protocols, which are used during negotiation with peer. </p>
<p> If <code>GNUTLS_ALPN_MAND</code> is specified the connection will be aborted if no matching ALPN protocol is found.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned. </p>
<p> Since 3.2.0</p>
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
