---
title: "gnutls_certificate_verify_peers(3)"
name: "gnutls_certificate_verify_peers"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_verify_peers/"
description: "gnutls_certificate_verify_peers – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_verify_peers &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_certificate_verify_peers(gnutls_session_t </code><i>session</i><code>, gnutls_typed_vdata_st * </code><i>data</i><code>, unsigned int </code><i>elements</i><code>, unsigned int * </code><i>status</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a gnutls session</p>
<dt>gnutls_typed_vdata_st * data</p>
<dd> an array of typed data</p>
<dt>unsigned int elements</p>
<dd> the number of data elements</p>
<dt>unsigned int * status</p>
<dd> is the output of the verification</dl>
<h2>DESCRIPTION</h2>
<p> This function will verify the peer&#8217;s certificate and store the status in the <i>status</i> variable as a bitwise or&#8217;d gnutls_certificate_status_t values or zero if the certificate is trusted. Note that value in <i>status</i> is set only when the return value of this function is success (i.e, failure to trust a certificate does not imply a negative return value). The default verification flags used by this function can be overridden using <code>gnutls_certificate_set_verify_flags()</code>. See the documentation of <code>gnutls_certificate_verify_peers2()</code> for details in the verification process. </p>
<p> The acceptable <i>data</i> types are <code>GNUTLS_DT_DNS_HOSTNAME</code> and <code>GNUTLS_DT_KEY_PURPOSE_OID</code>. The former accepts as data a null-terminated hostname, and the latter a null-terminated object identifier (e.g., <code>GNUTLS_KP_TLS_WWW_SERVER</code>). If a DNS hostname is provided then this function will compare the hostname in the certificate against the given. If names do not match the <code>GNUTLS_CERT_UNEXPECTED_OWNER</code> status flag will be set. If a key purpose OID is provided and the end-certificate contains the extended key usage PKIX extension, it will be required to be have the provided key purpose or be marked for any purpose, otherwise verification will fail with <code>GNUTLS_CERT_SIGNER_CONSTRAINTS_FAILURE</code> status.</p>
<h2>RETURNS</h2>
<p> a negative error code on error and <code>GNUTLS_E_SUCCESS</code> (0) when the peer&#8217;s certificate was successfully parsed, irrespective of whether it was verified.</p>
<h2>SINCE</h2>
<p> 3.3.0</p>
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
