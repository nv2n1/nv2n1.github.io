---
title: "gnutls_pkcs11_init(3)"
name: "gnutls_pkcs11_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_init/"
description: "gnutls_pkcs11_init – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_init &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_init(unsigned int </code><i>flags</i><code>, const char * </code><i>deprecated_config_file</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>unsigned int flags</p>
<dd> An ORed sequence of <code>GNUTLS_PKCS11_FLAG_</code>*</p>
<dt>const char * deprecated_config_file</p>
<dd> either NULL or the location of a deprecated configuration file</dl>
<h2>DESCRIPTION</h2>
<p> This function will initialize the PKCS 11 subsystem in gnutls. It will read configuration files if <code>GNUTLS_PKCS11_FLAG_AUTO</code> is used or allow you to independently load PKCS 11 modules using <code>gnutls_pkcs11_add_provider()</code> if <code>GNUTLS_PKCS11_FLAG_MANUAL</code> is specified. </p>
<p> Normally you don&#8217;t need to call this function since it is being called when the first PKCS 11 operation is requested using the <code>GNUTLS_PKCS11_FLAG_AUTO</code> flag. If another flags are required then it must be called independently prior to any PKCS 11 operation.</p>
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
