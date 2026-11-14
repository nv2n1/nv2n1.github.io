---
title: "gnutls_x509_crt_set_policy(3)"
name: "gnutls_x509_crt_set_policy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_set_policy/"
description: "gnutls_x509_crt_set_policy – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_set_policy &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_set_policy(gnutls_x509_crt_t </code><i>crt</i><code>, const struct gnutls_x509_policy_st * </code><i>policy</i><code>, unsigned int </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t crt</p>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</p>
<dt>const struct gnutls_x509_policy_st * policy</p>
<dd> A pointer to a policy structure.</p>
<dt>unsigned int critical</p>
<dd> use non-zero if the extension is marked as critical</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the certificate policy extension (2.5.29.32). Multiple calls to this function append a new policy. </p>
<p> Note the maximum text size for the qualifier <code>GNUTLS_X509_QUALIFIER_NOTICE</code> is 200 characters. This function will fail with <code>GNUTLS_E_INVALID_REQUEST</code> if this is exceeded.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.1.5</p>
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
