---
title: "curlopt_issuercert(3)"
name: "curlopt_issuercert"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_issuercert/"
description: "CURLOPT_ISSUERCERT – issuer SSL certificate filename"
---

<p>CURLOPT_ISSUERCERT &#8211; issuer SSL certificate filename</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_ISSUERCERT, char *file);</p>
<h2>Description</h2>
<p>Pass a char * to a zero terminated string naming a <i>file</i> holding a CA certificate in PEM format. If the option is set, an additional check against the peer certificate is performed to verify the issuer is indeed the one associated with the certificate provided by the option. This additional check is useful in multi-level PKI where one needs to enforce that the peer certificate is from a specific branch of the tree. </p>
<p> This option makes sense only when used in combination with the <i><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a>(3)</i> option. Otherwise, the result of the check is not considered as failure. </p>
<p> A specific error code (CURLE_SSL_ISSUER_ERROR) is defined with the option, which is returned if the setup of the SSL/TLS session has failed due to a mismatch with the issuer of peer certificate (<i><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a>(3)</i> has to be set too for the check to fail). (Added in 7.19.0)</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS-based protocols</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built TLS enabled</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_crlfile/">CURLOPT_CRLFILE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a></code>(3),</p>
