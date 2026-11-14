---
title: "gnutls_x509_crt_set_pin_function(3)"
name: "gnutls_x509_crt_set_pin_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_set_pin_function/"
description: "gnutls_x509_crt_set_pin_function – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_set_pin_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>void gnutls_x509_crt_set_pin_function(gnutls_x509_crt_t </code><i>crt</i><code>, gnutls_pin_callback_t </code><i>fn</i><code>, void * </code><i>userdata</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t crt</p>
<dd> The certificate structure</p>
<dt>gnutls_pin_callback_t fn</p>
<dd> the callback</p>
<dt>void * userdata</p>
<dd> data associated with the callback</dl>
<h2>DESCRIPTION</h2>
<p> This function will set a callback function to be used when it is required to access a protected object. This function overrides the global function set using <code>gnutls_pkcs11_set_pin_function()</code>. </p>
<p> Note that this callback is currently used only during the import of a PKCS <code>11</code> certificate with <code>gnutls_x509_crt_import_pkcs11_url()</code>.</p>
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
