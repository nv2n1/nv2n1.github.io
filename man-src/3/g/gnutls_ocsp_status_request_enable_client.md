---
title: "gnutls_ocsp_status_request_enable_client(3)"
name: "gnutls_ocsp_status_request_enable_client"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_status_request_enable_client/"
---

<h2>NAME</h2>

 gnutls_ocsp_status_request_enable_client - API function

<h2>SYNOPSIS</h2>

 <b>#include &lt;gnutls/gnutls.h&gt;</b> 

 <b>int gnutls_ocsp_status_request_enable_client(gnutls_session_t </b><i>session</i><b>, gnutls_datum_t * </b><i>responder_id</i><b>, size_t </b><i>responder_id_size</i><b>, gnutls_datum_t * </b><i>extensions</i><b>);</b>

<h2>ARGUMENTS</h2>

<dl>
<dt>gnutls_session_t session
<dd> is a <b>gnutls_session_t</b> structure.
<dt>gnutls_datum_t * responder_id
<dd> array with <b>gnutls_datum_t</b> with DER data of responder id
<dt>size_t responder_id_size
<dd> number of members in <i>responder_id</i> array
<dt>gnutls_datum_t * extensions
<dd> a <b>gnutls_datum_t</b> with DER encoded OCSP extensions</dl>

<h2>DESCRIPTION</h2>

 This function is to be used by clients to request OCSP response from the server, using the &quot;status_request&quot; TLS extension. Only OCSP status type is supported. A typical server has a single OCSP response cached, so <i>responder_id</i> and <i>extensions</i> should be null.

<h2>RETURNS</h2>

 On success, <b>GNUTLS_E_SUCCESS</b> (0) is returned, otherwise a negative error code is returned.

<h2>SINCE</h2>

 3.1.3

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


