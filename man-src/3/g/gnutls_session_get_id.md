---
title: "gnutls_session_get_id(3)"
name: "gnutls_session_get_id"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_session_get_id/"
description: "gnutls_session_get_id – API function"
---

<h2>NAME</h2>
<p> gnutls_session_get_id &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_session_get_id(gnutls_session_t </code><i>session</i><code>, void * </code><i>session_id</i><code>, size_t * </code><i>session_id_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>void * session_id</p>
<dd> is a pointer to space to hold the session id.</p>
<dt>size_t * session_id_size</p>
<dd> initially should contain the maximum <i>session_id</i> size and will be updated.</dl>
<h2>DESCRIPTION</h2>
<p> Returns the current session ID. This can be used if you want to check if the next session you tried to resume was actually resumed. That is because resumed sessions share the same session ID with the original session. </p>
<p> The session ID is selected by the server, that identify the current session. In TLS 1.0 and SSL 3.0 session id is always less than 32 bytes.</p>
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
