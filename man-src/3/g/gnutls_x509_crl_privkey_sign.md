---
title: "gnutls_x509_crl_privkey_sign(3)"
name: "gnutls_x509_crl_privkey_sign"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_privkey_sign/"
---

<h2>NAME</h2>

 gnutls_x509_crl_privkey_sign - API function

<h2>SYNOPSIS</h2>

 <b>#include &lt;gnutls/abstract.h&gt;</b> 

 <b>int gnutls_x509_crl_privkey_sign(gnutls_x509_crl_t </b><i>crl</i><b>, gnutls_x509_crt_t </b><i>issuer</i><b>, gnutls_privkey_t </b><i>issuer_key</i><b>, gnutls_digest_algorithm_t </b><i>dig</i><b>, unsigned int </b><i>flags</i><b>);</b>

<h2>ARGUMENTS</h2>

<dl>
<dt>gnutls_x509_crl_t crl
<dd> should contain a gnutls_x509_crl_t structure
<dt>gnutls_x509_crt_t issuer
<dd> is the certificate of the certificate issuer
<dt>gnutls_privkey_t issuer_key
<dd> holds the issuer's private key
<dt>gnutls_digest_algorithm_t dig
<dd> The message digest to use. GNUTLS_DIG_SHA1 is the safe choice unless you know what you're doing.
<dt>unsigned int flags
<dd> must be 0</dl>

<h2>DESCRIPTION</h2>

 This function will sign the CRL with the issuer's private key, and will copy the issuer's information into the CRL. 

 This must be the last step in a certificate CRL since all the previously set parameters are now signed.

<h2>RETURNS</h2>

 On success, <b>GNUTLS_E_SUCCESS</b> (0) is returned, otherwise a negative error value. 

 Since 2.12.0

<h2>REPORTING BUGS</h2>

 Report bugs to &lt;bugs [at] gnutls.org&gt;. 
 Home page: <a rel="nofollow" HREF="http://www.gnutls.org">http://www.gnutls.org</a> 

<h2>COPYRIGHT</h2>

 Copyright &#169; 2001-2014 Free Software Foundation, Inc.. 
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.

<h2>SEE ALSO</h2>

 The full documentation for <b>gnutls</b> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <b>
<dl>
<dt><a rel="nofollow" HREF="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a>
<dd> </b></dl>
 

 

<h2>Index</h2>


