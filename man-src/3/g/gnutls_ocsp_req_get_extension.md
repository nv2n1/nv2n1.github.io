---
title: "gnutls_ocsp_req_get_extension(3)"
name: "gnutls_ocsp_req_get_extension"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_req_get_extension/"
description: "gnutls_ocsp_req_get_extension – API function"
---

<h2>NAME</h2>
<p> gnutls_ocsp_req_get_extension &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_req_get_extension(gnutls_ocsp_req_t </code><i>req</i><code>, unsigned </code><i>indx</i><code>, gnutls_datum_t * </code><i>oid</i><code>, unsigned int * </code><i>critical</i><code>, gnutls_datum_t * </code><i>data</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_req_t req</p>
<dd> should contain a <code>gnutls_ocsp_req_t</code> structure</p>
<dt>unsigned indx</p>
<dd> Specifies which extension OID to get. Use (0) to get the first one.</p>
<dt>gnutls_datum_t * oid</p>
<dd> will hold newly allocated buffer with OID of extension, may be NULL</p>
<dt>unsigned int * critical</p>
<dd> output variable with critical flag, may be NULL.</p>
<dt>gnutls_datum_t * data</p>
<dd> will hold newly allocated buffer with extension data, may be NULL</dl>
<h2>DESCRIPTION</h2>
<p> This function will return all information about the requested extension in the OCSP request. The information returned is the OID, the critical flag, and the data itself. The extension OID will be stored as a string. Any of <i>oid</i> , <i>critical</i> , and <i>data</i> may be NULL which means that the caller is not interested in getting that information back. </p>
<p> The caller needs to deallocate memory by calling <code>gnutls_free()</code> on<br />
&nbsp;<wbr><i>oid</i>&nbsp;<wbr>-&gt;data and&nbsp;<wbr>&nbsp;<wbr><i>data</i>&nbsp;<wbr>-&gt;data.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned. If you have reached the last extension available <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> will be returned.</p>
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
