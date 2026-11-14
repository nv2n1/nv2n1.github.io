---
title: "gnutls_pkcs7_delete_crt(3)"
name: "gnutls_pkcs7_delete_crt"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs7_delete_crt/"
---

<h2>NAME</h2>

 gnutls_pkcs7_delete_crt - API function

<h2>SYNOPSIS</h2>

 <b>#include &lt;gnutls/x509.h&gt;</b> 

 <b>int gnutls_pkcs7_delete_crt(gnutls_pkcs7_t </b><i>pkcs7</i><b>, int </b><i>indx</i><b>);</b>

<h2>ARGUMENTS</h2>

<dl>
<dt>gnutls_pkcs7_t pkcs7
<dd> should contain a gnutls_pkcs7_t structure
<dt>int indx
<dd> the index of the certificate to delete</dl>

<h2>DESCRIPTION</h2>

 This function will delete a certificate from a PKCS7 or RFC2630 certificate set. Index starts from 0. Returns 0 on success.

<h2>RETURNS</h2>

 On success, <b>GNUTLS_E_SUCCESS</b> (0) is returned, otherwise a negative error value.

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


