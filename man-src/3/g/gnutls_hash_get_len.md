---
title: "gnutls_hash_get_len(3)"
name: "gnutls_hash_get_len"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_hash_get_len/"
description: "gnutls_hash_get_len – API function"
---

<h2>NAME</h2>
<p> gnutls_hash_get_len &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/crypto.h&gt;</code> </p>
<p> <code>int gnutls_hash_get_len(gnutls_digest_algorithm_t </code><i>algorithm</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_digest_algorithm_t algorithm</p>
<dd> the hash algorithm to use</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the length of the output data of the given hash algorithm.</p>
<h2>RETURNS</h2>
<p> The length or zero on error.</p>
<h2>SINCE</h2>
<p> 2.10.0</p>
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
