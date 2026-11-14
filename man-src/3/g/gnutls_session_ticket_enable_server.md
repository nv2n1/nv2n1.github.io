---
title: "gnutls_session_ticket_enable_server(3)"
name: "gnutls_session_ticket_enable_server"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_session_ticket_enable_server/"
description: "gnutls_session_ticket_enable_server – API function"
---

<h2>NAME</h2>
<p> gnutls_session_ticket_enable_server &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_session_ticket_enable_server(gnutls_session_t </code><i>session</i><code>, const gnutls_datum_t * </code><i>key</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const gnutls_datum_t * key</p>
<dd> key to encrypt session parameters.</dl>
<h2>DESCRIPTION</h2>
<p> Request that the server should attempt session resumption using SessionTicket. <i>key</i> must be initialized with <code>gnutls_session_ticket_key_generate()</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, or an error code.</p>
<h2>SINCE</h2>
<p> 2.10.0</p>
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
