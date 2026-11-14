---
title: "curlopt_crlfile(3)"
name: "curlopt_crlfile"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_crlfile/"
description: "CURLOPT_CRLFILE – specify a Certificate Revocation List file"
---

<p>CURLOPT_CRLFILE &#8211; specify a Certificate Revocation List file</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CRLFILE, char *file);</p>
<h2>Description</h2>
<p>Pass a char * to a zero terminated string naming a <i>file</i> with the concatenation of CRL (in PEM format) to use in the certificate validation that occurs during the SSL exchange. </p>
<p> When curl is built to use NSS or GnuTLS, there is no way to influence the use of CRL passed to help in the verification process. When libcurl is built with OpenSSL support, X509_V_FLAG_CRL_CHECK and X509_V_FLAG_CRL_CHECK_ALL are both set, requiring CRL check against all the elements of the certificate chain if a CRL file is passed. </p>
<p> This option makes sense only when used in combination with the <i><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a>(3)</i> option. </p>
<p> A specific error code (<i>CURLE_SSL_CRL_BADFILE</i>) is defined with the option. It is returned when the SSL exchange fails because the CRL file cannot be loaded. A failure in certificate verification due to a revocation information found in the CRL does not trigger this specific error.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS-based protocols</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssl_verifyhost/">CURLOPT_SSL_VERIFYHOST</a></code>(3),</p>
