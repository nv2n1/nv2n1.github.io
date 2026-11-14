---
title: "gnutls_x509_privkey_export_pkcs8(3)"
name: "gnutls_x509_privkey_export_pkcs8"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_privkey_export_pkcs8/"
description: "gnutls_x509_privkey_export_pkcs8 – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_privkey_export_pkcs8 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_privkey_export_pkcs8(gnutls_x509_privkey_t </code><i>key</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>, const char * </code><i>password</i><code>, unsigned int </code><i>flags</i><code>, void * </code><i>output_data</i><code>, size_t * </code><i>output_data_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_privkey_t key</p>
<dd> Holds the key</p>
<dt>gnutls_x509_crt_fmt_t format</p>
<dd> the format of output params. One of PEM or DER.</p>
<dt>const char * password</p>
<dd> the password that will be used to encrypt the key.</p>
<dt>unsigned int flags</p>
<dd> an ORed sequence of gnutls_pkcs_encrypt_flags_t</p>
<dt>void * output_data</p>
<dd> will contain a private key PEM or DER encoded</p>
<dt>size_t * output_data_size</p>
<dd> holds the size of output_data (and will be replaced by the actual size of parameters)</dl>
<h2>DESCRIPTION</h2>
<p> This function will export the private key to a PKCS8 structure. Both RSA and DSA keys can be exported. For DSA keys we use PKCS <code>11</code> definitions. If the flags do not specify the encryption cipher, then the default 3DES (PBES2) will be used. </p>
<p> The <i>password</i> can be either ASCII or UTF-8 in the default PBES2 encryption schemas, or ASCII for the PKCS12 schemas. </p>
<p> If the buffer provided is not long enough to hold the output, then *output_data_size is updated and GNUTLS_E_SHORT_MEMORY_BUFFER will be returned. </p>
<p> If the structure is PEM encoded, it will have a header of &quot;BEGIN ENCRYPTED PRIVATE KEY&quot; or &quot;BEGIN PRIVATE KEY&quot; if encryption is not used.</p>
<h2>RETURNS</h2>
<p> In case of failure a negative error code will be returned, and 0 on success.</p>
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
