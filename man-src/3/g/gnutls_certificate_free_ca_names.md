---
title: "gnutls_certificate_free_ca_names(3)"
name: "gnutls_certificate_free_ca_names"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_free_ca_names/"
description: "gnutls_certificate_free_ca_names – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_free_ca_names &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_certificate_free_ca_names(gnutls_certificate_credentials_t </code><i>sc</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t sc</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</dl>
<h2>DESCRIPTION</h2>
<p> This function will delete all the CA name in the given credentials. Clients may call this to save some memory since in client side the CA names are not used. Servers might want to use this function if a large list of trusted CAs is present and sending the names of it would just consume bandwidth without providing information to client. </p>
<p> CA names are used by servers to advertise the CAs they support to clients.</p>
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
