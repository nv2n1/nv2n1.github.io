---
title: "curlopt_ssl_enable_npn(3)"
name: "curlopt_ssl_enable_npn"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssl_enable_npn/"
description: "CURLOPT_SSL_ENABLE_NPN – enable NPN"
---

<p>CURLOPT_SSL_ENABLE_NPN &#8211; enable NPN</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSL_ENABLE_NPN, long npn);</p>
<h2>Description</h2>
<p>Pass a long as parameter, 0 or 1 where 1 is for enable and 0 for disable. This option enables/disables NPN in the SSL handshake (if the SSL backend libcurl is built to use supports it), which can be used to negotiate http2.</p>
<h2>Default</h2>
<p>1, enabled</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.36.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssl_enable_alpn/">CURLOPT_SSL_ENABLE_ALPN</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssl_options/">CURLOPT_SSL_OPTIONS</a></code>(3),</p>
