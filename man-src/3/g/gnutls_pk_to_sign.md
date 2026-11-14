---
title: "gnutls_pk_to_sign(3)"
name: "gnutls_pk_to_sign"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pk_to_sign/"
description: "gnutls_pk_to_sign – API function"
---

<h2>NAME</h2>
<p> gnutls_pk_to_sign &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>gnutls_sign_algorithm_t gnutls_pk_to_sign(gnutls_pk_algorithm_t </code><i>pk</i><code>, gnutls_digest_algorithm_t </code><i>hash</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pk_algorithm_t pk</p>
<dd> is a public key algorithm</p>
<dt>gnutls_digest_algorithm_t hash</p>
<dd> a hash algorithm</dl>
<h2>DESCRIPTION</h2>
<p> This function maps public key and hash algorithms combinations to signature algorithms.</p>
<h2>RETURNS</h2>
<p> return a <code>gnutls_sign_algorithm_t</code> value, or <code>GNUTLS_SIGN_UNKNOWN</code> on error.</p>
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
