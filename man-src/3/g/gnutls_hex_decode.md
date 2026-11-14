---
title: "gnutls_hex_decode(3)"
name: "gnutls_hex_decode"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_hex_decode/"
description: "gnutls_hex_decode – API function"
---

<h2>NAME</h2>
<p> gnutls_hex_decode &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_hex_decode(const gnutls_datum_t * </code><i>hex_data</i><code>, void * </code><i>result</i><code>, size_t * </code><i>result_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const gnutls_datum_t * hex_data</p>
<dd> contain the encoded data</p>
<dt>void * result</p>
<dd> the place where decoded data will be copied</p>
<dt>size_t * result_size</p>
<dd> holds the size of the result</dl>
<h2>DESCRIPTION</h2>
<p> This function will decode the given encoded data, using the hex encoding used by PSK password files. </p>
<p> Note that hex_data should be null terminated.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> if the buffer given is not long enough, or 0 on success.</p>
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
