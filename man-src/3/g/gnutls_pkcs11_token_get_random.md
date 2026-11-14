---
title: "gnutls_pkcs11_token_get_random(3)"
name: "gnutls_pkcs11_token_get_random"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_token_get_random/"
description: "gnutls_pkcs11_token_get_random – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_token_get_random &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_token_get_random(const char * </code><i>token_url</i><code>, void * </code><i>rnddata</i><code>, size_t </code><i>len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * token_url</p>
<dd> A PKCS <code>11</code> URL specifying a token</p>
<dt>void * rnddata</p>
<dd> A pointer to the memory area to be filled with random data</p>
<dt>size_t len</p>
<dd> The number of bytes of randomness to request</dl>
<h2>DESCRIPTION</h2>
<p> This function will get random data from the given token. It will store rnddata and fill the memory pointed to by rnddata with len random bytes from the token.</p>
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
