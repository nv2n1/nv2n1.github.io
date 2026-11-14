---
title: "gnutls_x509_crl_sign2(3)"
name: "gnutls_x509_crl_sign2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_sign2/"
description: "gnutls_x509_crl_sign2 – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_sign2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_sign2(gnutls_x509_crl_t </code><i>crl</i><code>, gnutls_x509_crt_t </code><i>issuer</i><code>, gnutls_x509_privkey_t </code><i>issuer_key</i><code>, gnutls_digest_algorithm_t </code><i>dig</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_t crl</p>
<dd> should contain a gnutls_x509_crl_t structure</p>
<dt>gnutls_x509_crt_t issuer</p>
<dd> is the certificate of the certificate issuer</p>
<dt>gnutls_x509_privkey_t issuer_key</p>
<dd> holds the issuer&#8217;s private key</p>
<dt>gnutls_digest_algorithm_t dig</p>
<dd> The message digest to use. GNUTLS_DIG_SHA1 is the safe choice unless you know what you&#8217;re doing.</p>
<dt>unsigned int flags</p>
<dd> must be 0</dl>
<h2>DESCRIPTION</h2>
<p> This function will sign the CRL with the issuer&#8217;s private key, and will copy the issuer&#8217;s information into the CRL. </p>
<p> This must be the last step in a certificate CRL since all the previously set parameters are now signed.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
