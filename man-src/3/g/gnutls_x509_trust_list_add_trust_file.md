---
title: "gnutls_x509_trust_list_add_trust_file(3)"
name: "gnutls_x509_trust_list_add_trust_file"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_trust_list_add_trust_file/"
description: "gnutls_x509_trust_list_add_trust_file – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_trust_list_add_trust_file &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_trust_list_add_trust_file(gnutls_x509_trust_list_t </code><i>list</i><code>, const char * </code><i>ca_file</i><code>, const char * </code><i>crl_file</i><code>, gnutls_x509_crt_fmt_t </code><i>type</i><code>, unsigned int </code><i>tl_flags</i><code>, unsigned int </code><i>tl_vflags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_trust_list_t list</p>
<dd> The structure of the list</p>
<dt>const char * ca_file</p>
<dd> A file containing a list of CAs (optional)</p>
<dt>const char * crl_file</p>
<dd> A file containing a list of CRLs (optional)</p>
<dt>gnutls_x509_crt_fmt_t type</p>
<dd> The format of the certificates</p>
<dt>unsigned int tl_flags</p>
<dd> GNUTLS_TL_*</p>
<dt>unsigned int tl_vflags</p>
<dd> gnutls_certificate_verify_flags if flags specifies GNUTLS_TL_VERIFY_CRL</dl>
<h2>DESCRIPTION</h2>
<p> This function will add the given certificate authorities to the trusted list. PKCS <code>11</code> URLs are also accepted, instead of files, by this function. A PKCS <code>11</code> URL implies a trust database (a specially marked module in p11-kit); the URL &quot;pkcs11:&quot; implies all trust databases in the system. Only a single URL specifying trust databases can be set; they cannot be stacked with multiple calls.</p>
<h2>RETURNS</h2>
<p> The number of added elements is returned.</p>
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
