---
title: "gnutls_openpgp_crt_get_key_usage(3)"
name: "gnutls_openpgp_crt_get_key_usage"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_crt_get_key_usage/"
description: "gnutls_openpgp_crt_get_key_usage – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_crt_get_key_usage &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_crt_get_key_usage(gnutls_openpgp_crt_t </code><i>key</i><code>, unsigned int * </code><i>key_usage</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_crt_t key</p>
<dd> should contain a gnutls_openpgp_crt_t structure</p>
<dt>unsigned int * key_usage</p>
<dd> where the key usage bits will be stored</dl>
<h2>DESCRIPTION</h2>
<p> This function will return certificate&#8217;s key usage, by checking the key algorithm. The key usage value will ORed values of the: <code>GNUTLS_KEY_DIGITAL_SIGNATURE</code>, <code>GNUTLS_KEY_KEY_ENCIPHERMENT</code>.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an error code.</p>
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
