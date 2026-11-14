---
title: "gnutls_certificate_set_x509_key_file(3)"
name: "gnutls_certificate_set_x509_key_file"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_x509_key_file/"
description: "gnutls_certificate_set_x509_key_file – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_x509_key_file &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_certificate_set_x509_key_file(gnutls_certificate_credentials_t </code><i>res</i><code>, const char * </code><i>certfile</i><code>, const char * </code><i>keyfile</i><code>, gnutls_x509_crt_fmt_t </code><i>type</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t res</p>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</p>
<dt>const char * certfile</p>
<dd> is a file that containing the certificate list (path) for the specified private key, in PKCS7 format, or a list of certificates</p>
<dt>const char * keyfile</p>
<dd> is a file that contains the private key</p>
<dt>gnutls_x509_crt_fmt_t type</p>
<dd> is PEM or DER</dl>
<h2>DESCRIPTION</h2>
<p> This function sets a certificate/private key pair in the gnutls_certificate_credentials_t structure. This function may be called more than once, in case multiple keys/certificates exist for the server. For clients that need to send more than its own end entity certificate, e.g., also an intermediate CA cert, then the<br />
&nbsp;<wbr><i>certfile</i>&nbsp;<wbr>must contain the ordered certificate chain. </p>
<p> Note that the names in the certificate provided will be considered when selecting the appropriate certificate to use (in case of multiple certificate/key pairs). </p>
<p> This function can also accept URLs at <i>keyfile</i> and <i>certfile</i> . In that case it will import the private key and certificate indicated by the URLs. Note that the supported URLs are the ones indicated by <code>gnutls_url_is_supported()</code>. </p>
<p> In case the <i>certfile</i> is provided as a PKCS <code>11</code> URL, then the certificate, and its present issuers in the token are are imported (i.e., the required trust chain). </p>
<p> If that function fails to load the <i>res</i> structure is at an undefined state, it must not be reused to load other keys or certificates.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> (0) on success, or a negative error code.</p>
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
