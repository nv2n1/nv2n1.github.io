---
title: "gnutls_malloc(3)"
name: "gnutls_malloc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_malloc/"
description: "gnutls_malloc – Allocates and returns data"
---

<h2>NAME</h2>
<p> gnutls_malloc &#8211; Allocates and returns data</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>void * gnutls_malloc(size_t </code><i>s</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>size_t s</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> This function will allocate &#8216;s&#8217; bytes data, and return a pointer to memory. This function is supposed to be used by callbacks. </p>
<p> The allocation function used is the one set by <code>gnutls_global_set_mem_functions()</code>.</p>
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
