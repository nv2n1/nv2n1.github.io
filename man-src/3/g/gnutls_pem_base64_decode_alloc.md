---
title: "gnutls_pem_base64_decode_alloc(3)"
name: "gnutls_pem_base64_decode_alloc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pem_base64_decode_alloc/"
description: "gnutls_pem_base64_decode_alloc – API function"
---

<h2>NAME</h2>
<p> gnutls_pem_base64_decode_alloc &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_pem_base64_decode_alloc(const char * </code><i>header</i><code>, const gnutls_datum_t * </code><i>b64_data</i><code>, gnutls_datum_t * </code><i>result</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * header</p>
<dd> The PEM header (eg. CERTIFICATE)</p>
<dt>const gnutls_datum_t * b64_data</p>
<dd> contains the encoded data</p>
<dt>gnutls_datum_t * result</p>
<dd> the place where decoded data lie</dl>
<h2>DESCRIPTION</h2>
<p> This function will decode the given encoded data. The decoded data will be allocated, and stored into result. If the header given is non null this function will search for &quot;&#8212;&#8211;BEGIN header&quot; and decode only this part. Otherwise it will decode the first PEM packet found. </p>
<p> You should use <code>gnutls_free()</code> to free the returned data.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise an error code is returned.</p>
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
