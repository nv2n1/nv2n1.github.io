---
title: "gnutls_pkcs11_obj_set_pin_function(3)"
name: "gnutls_pkcs11_obj_set_pin_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_obj_set_pin_function/"
description: "gnutls_pkcs11_obj_set_pin_function – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_obj_set_pin_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>void gnutls_pkcs11_obj_set_pin_function(gnutls_pkcs11_obj_t </code><i>obj</i><code>, gnutls_pin_callback_t </code><i>fn</i><code>, void * </code><i>userdata</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs11_obj_t obj</p>
<dd> The object structure</p>
<dt>gnutls_pin_callback_t fn</p>
<dd> the callback</p>
<dt>void * userdata</p>
<dd> data associated with the callback</dl>
<h2>DESCRIPTION</h2>
<p> This function will set a callback function to be used when required to access the object. This function overrides the global set using <code>gnutls_pkcs11_set_pin_function()</code>.</p>
<h2>SINCE</h2>
<p> 3.1.0</p>
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
