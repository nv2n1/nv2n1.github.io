---
title: "gnutls_certificate_set_rsa_export_params(3)"
name: "gnutls_certificate_set_rsa_export_params"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_rsa_export_params/"
description: "gnutls_certificate_set_rsa_export_params – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_rsa_export_params &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>void gnutls_certificate_set_rsa_export_params(gnutls_certificate_credentials_t </code><i>res</i><code>, gnutls_rsa_params_t </code><i>rsa_params</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t res</p>
<dd> is a gnutls_certificate_credentials_t structure</p>
<dt>gnutls_rsa_params_t rsa_params</p>
<dd> is a structure that holds temporary RSA parameters.</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the temporary RSA parameters for a certificate server to use. These parameters will be used in RSA-EXPORT cipher suites.</p>
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
