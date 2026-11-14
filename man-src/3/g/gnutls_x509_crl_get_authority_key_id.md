---
title: "gnutls_x509_crl_get_authority_key_id(3)"
name: "gnutls_x509_crl_get_authority_key_id"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_get_authority_key_id/"
description: "gnutls_x509_crl_get_authority_key_id – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_get_authority_key_id &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_get_authority_key_id(gnutls_x509_crl_t </code><i>crl</i><code>, void * </code><i>id</i><code>, size_t * </code><i>id_size</i><code>, unsigned int * </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_t crl</p>
<dd> should contain a <code>gnutls_x509_crl_t</code> structure</p>
<dt>void * id</p>
<dd> The place where the identifier will be copied</p>
<dt>size_t * id_size</p>
<dd> Holds the size of the result field.</p>
<dt>unsigned int * critical</p>
<dd> will be non-zero if the extension is marked as critical (may be null)</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the CRL authority&#8217;s key identifier. This is obtained by the X.509 Authority Key identifier extension field (2.5.29.35). Note that this function only returns the keyIdentifier field of the extension and <code>GNUTLS_E_X509_UNSUPPORTED_EXTENSION</code>, if the extension contains the name and serial number of the certificate. In that case <code>gnutls_x509_crl_get_authority_key_gn_serial()</code> may be used.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code in case of an error.</p>
<h2>SINCE</h2>
<p> 2.8.0</p>
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
