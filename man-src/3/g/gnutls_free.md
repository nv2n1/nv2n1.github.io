---
title: "gnutls_free(3)"
name: "gnutls_free"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_free/"
description: "gnutls_free – Returns a free() like function"
---

<h2>NAME</h2>
<p> gnutls_free &#8211; Returns a free() like function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>void gnutls_free(void * </code><i>ptr</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>void * ptr</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> This function will free data pointed by ptr. </p>
<p> The deallocation function used is the one set by <code>gnutls_global_set_mem_functions()</code>.</p>
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
