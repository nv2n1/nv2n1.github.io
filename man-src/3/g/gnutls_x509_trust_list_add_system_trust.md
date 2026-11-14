---
title: "gnutls_x509_trust_list_add_system_trust(3)"
name: "gnutls_x509_trust_list_add_system_trust"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_trust_list_add_system_trust/"
description: "gnutls_x509_trust_list_add_system_trust – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_trust_list_add_system_trust &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_trust_list_add_system_trust(gnutls_x509_trust_list_t </code><i>list</i><code>, unsigned int </code><i>tl_flags</i><code>, unsigned int </code><i>tl_vflags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_trust_list_t list</p>
<dd> The structure of the list</p>
<dt>unsigned int tl_flags</p>
<dd> GNUTLS_TL_*</p>
<dt>unsigned int tl_vflags</p>
<dd> gnutls_certificate_verify_flags if flags specifies GNUTLS_TL_VERIFY_CRL</dl>
<h2>DESCRIPTION</h2>
<p> This function adds the system&#8217;s default trusted certificate authorities to the trusted list. Note that on unsupported systems this function returns <code>GNUTLS_E_UNIMPLEMENTED_FEATURE</code>. </p>
<p> This function implies the flag <code>GNUTLS_TL_NO_DUPLICATES</code>.</p>
<h2>RETURNS</h2>
<p> The number of added elements or a negative error code on error.</p>
<h2>SINCE</h2>
<p> 3.1</p>
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
