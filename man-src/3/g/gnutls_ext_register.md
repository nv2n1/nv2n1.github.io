---
title: "gnutls_ext_register(3)"
name: "gnutls_ext_register"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ext_register/"
description: "gnutls_ext_register – Register a handler for a TLS extension"
---

<h2>NAME</h2>
<p> gnutls_ext_register &#8211; Register a handler for a TLS extension</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>int gnutls_ext_register(int </code><i>type</i><code>, const char * </code><i>name</i><code>, gnutls_ext_parse_type_t </code><i>parse_type</i><code>, gnutls_ext_recv_func </code><i>recv_func</i><code>, gnutls_ext_send_func </code><i>send_func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>int type</p>
<dd> the 16-bit integer referring to the extension type</p>
<dt>const char * name</p>
<dd> human printable name of the extension used for debugging</p>
<dt>gnutls_ext_parse_type_t parse_type</p>
<dd> either <code>GNUTLS_EXT_TLS</code> or <code>GNUTLS_EXT_APPLICATION</code>.</p>
<dt>gnutls_ext_recv_func recv_func</p>
<dd> a function to receive extension data</p>
<dt>gnutls_ext_send_func send_func</p>
<dd> a function to send extension data</dl>
<h2>DESCRIPTION</h2>
<p> This function is used to register a new TLS extension handler.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an error code.</p>
<h2>SINCE</h2>
<p> 2.6.0</p>
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
