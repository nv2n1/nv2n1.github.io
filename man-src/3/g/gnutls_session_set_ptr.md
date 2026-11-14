---
title: "gnutls_session_set_ptr(3)"
name: "gnutls_session_set_ptr"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_session_set_ptr/"
description: "gnutls_session_set_ptr – API function"
---

<h2>NAME</h2>
<p> gnutls_session_set_ptr &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_session_set_ptr(gnutls_session_t </code><i>session</i><code>, void * </code><i>ptr</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>void * ptr</p>
<dd> is the user pointer</dl>
<h2>DESCRIPTION</h2>
<p> This function will set (associate) the user given pointer <i>ptr</i> to the session structure. This pointer can be accessed with <code>gnutls_session_get_ptr()</code>.</p>
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
