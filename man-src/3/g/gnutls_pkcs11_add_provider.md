---
title: "gnutls_pkcs11_add_provider(3)"
name: "gnutls_pkcs11_add_provider"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_add_provider/"
description: "gnutls_pkcs11_add_provider – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_add_provider &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_add_provider(const char * </code><i>name</i><code>, const char * </code><i>params</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * name</p>
<dd> The filename of the module</p>
<dt>const char * params</p>
<dd> should be NULL</dl>
<h2>DESCRIPTION</h2>
<p> This function will load and add a PKCS 11 module to the module list used in gnutls. After this function is called the module will be used for PKCS 11 operations. </p>
<p> When loading a module to be used for certificate verification, use the string &#8216;trusted&#8217; as <i>params</i> . </p>
<p> Note that this function is not thread safe.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
