---
title: "gnutls_rsa_params_generate2(3)"
name: "gnutls_rsa_params_generate2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_rsa_params_generate2/"
description: "gnutls_rsa_params_generate2 – API function"
---

<h2>NAME</h2>
<p> gnutls_rsa_params_generate2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_rsa_params_generate2(gnutls_rsa_params_t </code><i>params</i><code>, unsigned int </code><i>bits</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_rsa_params_t params</p>
<dd> The structure where the parameters will be stored</p>
<dt>unsigned int bits</p>
<dd> is the prime&#8217;s number of bits</dl>
<h2>DESCRIPTION</h2>
<p> This function will generate new temporary RSA parameters for use in RSA-EXPORT ciphersuites. This function is normally slow. </p>
<p> Note that if the parameters are to be used in export cipher suites the bits value should be 512 or less. Also note that the generation of new RSA parameters is only useful to servers. Clients use the parameters sent by the server, thus it&#8217;s no use calling this in client side.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an negative error code.</p>
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
