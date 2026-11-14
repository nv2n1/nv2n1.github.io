---
title: "curlopt_ssl_ctx_data(3)"
name: "curlopt_ssl_ctx_data"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssl_ctx_data/"
description: "CURLOPT_SSL_CTX_DATA – custom pointer passed to ssl_ctx callback"
---

<p>CURLOPT_SSL_CTX_DATA &#8211; custom pointer passed to ssl_ctx callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSL_CTX_DATA, void *pointer);</p>
<h2>Description</h2>
<p>Data <i>pointer</i> to pass to the ssl context callback set by the option <i><a href="/docs/linux/man/3-curlopt_ssl_ctx_function/">CURLOPT_SSL_CTX_FUNCTION</a>(3)</i>, this is the pointer you&#8217;ll get as third parameter.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.11.0. Only used with the OpenSSL backend.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssl_ctx_function/">CURLOPT_SSL_CTX_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_sslversion/">CURLOPT_SSLVERSION</a></code>(3),</p>
