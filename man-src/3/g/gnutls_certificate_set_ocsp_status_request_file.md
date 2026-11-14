---
title: "gnutls_certificate_set_ocsp_status_request_file(3)"
name: "gnutls_certificate_set_ocsp_status_request_file"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_ocsp_status_request_file/"
description: "gnutls_certificate_set_ocsp_status_request_file – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_ocsp_status_request_file &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_certificate_set_ocsp_status_request_file(gnutls_certificate_credentials_t </code><i>sc</i><code>, const char * </code><i>response_file</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t sc</p>
<dd> is a credentials structure.</p>
<dt>const char * response_file</p>
<dd> a filename of the OCSP response</p>
<dt>unsigned int flags</p>
<dd> should be zero</dl>
<h2>DESCRIPTION</h2>
<p> This function sets the filename of an OCSP response, that will be sent to the client if requests an OCSP certificate status. This is a convenience function which is inefficient on busy servers since the file is opened on every access. Use <code>gnutls_certificate_set_ocsp_status_request_function()</code> to fine-tune file accesses.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
<h2>SINCE</h2>
<p> 3.1.3</p>
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
