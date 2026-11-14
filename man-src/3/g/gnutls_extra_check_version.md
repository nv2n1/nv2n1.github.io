---
title: "gnutls_extra_check_version(3)"
name: "gnutls_extra_check_version"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_extra_check_version/"
description: "gnutls_extra_check_version – checks the libgnutls-extra version"
---

<h2>NAME</h2>
<p> gnutls_extra_check_version &#8211; checks the libgnutls-extra version</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/extra.h">gnutls/extra.h</a>&gt;</code> </p>
<p> <code>const char * gnutls_extra_check_version(const char * </code><i>req_version</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * req_version</p>
<dd> version string to compare with, or <code>NULL</code>.</dl>
<h2>DESCRIPTION</h2>
<p> Check GnuTLS Extra Library version. </p>
<p> See <code>GNUTLS_EXTRA_VERSION</code> for a suitable <i>req_version</i> string.</p>
<h2>RETURN VALUE</h2>
<p> Check that the version of the library is at minimum the one given as a string in <i>req_version</i> and return the actual version string of the library; return <code>NULL</code> if the condition is not met. If <code>NULL</code> is passed to this function no check is done and only the version string is returned.</p>
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
