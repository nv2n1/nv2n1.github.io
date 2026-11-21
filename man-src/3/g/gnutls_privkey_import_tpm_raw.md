---

title: "gnutls_privkey_import_tpm_raw(3)"
name: "gnutls_privkey_import_tpm_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_import_tpm_raw/"
description: "gnutls_privkey_import_tpm_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_privkey_import_tpm_raw &#8211; API function</p>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_privkey_import_tpm_raw(gnutls_privkey_t </code><i>pkey</i><code>, const gnutls_datum_t * </code><i>fdata</i><code>, gnutls_tpmkey_fmt_t </code><i>format</i><code>, const char * </code><i>srk_password</i><code>, const char * </code><i>key_password</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t pkey</dt>
<dd> The private key</dd>
<dt>const gnutls_datum_t * fdata</dt>
<dd> The TPM key to be imported</dd>
<dt>gnutls_tpmkey_fmt_t format</dt>
<dd> The format of the private key</dd>
<dt>const char * srk_password</dt>
<dd> The password for the SRK key (optional)</dd>
<dt>const char * key_password</dt>
<dd> A password for the key (optional)</dd>
<dt>unsigned int flags</dt>
<dd> should be zero</dd></dl>
<p> This function will import the given private key to the abstract <code>gnutls_privkey_t</code> structure. </p>
<p> With respect to passwords the same as in <code>gnutls_privkey_import_tpm_url()</code> apply.</p>
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
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
