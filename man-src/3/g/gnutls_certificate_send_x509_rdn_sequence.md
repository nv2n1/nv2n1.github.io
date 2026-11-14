---
title: "gnutls_certificate_send_x509_rdn_sequence(3)"
name: "gnutls_certificate_send_x509_rdn_sequence"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_send_x509_rdn_sequence/"
description: "gnutls_certificate_send_x509_rdn_sequence – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_send_x509_rdn_sequence &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_certificate_send_x509_rdn_sequence(gnutls_session_t </code><i>session</i><code>, int </code><i>status</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a pointer to a <code>gnutls_session_t</code> structure.</p>
<dt>int status</p>
<dd> is 0 or 1</dl>
<h2>DESCRIPTION</h2>
<p> If status is non zero, this function will order gnutls not to send the rdnSequence in the certificate request message. That is the server will not advertise its trusted CAs to the peer. If status is zero then the default behaviour will take effect, which is to advertise the server&#8217;s trusted CAs. </p>
<p> This function has no effect in clients, and in authentication methods other than certificate with X.509 certificates.</p>
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
