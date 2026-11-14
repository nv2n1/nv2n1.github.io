---
title: "curlopt_chunk_data(3)"
name: "curlopt_chunk_data"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_chunk_data/"
description: "CURLOPT_CHUNK_DATA – custom pointer to the FTP chunk callbacks"
---

<p>CURLOPT_CHUNK_DATA &#8211; custom pointer to the FTP chunk callbacks</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CHUNK_DATA, void *pointer);</p>
<h2>Description</h2>
<p>Pass a <i>pointer</i> that will be untouched by libcurl and passed as the ptr argument to the <i><a href="/docs/linux/man/3-curl_chunk_bgn_funtion/">CURL_CHUNK_BGN_FUNTION</a>(3)</i> and <i><a href="/docs/linux/man/3-curl_chunk_end_funtion/">CURL_CHUNK_END_FUNTION</a>(3)</i>.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.21.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_chunk_bgn_function/">CURLOPT_CHUNK_BGN_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_wildcardmatch/">CURLOPT_WILDCARDMATCH</a></code>(3),</p>
