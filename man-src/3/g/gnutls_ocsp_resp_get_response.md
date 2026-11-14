---
title: "gnutls_ocsp_resp_get_response(3)"
name: "gnutls_ocsp_resp_get_response"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_resp_get_response/"
---

<h2>NAME</h2>

 gnutls_ocsp_resp_get_response - API function

<h2>SYNOPSIS</h2>

 <b>#include &lt;gnutls/ocsp.h&gt;</b> 

 <b>int gnutls_ocsp_resp_get_response(gnutls_ocsp_resp_t </b><i>resp</i><b>, gnutls_datum_t * </b><i>response_type_oid</i><b>, gnutls_datum_t * </b><i>response</i><b>);</b>

<h2>ARGUMENTS</h2>

<dl>
<dt>gnutls_ocsp_resp_t resp
<dd> should contain a <b>gnutls_ocsp_resp_t</b> structure
<dt>gnutls_datum_t * response_type_oid
<dd> newly allocated output buffer with response type OID
<dt>gnutls_datum_t * response
<dd> newly allocated output buffer with DER encoded response</dl>

<h2>DESCRIPTION</h2>

 This function will extract the response type OID in and the response data from an OCSP response. Normally the 
&nbsp;<wbr><i>response_type_oid</i>&nbsp;<wbr>is always&nbsp;<wbr>&quot;1.3.6.1.5.5.7.48.1.1&quot;&nbsp;<wbr>which means the 
&nbsp;<wbr><i>response</i>&nbsp;<wbr>should be decoded as a Basic OCSP Response, but technically other response types could be used. 

 This function is typically only useful when you want to extract the response type OID of an response for diagnostic purposes. Otherwise <b>gnutls_ocsp_resp_import()</b> will decode the basic OCSP response part and the caller need not worry about that aspect.

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


