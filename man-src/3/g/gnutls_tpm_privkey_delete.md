---
title: "gnutls_tpm_privkey_delete(3)"
name: "gnutls_tpm_privkey_delete"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_tpm_privkey_delete/"
description: "gnutls_tpm_privkey_delete – API function"
---

<h2>NAME</h2>
<p> gnutls_tpm_privkey_delete &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/tpm.h&gt;</code> </p>
<p> <code>int gnutls_tpm_privkey_delete(const char * </code><i>url</i><code>, const char * </code><i>srk_password</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * url</p>
<dd> the URL describing the key</p>
<dt>const char * srk_password</p>
<dd> a password for the SRK key</dl>
<h2>DESCRIPTION</h2>
<p> This function will unregister the private key from the TPM chip.</p>
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
