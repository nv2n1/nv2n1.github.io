---
title: "gnutls_certificate_get_openpgp_keyring(3)"
name: "gnutls_certificate_get_openpgp_keyring"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_get_openpgp_keyring/"
description: "gnutls_certificate_get_openpgp_keyring – export keyring from a #gnutls_certificate_credentials_t"
---

<h2>NAME</h2>
<p> gnutls_certificate_get_openpgp_keyring &#8211; export keyring from a #gnutls_certificate_credentials_t</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>void gnutls_certificate_get_openpgp_keyring(gnutls_certificate_credentials_t </code><i>sc</i><code>, gnutls_openpgp_keyring_t * </code><i>keyring</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t sc</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</p>
<dt>gnutls_openpgp_keyring_t * keyring</p>
<dd> the exported keyring. Should be treated as constant</dl>
<h2>DESCRIPTION</h2>
<p> This function will export the OpenPGP keyring associated with the given credentials.</p>
<h2>SINCE</h2>
<p> 2.4.0</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnutls [at] gnu.org&gt;. GnuTLS home page: <a rel="nofollow" href="http://www.gnu.org/software/gnutls/">http://www.gnu.org/software/gnutls/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Free Software Foundation.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gnutls</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gnutls</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
