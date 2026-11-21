---
title: "gnutls_ocsp_resp_verify(3)"
name: "gnutls_ocsp_resp_verify"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_resp_verify/"
---
<p> gnutls_ocsp_resp_verify - API function  </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_resp_verify(gnutls_ocsp_resp_t </code><i>resp</i><code>, gnutls_x509_trust_list_t </code><i>trustlist</i><code>, unsigned int * </code><i>verify</i><code>, unsigned int </code><i>flags</i><code>);</code>  </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_resp_t resp</dt>
<dd> <p> should contain a <code>gnutls_ocsp_resp_t</code> structure </p>
 </dd>
<dt>gnutls_x509_trust_list_t trustlist</dt>
<dd> <p> trust anchors as a <code>gnutls_x509_trust_list_t</code> structure </p>
 </dd>
<dt>unsigned int * verify</dt>
<dd> <p> output variable with verification status, an <code>gnutls_ocsp_cert_status_t</code> </p>
 </dd>
<dt>unsigned int flags</dt>
<dd> <p> verification flags, 0 for now. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> Verify signature of the Basic OCSP Response against the public key in the certificate of a trusted signer. The <i>trustlist</i> should be populated with trust anchors. The function will extract the signer certificate from the Basic OCSP Response and will verify it against the <i>trustlist</i> . A trusted signer is a certificate that is either in <i>trustlist</i> , or it is signed directly by a certificate in <br />
&nbsp;<wbr><i>trustlist</i>&nbsp;<wbr>and has the id-ad-ocspSigning Extended Key Usage bit set. </p>
<p>The output <i>verify</i> variable will hold verification status codes (e.g., <code>GNUTLS_OCSP_VERIFY_SIGNER_NOT_FOUND</code>, <code>GNUTLS_OCSP_VERIFY_INSECURE_ALGORITHM</code>) which are only valid if the function returned <code>GNUTLS_E_SUCCESS</code>. </p>
<p>Note that the function returns <code>GNUTLS_E_SUCCESS</code> even when verification failed. The caller must always inspect the <i>verify</i> variable to find out the verification status. </p>
<p>The <i>flags</i> variable should be 0 for now.  </p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.  </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;. <br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc.. <br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.  </p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code> </p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> <p> </code> </p>
 </dd></dl>
