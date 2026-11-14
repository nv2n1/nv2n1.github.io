---
title: "gnutls_session_set_data(3)"
name: "gnutls_session_set_data"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_session_set_data/"
description: "gnutls_session_set_data – API function"
---

<h2>NAME</h2>
<p> gnutls_session_set_data &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_session_set_data(gnutls_session_t </code><i>session</i><code>, const void * </code><i>session_data</i><code>, size_t </code><i>session_data_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const void * session_data</p>
<dd> is a pointer to space to hold the session.</p>
<dt>size_t session_data_size</p>
<dd> is the session&#8217;s size</dl>
<h2>DESCRIPTION</h2>
<p> Sets all session parameters, in order to resume a previously established session. The session data given must be the one returned by <code>gnutls_session_get_data()</code>. This function should be called before <code>gnutls_handshake()</code>. </p>
<p> Keep in mind that session resuming is advisory. The server may choose not to resume the session, thus a full handshake will be performed.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise an error code is returned.</p>
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
