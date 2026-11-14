---
title: "gnutls_x509_trust_list_add_crls(3)"
name: "gnutls_x509_trust_list_add_crls"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_trust_list_add_crls/"
description: "gnutls_x509_trust_list_add_crls – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_trust_list_add_crls &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_trust_list_add_crls(gnutls_x509_trust_list_t </code><i>list</i><code>, const gnutls_x509_crl_t * </code><i>crl_list</i><code>, int </code><i>crl_size</i><code>, unsigned int </code><i>flags</i><code>, unsigned int </code><i>verification_flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_trust_list_t list</p>
<dd> The structure of the list</p>
<dt>const gnutls_x509_crl_t * crl_list</p>
<dd> A list of CRLs</p>
<dt>int crl_size</p>
<dd> The length of the CRL list</p>
<dt>unsigned int flags</p>
<dd> if GNUTLS_TL_VERIFY_CRL is given the CRLs will be verified before being added.</p>
<dt>unsigned int verification_flags</p>
<dd> gnutls_certificate_verify_flags if flags specifies GNUTLS_TL_VERIFY_CRL</dl>
<h2>DESCRIPTION</h2>
<p> This function will add the given certificate revocation lists to the trusted list. The list of CRLs must not be deinitialized during this structure&#8217;s lifetime. </p>
<p> This function must be called after <code>gnutls_x509_trust_list_add_cas()</code> to allow verifying the CRLs for validity. If the flag <code>GNUTLS_TL_NO_DUPLICATES</code> is given, then any provided CRLs that are a duplicate, will be deinitialized and not added to the list (that assumes that <code>gnutls_x509_trust_list_deinit()</code> will be called with all=1).</p>
<h2>RETURNS</h2>
<p> The number of added elements is returned.</p>
<h2>SINCE</h2>
<p> 3.0</p>
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
