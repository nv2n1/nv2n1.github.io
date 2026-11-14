---
title: "gnutls_pkcs11_token_init(3)"
name: "gnutls_pkcs11_token_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_token_init/"
description: "gnutls_pkcs11_token_init – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_token_init &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_token_init(const char * </code><i>token_url</i><code>, const char * </code><i>so_pin</i><code>, const char * </code><i>label</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * token_url</p>
<dd> A PKCS <code>11</code> URL specifying a token</p>
<dt>const char * so_pin</p>
<dd> Security Officer&#8217;s PIN</p>
<dt>const char * label</p>
<dd> A name to be used for the token</dl>
<h2>DESCRIPTION</h2>
<p> This function will initialize (format) a token. If the token is at a factory defaults state the security officer&#8217;s PIN given will be set to be the default. Otherwise it should match the officer&#8217;s PIN.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
