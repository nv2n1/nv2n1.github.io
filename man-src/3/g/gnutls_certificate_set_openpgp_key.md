---
title: "gnutls_certificate_set_openpgp_key(3)"
name: "gnutls_certificate_set_openpgp_key"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_openpgp_key/"
description: "gnutls_certificate_set_openpgp_key – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_openpgp_key &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_certificate_set_openpgp_key(gnutls_certificate_credentials_t </code><i>res</i><code>, gnutls_openpgp_crt_t </code><i>crt</i><code>, gnutls_openpgp_privkey_t </code><i>pkey</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t res</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</p>
<dt>gnutls_openpgp_crt_t crt</p>
<dd> contains an openpgp public key</p>
<dt>gnutls_openpgp_privkey_t pkey</p>
<dd> is an openpgp private key</dl>
<h2>DESCRIPTION</h2>
<p> This function sets a certificate/private key pair in the gnutls_certificate_credentials_t structure. This function may be called more than once (in case multiple keys/certificates exist for the server). </p>
<p> Note that this function requires that the preferred key ids have been set and be used. See <code>gnutls_openpgp_crt_set_preferred_key_id()</code>. Otherwise the master key will be used.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
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
