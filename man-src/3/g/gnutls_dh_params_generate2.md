---
title: "gnutls_dh_params_generate2(3)"
name: "gnutls_dh_params_generate2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_dh_params_generate2/"
description: "gnutls_dh_params_generate2 – API function"
---

<h2>NAME</h2>
<p> gnutls_dh_params_generate2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_dh_params_generate2(gnutls_dh_params_t </code><i>dparams</i><code>, unsigned int </code><i>bits</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_dh_params_t dparams</p>
<dd> Is the structure that the DH parameters will be stored</p>
<dt>unsigned int bits</p>
<dd> is the prime&#8217;s number of bits</dl>
<h2>DESCRIPTION</h2>
<p> This function will generate a new pair of prime and generator for use in the Diffie-Hellman key exchange. The new parameters will be allocated using <code>gnutls_malloc()</code> and will be stored in the appropriate datum. This function is normally slow. </p>
<p> Do not set the number of bits directly, use <code>gnutls_sec_param_to_pk_bits()</code> to get bits for <code>GNUTLS_PK_DSA</code>. Also note that the DH parameters are only useful to servers. Since clients use the parameters sent by the server, it&#8217;s of no use to call this in client side.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
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
