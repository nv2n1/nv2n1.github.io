---
title: "gnutls_x509_crq_set_challenge_password(3)"
name: "gnutls_x509_crq_set_challenge_password"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_set_challenge_password/"
description: "gnutls_x509_crq_set_challenge_password – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_set_challenge_password &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_set_challenge_password(gnutls_x509_crq_t </code><i>crq</i><code>, const char * </code><i>pass</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> should contain a <code>gnutls_x509_crq_t</code> structure</p>
<dt>const char * pass</p>
<dd> holds a (0)-terminated password</dl>
<h2>DESCRIPTION</h2>
<p> This function will set a challenge password to be used when revoking the request.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
