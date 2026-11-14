---
title: "gnutls_cipher_suite_get_name(3)"
name: "gnutls_cipher_suite_get_name"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_cipher_suite_get_name/"
description: "gnutls_cipher_suite_get_name – API function"
---

<h2>NAME</h2>
<p> gnutls_cipher_suite_get_name &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>const char * gnutls_cipher_suite_get_name(gnutls_kx_algorithm_t </code><i>kx_algorithm</i><code>, gnutls_cipher_algorithm_t </code><i>cipher_algorithm</i><code>, gnutls_mac_algorithm_t </code><i>mac_algorithm</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_kx_algorithm_t kx_algorithm</p>
<dd> is a Key exchange algorithm</p>
<dt>gnutls_cipher_algorithm_t cipher_algorithm</p>
<dd> is a cipher algorithm</p>
<dt>gnutls_mac_algorithm_t mac_algorithm</p>
<dd> is a MAC algorithm</dl>
<h2>DESCRIPTION</h2>
<p> Note that the full cipher suite name must be prepended by TLS or SSL depending of the protocol in use.</p>
<h2>RETURNS</h2>
<p> a string that contains the name of a TLS cipher suite, specified by the given algorithms, or <code>NULL</code>.</p>
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
