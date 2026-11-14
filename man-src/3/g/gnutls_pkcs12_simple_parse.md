---
title: "gnutls_pkcs12_simple_parse(3)"
name: "gnutls_pkcs12_simple_parse"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs12_simple_parse/"
description: "gnutls_pkcs12_simple_parse – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs12_simple_parse &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs12.h&gt;</code> </p>
<p> <code>int gnutls_pkcs12_simple_parse(gnutls_pkcs12_t </code><i>p12</i><code>, const char * </code><i>password</i><code>, gnutls_x509_privkey_t * </code><i>key</i><code>, gnutls_x509_crt_t ** </code><i>chain</i><code>, unsigned int * </code><i>chain_len</i><code>, gnutls_x509_crt_t ** </code><i>extra_certs</i><code>, unsigned int * </code><i>extra_certs_len</i><code>, gnutls_x509_crl_t * </code><i>crl</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs12_t p12</p>
<dd> should contain a gnutls_pkcs12_t structure</p>
<dt>const char * password</p>
<dd> optional password used to decrypt the structure, bags and keys.</p>
<dt>gnutls_x509_privkey_t * key</p>
<dd> a structure to store the parsed private key.</p>
<dt>gnutls_x509_crt_t ** chain</p>
<dd> the corresponding to key certificate chain (may be <code>NULL</code>)</p>
<dt>unsigned int * chain_len</p>
<dd> will be updated with the number of additional (may be <code>NULL</code>)</p>
<dt>gnutls_x509_crt_t ** extra_certs</p>
<dd> optional pointer to receive an array of additional certificates found in the PKCS12 structure (may be <code>NULL</code>).</p>
<dt>unsigned int * extra_certs_len</p>
<dd> will be updated with the number of additional certs (may be <code>NULL</code>).</p>
<dt>gnutls_x509_crl_t * crl</p>
<dd> an optional structure to store the parsed CRL (may be <code>NULL</code>).</p>
<dt>unsigned int flags</p>
<dd> should be zero or one of GNUTLS_PKCS12_SP_*</dl>
<h2>DESCRIPTION</h2>
<p> This function parses a PKCS12 structure in <i>pkcs12</i> and extracts the private key, the corresponding certificate chain, any additional certificates and a CRL. </p>
<p> The <i>extra_certs</i> and <i>extra_certs_len</i> parameters are optional and both may be set to <code>NULL</code>. If either is non-<code>NULL</code>, then both must be set. The value for <i>extra_certs</i> is allocated using <code>gnutls_malloc()</code>. </p>
<p> Encrypted PKCS12 bags and PKCS8 private keys are supported, but only with password based security and the same password for all operations. </p>
<p> Note that a PKCS12 structure may contain many keys and/or certificates, and there is no way to identify which key/certificate pair you want. For this reason this function is useful for PKCS12 files that contain only one key/certificate pair and/or one CRL. </p>
<p> If the provided structure has encrypted fields but no password is provided then this function returns <code>GNUTLS_E_DECRYPTION_FAILED</code>. </p>
<p> Note that normally the chain constructed does not include self signed certificates, to comply with TLS&#8217; requirements. If, however, the flag <code>GNUTLS_PKCS12_SP_INCLUDE_SELF_SIGNED</code> is specified then self signed certificates will be included in the chain. </p>
<p> Prior to using this function the PKCS <code>12</code> structure integrity must be verified using <code>gnutls_pkcs12_verify_mac()</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.1.0</p>
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
