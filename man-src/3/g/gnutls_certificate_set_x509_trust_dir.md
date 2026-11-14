---
title: "gnutls_certificate_set_x509_trust_dir(3)"
name: "gnutls_certificate_set_x509_trust_dir"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_x509_trust_dir/"
description: "gnutls_certificate_set_x509_trust_dir – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_x509_trust_dir &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_certificate_set_x509_trust_dir(gnutls_certificate_credentials_t </code><i>cred</i><code>, const char * </code><i>ca_dir</i><code>, gnutls_x509_crt_fmt_t </code><i>type</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t cred</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</p>
<dt>const char * ca_dir</p>
<dd> is a directory containing the list of trusted CAs (DER or PEM list)</p>
<dt>gnutls_x509_crt_fmt_t type</p>
<dd> is PEM or DER</dl>
<h2>DESCRIPTION</h2>
<p> This function adds the trusted CAs present in the directory in order to verify client or server certificates. This function is identical to <code>gnutls_certificate_set_x509_trust_file()</code> but loads all certificates in a directory.</p>
<h2>RETURNS</h2>
<p> the number of certificates processed</p>
<h2>SINCE</h2>
<p> 3.3.6</p>
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
