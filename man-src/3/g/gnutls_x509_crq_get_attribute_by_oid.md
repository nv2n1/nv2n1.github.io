---
title: "gnutls_x509_crq_get_attribute_by_oid(3)"
name: "gnutls_x509_crq_get_attribute_by_oid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_get_attribute_by_oid/"
---

<h2>NAME</h2>

 gnutls_x509_crq_get_attribute_by_oid - API function

<h2>SYNOPSIS</h2>

 <b>#include &lt;gnutls/x509.h&gt;</b> 

 <b>int gnutls_x509_crq_get_attribute_by_oid(gnutls_x509_crq_t </b><i>crq</i><b>, const char * </b><i>oid</i><b>, int </b><i>indx</i><b>, void * </b><i>buf</i><b>, size_t * </b><i>buf_size</i><b>);</b>

<h2>ARGUMENTS</h2>

<dl>
<dt>gnutls_x509_crq_t crq
<dd> should contain a <b>gnutls_x509_crq_t</b> structure
<dt>const char * oid
<dd> holds an Object Identifier in null-terminated string
<dt>int indx
<dd> In case multiple same OIDs exist in the attribute list, this specifies which to get, use (0) to get the first one
<dt>void * buf
<dd> a pointer to a structure to hold the attribute data (may be <b>NULL</b>)
<dt>size_t * buf_size
<dd> initially holds the size of <i>buf</i></dl>

<h2>DESCRIPTION</h2>

 This function will return the attribute in the certificate request specified by the given Object ID. The attribute will be DER encoded. 

 Attributes in a certificate request is an optional set of data appended to the request. Their interpretation depends on the CA policy.

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


