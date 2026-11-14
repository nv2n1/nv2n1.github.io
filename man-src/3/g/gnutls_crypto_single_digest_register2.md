---
title: "gnutls_crypto_single_digest_register2(3)"
name: "gnutls_crypto_single_digest_register2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_crypto_single_digest_register2/"
description: "gnutls_crypto_single_digest_register2 – register a digest algorithm"
---

<h2>NAME</h2>
<p> gnutls_crypto_single_digest_register2 &#8211; register a digest algorithm</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>int gnutls_crypto_single_digest_register2(gnutls_digest_algorithm_t </code><i>algorithm</i><code>, int </code><i>priority</i><code>, int </code><i>version</i><code>, gnutls_crypto_single_digest_st * </code><i>s</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_digest_algorithm_t algorithm</p>
<dd> is the gnutls algorithm identifier</p>
<dt>int priority</p>
<dd> is the priority of the algorithm</p>
<dt>int version</p>
<dd> should be set to <code>GNUTLS_CRYPTO_API_VERSION</code></p>
<dt>gnutls_crypto_single_digest_st * s</p>
<dd> is a structure holding new algorithms&#8217;s data</dl>
<h2>DESCRIPTION</h2>
<p> This function will register a digest (hash) algorithm to be used by gnutls. Any algorithm registered will override the included algorithms and by convention kernel implemented algorithms have priority of 90. The algorithm with the lowest priority will be used by gnutls. </p>
<p> This function should be called before <code>gnutls_global_init()</code>. </p>
<p> For simplicity you can use the convenience <code>gnutls_crypto_single_digest_register()</code> macro.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, otherwise an error.</p>
<h2>SINCE</h2>
<p> 2.6.0</p>
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
