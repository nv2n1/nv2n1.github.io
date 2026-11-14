---
title: "gnutls_ocsp_resp_get_version(3)"
name: "gnutls_ocsp_resp_get_version"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_resp_get_version/"
---

<h2>NAME</h2>

 gnutls_ocsp_resp_get_version - API function

<h2>SYNOPSIS</h2>

 <b>#include &lt;gnutls/ocsp.h&gt;</b> 

 <b>int gnutls_ocsp_resp_get_version(gnutls_ocsp_resp_t </b><i>resp</i><b>);</b>

<h2>ARGUMENTS</h2>

<dl>
<dt>gnutls_ocsp_resp_t resp
<dd> should contain a <b>gnutls_ocsp_resp_t</b> structure</dl>

<h2>DESCRIPTION</h2>

 This function will return the version of the Basic OCSP Response. Typically this is always 1 indicating version 1.

<h2>RETURNS</h2>

 version of Basic OCSP response, or a negative error code on error.

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


