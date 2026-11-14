---
title: "gnutls_privkey_import_tpm_url(3)"
name: "gnutls_privkey_import_tpm_url"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_import_tpm_url/"
description: "gnutls_privkey_import_tpm_url – API function"
---

<h2>NAME</h2>
<p> gnutls_privkey_import_tpm_url &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_privkey_import_tpm_url(gnutls_privkey_t </code><i>pkey</i><code>, const char * </code><i>url</i><code>, const char * </code><i>srk_password</i><code>, const char * </code><i>key_password</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t pkey</p>
<dd> The private key</p>
<dt>const char * url</p>
<dd> The URL of the TPM key to be imported</p>
<dt>const char * srk_password</p>
<dd> The password for the SRK key (optional)</p>
<dt>const char * key_password</p>
<dd> A password for the key (optional)</p>
<dt>unsigned int flags</p>
<dd> One of the GNUTLS_PRIVKEY_* flags</dl>
<h2>DESCRIPTION</h2>
<p> This function will import the given private key to the abstract <code>gnutls_privkey_t</code> structure. </p>
<p> Note that unless <code>GNUTLS_PRIVKEY_DISABLE_CALLBACKS</code> is specified, if incorrect (or NULL) passwords are given the PKCS11 callback functions will be used to obtain the correct passwords. Otherwise if the SRK password is wrong <code>GNUTLS_E_TPM_SRK_PASSWORD_ERROR</code> is returned and if the key password is wrong or not provided then <code>GNUTLS_E_TPM_KEY_PASSWORD_ERROR</code> is returned.</p>
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
