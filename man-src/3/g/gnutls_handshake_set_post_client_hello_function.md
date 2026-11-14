---
title: "gnutls_handshake_set_post_client_hello_function(3)"
name: "gnutls_handshake_set_post_client_hello_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_handshake_set_post_client_hello_function/"
description: "gnutls_handshake_set_post_client_hello_function – API function"
---

<h2>NAME</h2>
<p> gnutls_handshake_set_post_client_hello_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_handshake_set_post_client_hello_function(gnutls_session_t </code><i>session</i><code>, gnutls_handshake_post_client_hello_func </code><i>func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_handshake_post_client_hello_func func</p>
<dd> is the function to be called</dl>
<h2>DESCRIPTION</h2>
<p> This function will set a callback to be called after the client hello has been received (callback valid in server side only). This allows the server to adjust settings based on received extensions. </p>
<p> Those settings could be ciphersuites, requesting certificate, or anything else except for version negotiation (this is done before the hello message is parsed). </p>
<p> This callback must return 0 on success or a gnutls error code to terminate the handshake. </p>
<p> Since GnuTLS 3.3.5 the callback is allowed to return <code>GNUTLS_E_AGAIN</code> or <code>GNUTLS_E_INTERRUPTED</code> to put the handshake on hold. In that case <code>gnutls_handshake()</code> will return <code>GNUTLS_E_INTERRUPTED</code> and can be resumed when needed.</p>
<h2>WARNING</h2>
<p> You should not use this function to terminate the handshake based on client input unless you know what you are doing. Before the handshake is finished there is no way to know if there is a man-in-the-middle attack being performed.</p>
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
