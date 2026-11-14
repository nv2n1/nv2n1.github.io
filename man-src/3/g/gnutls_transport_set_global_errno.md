---
title: "gnutls_transport_set_global_errno(3)"
name: "gnutls_transport_set_global_errno"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_transport_set_global_errno/"
description: "gnutls_transport_set_global_errno – API function"
---

<h2>NAME</h2>
<p> gnutls_transport_set_global_errno &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>void gnutls_transport_set_global_errno(int </code><i>err</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>int err</p>
<dd> error value to store in global errno variable.</dl>
<h2>DESCRIPTION</h2>
<p> Store <i>err</i> in the global errno variable. Useful values for <i>err</i> is EAGAIN and EINTR, other values are treated will be treated as real errors in the push/pull function. </p>
<p> This function is useful in replacement push/pull functions set by gnutls_transport_set_push_function and gnutls_transport_set_pullpush_function under Windows, where the replacement push/pull may not have access to the same <i>errno</i> variable that is used by GnuTLS (e.g., the application is linked to msvcr71.dll and gnutls is linked to msvcrt.dll). </p>
<p> Whether this function is thread safe or not depends on whether the global variable errno is thread safe, some system libraries make it a thread-local variable. When feasible, using the guaranteed thread-safe <code>gnutls_transport_set_errno()</code> may be better.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnutls [at] gnu.org&gt;. GnuTLS home page: <a rel="nofollow" href="http://www.gnu.org/software/gnutls/">http://www.gnu.org/software/gnutls/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Free Software Foundation.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gnutls</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gnutls</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
