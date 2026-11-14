---
title: "gnutls_psk_set_server_params_function(3)"
name: "gnutls_psk_set_server_params_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_psk_set_server_params_function/"
description: "gnutls_psk_set_server_params_function – API function"
---

<h2>NAME</h2>
<p> gnutls_psk_set_server_params_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_psk_set_server_params_function(gnutls_psk_server_credentials_t </code><i>res</i><code>, gnutls_params_function * </code><i>func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_psk_server_credentials_t res</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure</p>
<dt>gnutls_params_function * func</p>
<dd> is the function to be called</dl>
<h2>DESCRIPTION</h2>
<p> This function will set a callback in order for the server to get the Diffie-Hellman parameters for PSK authentication. The callback should return <code>GNUTLS_E_SUCCESS</code> (0) on success.</p>
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
