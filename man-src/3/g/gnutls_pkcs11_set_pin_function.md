---
title: "gnutls_pkcs11_set_pin_function(3)"
name: "gnutls_pkcs11_set_pin_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_set_pin_function/"
description: "gnutls_pkcs11_set_pin_function – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_set_pin_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>void gnutls_pkcs11_set_pin_function(gnutls_pin_callback_t </code><i>fn</i><code>, void * </code><i>userdata</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pin_callback_t fn</p>
<dd> The PIN callback, a <code>gnutls_pin_callback_t()</code> function.</p>
<dt>void * userdata</p>
<dd> data to be supplied to callback</dl>
<h2>DESCRIPTION</h2>
<p> This function will set a callback function to be used when a PIN is required for PKCS 11 operations. See <code>gnutls_pin_callback_t()</code> on how the callback should behave.</p>
<h2>SINCE</h2>
<p> 2.12.0</p>
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
