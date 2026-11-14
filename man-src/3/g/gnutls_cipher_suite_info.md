---
title: "gnutls_cipher_suite_info(3)"
name: "gnutls_cipher_suite_info"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_cipher_suite_info/"
description: "gnutls_cipher_suite_info – API function"
---

<h2>NAME</h2>
<p> gnutls_cipher_suite_info &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>const char * gnutls_cipher_suite_info(size_t </code><i>idx</i><code>, unsigned char * </code><i>cs_id</i><code>, gnutls_kx_algorithm_t * </code><i>kx</i><code>, gnutls_cipher_algorithm_t * </code><i>cipher</i><code>, gnutls_mac_algorithm_t * </code><i>mac</i><code>, gnutls_protocol_t * </code><i>min_version</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>size_t idx</p>
<dd> index of cipher suite to get information about, starts on 0.</p>
<dt>unsigned char * cs_id</p>
<dd> output buffer with room for 2 bytes, indicating cipher suite value</p>
<dt>gnutls_kx_algorithm_t * kx</p>
<dd> output variable indicating key exchange algorithm, or <code>NULL</code>.</p>
<dt>gnutls_cipher_algorithm_t * cipher</p>
<dd> output variable indicating cipher, or <code>NULL</code>.</p>
<dt>gnutls_mac_algorithm_t * mac</p>
<dd> output variable indicating MAC algorithm, or <code>NULL</code>.</p>
<dt>gnutls_protocol_t * min_version</p>
<dd> output variable indicating TLS protocol version, or <code>NULL</code>.</dl>
<h2>DESCRIPTION</h2>
<p> Get information about supported cipher suites. Use the function iteratively to get information about all supported cipher suites. Call with idx=0 to get information about first cipher suite, then idx=1 and so on until the function returns NULL.</p>
<h2>RETURNS</h2>
<p> the name of <i>idx</i> cipher suite, and set the information about the cipher suite in the output variables. If <i>idx</i> is out of bounds, <code>NULL</code> is returned.</p>
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
