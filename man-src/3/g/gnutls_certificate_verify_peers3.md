---
title: "gnutls_certificate_verify_peers3(3)"
name: "gnutls_certificate_verify_peers3"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_verify_peers3/"
description: "gnutls_certificate_verify_peers3 – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_verify_peers3 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_certificate_verify_peers3(gnutls_session_t </code><i>session</i><code>, const char * </code><i>hostname</i><code>, unsigned int * </code><i>status</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a gnutls session</p>
<dt>const char * hostname</p>
<dd> is the expected name of the peer; may be <code>NULL</code></p>
<dt>unsigned int * status</p>
<dd> is the output of the verification</dl>
<h2>DESCRIPTION</h2>
<p> This function will verify the peer&#8217;s certificate and store the status in the <i>status</i> variable as a bitwise or&#8217;d gnutls_certificate_status_t values or zero if the certificate is trusted. Note that value in <i>status</i> is set only when the return value of this function is success (i.e, failure to trust a certificate does not imply a negative return value). The default verification flags used by this function can be overridden using <code>gnutls_certificate_set_verify_flags()</code>. See the documentation of <code>gnutls_certificate_verify_peers2()</code> for details in the verification process. </p>
<p> If the <i>hostname</i> provided is non-NULL then this function will compare the hostname in the certificate against the given. The comparison will be accurate for ascii names; non-ascii names are compared byte-by-byte. If names do not match the <code>GNUTLS_CERT_UNEXPECTED_OWNER</code> status flag will be set. </p>
<p> In order to verify the purpose of the end-certificate (by checking the extended key usage), use <code>gnutls_certificate_verify_peers()</code>.</p>
<h2>RETURNS</h2>
<p> a negative error code on error and <code>GNUTLS_E_SUCCESS</code> (0) when the peer&#8217;s certificate was successfully parsed, irrespective of whether it was verified.</p>
<h2>SINCE</h2>
<p> 3.1.4</p>
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
