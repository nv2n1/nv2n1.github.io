---
title: "gnutls_ocsp_resp_get_single(3)"
name: "gnutls_ocsp_resp_get_single"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_resp_get_single/"
description: "gnutls_ocsp_resp_get_single – API function"
---

<h2>NAME</h2>
<p> gnutls_ocsp_resp_get_single &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_resp_get_single(gnutls_ocsp_resp_t </code><i>resp</i><code>, unsigned </code><i>indx</i><code>, gnutls_digest_algorithm_t * </code><i>digest</i><code>, gnutls_datum_t * </code><i>issuer_name_hash</i><code>, gnutls_datum_t * </code><i>issuer_key_hash</i><code>, gnutls_datum_t * </code><i>serial_number</i><code>, unsigned int * </code><i>cert_status</i><code>, time_t * </code><i>this_update</i><code>, time_t * </code><i>next_update</i><code>, time_t * </code><i>revocation_time</i><code>, unsigned int * </code><i>revocation_reason</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_resp_t resp</p>
<dd> should contain a <code>gnutls_ocsp_resp_t</code> structure</p>
<dt>unsigned indx</p>
<dd> Specifies response number to get. Use (0) to get the first one.</p>
<dt>gnutls_digest_algorithm_t * digest</p>
<dd> output variable with <code>gnutls_digest_algorithm_t</code> hash algorithm</p>
<dt>gnutls_datum_t * issuer_name_hash</p>
<dd> output buffer with hash of issuer&#8217;s DN</p>
<dt>gnutls_datum_t * issuer_key_hash</p>
<dd> output buffer with hash of issuer&#8217;s public key</p>
<dt>gnutls_datum_t * serial_number</p>
<dd> output buffer with serial number of certificate to check</p>
<dt>unsigned int * cert_status</p>
<dd> a certificate status, a <code>gnutls_ocsp_cert_status_t</code> enum.</p>
<dt>time_t * this_update</p>
<dd> time at which the status is known to be correct.</p>
<dt>time_t * next_update</p>
<dd> when newer information will be available, or (time_t)-1 if unspecified</p>
<dt>time_t * revocation_time</p>
<dd> when <i>cert_status</i> is <code>GNUTLS_OCSP_CERT_REVOKED</code>, holds time of revocation.</p>
<dt>unsigned int * revocation_reason</p>
<dd> revocation reason, a <code>gnutls_x509_crl_reason_t</code> enum.</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the certificate information of the<br />
&nbsp;<wbr><i>indx</i>&nbsp;<wbr>&#8216;ed response in the Basic OCSP Response&nbsp;<wbr>&nbsp;<wbr><i>resp</i>&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>The information returned corresponds to the OCSP SingleResponse structure except the final singleExtensions. </p>
<p> Each of the pointers to output variables may be NULL to indicate that the caller is not interested in that value.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned. If you have reached the last CertID available <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> will be returned.</p>
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
