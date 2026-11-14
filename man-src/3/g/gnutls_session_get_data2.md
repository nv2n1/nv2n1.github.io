---
title: "gnutls_session_get_data2(3)"
name: "gnutls_session_get_data2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_session_get_data2/"
description: "gnutls_session_get_data2 – API function"
---

<h2>NAME</h2>
<p> gnutls_session_get_data2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_session_get_data2(gnutls_session_t </code><i>session</i><code>, gnutls_datum_t * </code><i>data</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_datum_t * data</p>
<dd> is a pointer to a datum that will hold the session.</dl>
<h2>DESCRIPTION</h2>
<p> Returns all session parameters needed to be stored to support resumption. The client should call this, and store the returned session data. A session may be resumed later by calling <code>gnutls_session_set_data()</code>. This function must be called after a successful (full) handshake. It should not be used in resumed sessions &#8211;see <code>gnutls_session_is_resumed()</code>. </p>
<p> The returned <i>data</i> are allocated and must be released using <code>gnutls_free()</code>.</p>
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
