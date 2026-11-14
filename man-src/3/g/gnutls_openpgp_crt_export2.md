---
title: "gnutls_openpgp_crt_export2(3)"
name: "gnutls_openpgp_crt_export2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_crt_export2/"
description: "gnutls_openpgp_crt_export2 – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_crt_export2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_crt_export2(gnutls_openpgp_crt_t </code><i>key</i><code>, gnutls_openpgp_crt_fmt_t </code><i>format</i><code>, gnutls_datum_t * </code><i>out</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_crt_t key</p>
<dd> Holds the key.</p>
<dt>gnutls_openpgp_crt_fmt_t format</p>
<dd> One of gnutls_openpgp_crt_fmt_t elements.</p>
<dt>gnutls_datum_t * out</p>
<dd> will contain the raw or base64 encoded key</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the given key to RAW or Base64 format. The output buffer is allocated using <code>gnutls_malloc()</code>.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an error code.</p>
<h2>SINCE</h2>
<p> 3.1.3</p>
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
