---
title: "gnutls_x509_crq_get_private_key_usage_period(3)"
name: "gnutls_x509_crq_get_private_key_usage_period"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_get_private_key_usage_period/"
description: "gnutls_x509_crq_get_private_key_usage_period – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_get_private_key_usage_period &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_get_private_key_usage_period(gnutls_x509_crq_t </code><i>crq</i><code>, time_t * </code><i>activation</i><code>, time_t * </code><i>expiration</i><code>, unsigned int * </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> should contain a <code>gnutls_x509_crq_t</code> structure</p>
<dt>time_t * activation</p>
<dd> The activation time</p>
<dt>time_t * expiration</p>
<dd> The expiration time</p>
<dt>unsigned int * critical</p>
<dd> the extension status</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the expiration and activation times of the private key of the certificate.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> if the extension is not present, otherwise a negative error value.</p>
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
