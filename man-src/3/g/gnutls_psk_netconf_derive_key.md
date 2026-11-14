---
title: "gnutls_psk_netconf_derive_key(3)"
name: "gnutls_psk_netconf_derive_key"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_psk_netconf_derive_key/"
description: "gnutls_psk_netconf_derive_key – derive PSK Netconf key from password"
---

<h2>NAME</h2>
<p> gnutls_psk_netconf_derive_key &#8211; derive PSK Netconf key from password</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>int gnutls_psk_netconf_derive_key(const char * </code><i>password</i><code>, const char * </code><i>psk_identity</i><code>, const char * </code><i>psk_identity_hint</i><code>, gnutls_datum_t * </code><i>output_key</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * password</p>
<dd> zero terminated string containing password.</p>
<dt>const char * psk_identity</p>
<dd> zero terminated string with PSK identity.</p>
<dt>const char * psk_identity_hint</p>
<dd> zero terminated string with PSK identity hint.</p>
<dt>gnutls_datum_t * output_key</p>
<dd> output variable, contains newly allocated *data pointer.</dl>
<h2>DESCRIPTION</h2>
<p> This function will derive a PSK key from a password, for use with the Netconf protocol.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an error code.</p>
<h2>SINCE</h2>
<p> 2.4.0</p>
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
