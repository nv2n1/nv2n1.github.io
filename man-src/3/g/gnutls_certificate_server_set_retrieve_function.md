---
title: "gnutls_certificate_server_set_retrieve_function(3)"
name: "gnutls_certificate_server_set_retrieve_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_server_set_retrieve_function/"
description: "gnutls_certificate_server_set_retrieve_function – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_server_set_retrieve_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>void gnutls_certificate_server_set_retrieve_function(gnutls_certificate_credentials_t </code><i>cred</i><code>, gnutls_certificate_server_retrieve_function * </code><i>func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t cred</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</p>
<dt>gnutls_certificate_server_retrieve_function * func</p>
<dd> is the callback function</dl>
<h2>DESCRIPTION</h2>
<p> This function sets a callback to be called in order to retrieve the certificate to be used in the handshake. You are advised to use <code>gnutls_certificate_set_retrieve_function2()</code> because it is much more efficient in the processing it requires from gnutls. </p>
<p> The callback&#8217;s function prototype is: int (*callback)(gnutls_session_t, gnutls_retr_st* st); </p>
<p>&nbsp;<wbr><i>st</i>&nbsp;<wbr>should contain the certificates and private keys. </p>
<p> If the callback function is provided then gnutls will call it, in the handshake, after the certificate request message has been received. </p>
<p> The callback function should set the certificate list to be sent, and return 0 on success. The value (-1) indicates error and the handshake will be terminated.</p>
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
