---
title: "gnutls_x509_policies_get(3)"
name: "gnutls_x509_policies_get"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_policies_get/"
description: "gnutls_x509_policies_get – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_policies_get &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509-ext.h&gt;</code> </p>
<p> <code>int gnutls_x509_policies_get(gnutls_x509_policies_t </code><i>policies</i><code>, unsigned int </code><i>seq</i><code>, struct gnutls_x509_policy_st * </code><i>policy</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_policies_t policies</p>
<dd> The policies structure</p>
<dt>unsigned int seq</p>
<dd> The index of the name to get</p>
<dt>struct gnutls_x509_policy_st * policy</p>
<dd> Will hold the policy</dl>
<h2>DESCRIPTION</h2>
<p> This function will return a specific policy as stored in the <i>policies</i> structure. The returned values should be treated as constant and valid for the lifetime of <i>policies</i> .</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> if the index is out of bounds, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.3.0</p>
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
