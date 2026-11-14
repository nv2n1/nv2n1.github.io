---
title: "gnutls_x509_crt_get_extension_info(3)"
name: "gnutls_x509_crt_get_extension_info"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_extension_info/"
description: "gnutls_x509_crt_get_extension_info – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_extension_info &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_extension_info(gnutls_x509_crt_t </code><i>cert</i><code>, int </code><i>indx</i><code>, void * </code><i>oid</i><code>, size_t * </code><i>oid_size</i><code>, unsigned int * </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</p>
<dt>int indx</p>
<dd> Specifies which extension OID to send. Use (0) to get the first one.</p>
<dt>void * oid</p>
<dd> a pointer to a structure to hold the OID</p>
<dt>size_t * oid_size</p>
<dd> initially holds the maximum size of <i>oid</i> , on return holds actual size of <i>oid</i> .</p>
<dt>unsigned int * critical</p>
<dd> output variable with critical flag, may be NULL.</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the requested extension OID in the certificate, and the critical flag for it. The extension OID will be stored as a string in the provided buffer. Use <code>gnutls_x509_crt_get_extension()</code> to extract the data. </p>
<p> If the buffer provided is not long enough to hold the output, then<br />
&nbsp;<wbr><i>oid_size</i>&nbsp;<wbr>is updated and&nbsp;<wbr><code>GNUTLS_E_SHORT_MEMORY_BUFFER</code>&nbsp;<wbr>will be returned. The <i>oid</i> returned will be null terminated, although<br />
&nbsp;<wbr><i>oid_size</i>&nbsp;<wbr>will not account for the trailing null.</p>
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
