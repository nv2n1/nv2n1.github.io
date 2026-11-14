---
title: "gnutls_transport_set_errno(3)"
name: "gnutls_transport_set_errno"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_transport_set_errno/"
description: "gnutls_transport_set_errno – API function"
---

<h2>NAME</h2>
<p> gnutls_transport_set_errno &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_transport_set_errno(gnutls_session_t </code><i>session</i><code>, int </code><i>err</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>int err</p>
<dd> error value to store in session-specific errno variable.</dl>
<h2>DESCRIPTION</h2>
<p> Store <i>err</i> in the session-specific errno variable. Useful values for <i>err</i> are EINTR, EAGAIN and EMSGSIZE, other values are treated will be treated as real errors in the push/pull function. </p>
<p> This function is useful in replacement push and pull functions set by <code>gnutls_transport_set_push_function()</code> and <code>gnutls_transport_set_pull_function()</code> under Windows, where the replacements may not have access to the same <i>errno</i> variable that is used by GnuTLS (e.g., the application is linked to msvcr71.dll and gnutls is linked to msvcrt.dll).</p>
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
