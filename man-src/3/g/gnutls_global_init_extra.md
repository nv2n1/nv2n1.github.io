---
title: "gnutls_global_init_extra(3)"
name: "gnutls_global_init_extra"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_global_init_extra/"
description: "gnutls_global_init_extra – initializes the global state of gnutls-extra"
---

<h2>NAME</h2>
<p> gnutls_global_init_extra &#8211; initializes the global state of gnutls-extra</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/extra.h">gnutls/extra.h</a>&gt;</code> </p>
<p> <code>int gnutls_global_init_extra( </code><i>void</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt> void</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> This function initializes the global state of gnutls-extra library to defaults. </p>
<p> Note that <code>gnutls_global_init()</code> has to be called before this function. If this function is not called then the gnutls-extra library will not be usable. </p>
<p> This function is not thread safe, see the discussion for <code>gnutls_global_init()</code> on how to deal with that.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (zero) is returned, otherwise an error code is returned.</p>
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
