---
title: "gnutls_sign_algorithm_get_name(3)"
name: "gnutls_sign_algorithm_get_name"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_sign_algorithm_get_name/"
description: "gnutls_sign_algorithm_get_name – Returns a string with the name of the specified sign algorithm"
---

<h2>NAME</h2>
<p> gnutls_sign_algorithm_get_name &#8211; Returns a string with the name of the specified sign algorithm</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>const char * gnutls_sign_algorithm_get_name(gnutls_sign_algorithm_t </code><i>sign</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_sign_algorithm_t sign</p>
<dd> is a sign algorithm</dl>
<h2>DESCRIPTION</h2>
<p> Convert a <code>gnutls_sign_algorithm_t</code> value to a string.</p>
<h2>RETURNS</h2>
<p> a string that contains the name of the specified sign algorithm, or <code>NULL</code>.</p>
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
