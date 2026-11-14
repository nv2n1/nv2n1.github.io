---
title: "gnutls_tpm_privkey_generate(3)"
name: "gnutls_tpm_privkey_generate"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_tpm_privkey_generate/"
description: "gnutls_tpm_privkey_generate – API function"
---

<h2>NAME</h2>
<p> gnutls_tpm_privkey_generate &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/tpm.h&gt;</code> </p>
<p> <code>int gnutls_tpm_privkey_generate(gnutls_pk_algorithm_t </code><i>pk</i><code>, unsigned int </code><i>bits</i><code>, const char * </code><i>srk_password</i><code>, const char * </code><i>key_password</i><code>, gnutls_tpmkey_fmt_t </code><i>format</i><code>, gnutls_x509_crt_fmt_t </code><i>pub_format</i><code>, gnutls_datum_t * </code><i>privkey</i><code>, gnutls_datum_t * </code><i>pubkey</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pk_algorithm_t pk</p>
<dd> the public key algorithm</p>
<dt>unsigned int bits</p>
<dd> the security bits</p>
<dt>const char * srk_password</p>
<dd> a password to protect the exported key (optional)</p>
<dt>const char * key_password</p>
<dd> the password for the TPM (optional)</p>
<dt>gnutls_tpmkey_fmt_t format</p>
<dd> the format of the private key</p>
<dt>gnutls_x509_crt_fmt_t pub_format</p>
<dd> the format of the public key</p>
<dt>gnutls_datum_t * privkey</p>
<dd> the generated key</p>
<dt>gnutls_datum_t * pubkey</p>
<dd> the corresponding public key (may be null)</p>
<dt>unsigned int flags</p>
<dd> should be a list of GNUTLS_TPM_* flags</dl>
<h2>DESCRIPTION</h2>
<p> This function will generate a private key in the TPM chip. The private key will be generated within the chip and will be exported in a wrapped with TPM&#8217;s master key form. Furthermore the wrapped key can be protected with the provided <i>password</i> . </p>
<p> Note that bits in TPM is quantized value. If the input value is not one of the allowed values, then it will be quantized to one of 512, 1024, 2048, 4096, 8192 and 16384. </p>
<p> Allowed flags are:</p>
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
