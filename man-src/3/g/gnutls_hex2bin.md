---

title: "gnutls_hex2bin(3)"
name: "gnutls_hex2bin"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_hex2bin/"
description: "gnutls_hex2bin – API function"
---

<p> gnutls_hex2bin &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_hex2bin(const char * </code><i>hex_data</i><code>, size_t </code><i>hex_size</i><code>, void * </code><i>bin_data</i><code>, size_t * </code><i>bin_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * hex_data</dt>
<dd> string with data in hex format</dd>
<dt>size_t hex_size</dt>
<dd> size of hex data</dd>
<dt>void * bin_data</dt>
<dd> output array with binary data</dd>
<dt>size_t * bin_size</dt>
<dd> when calling should hold maximum size of <i>bin_data</i> , on return will hold actual length of <i>bin_data</i> .</dd></dl>
<h2>DESCRIPTION</h2>
<p> Convert a buffer with hex data to binary data.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, otherwise a negative error code.</p>
<h2>SINCE</h2>
<p> 2.4.0</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
