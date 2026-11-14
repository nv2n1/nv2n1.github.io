---
title: "gnutls_sec_param_to_symmetric_bits(3)"
name: "gnutls_sec_param_to_symmetric_bits"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_sec_param_to_symmetric_bits/"
description: "gnutls_sec_param_to_symmetric_bits – API function"
---

<h2>NAME</h2>
<p> gnutls_sec_param_to_symmetric_bits &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>unsigned int gnutls_sec_param_to_symmetric_bits(gnutls_sec_param_t </code><i>param</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_sec_param_t param</p>
<dd> is a security parameter</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the number of bits that correspond to symmetric cipher strength for the given security parameter.</p>
<h2>RETURNS</h2>
<p> The number of bits, or (0).</p>
<h2>SINCE</h2>
<p> 3.3.0</p>
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
