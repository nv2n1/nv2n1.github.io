---
title: "curlopt_chunk_end_function(3)"
name: "curlopt_chunk_end_function"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_chunk_end_function/"
description: "CURLOPT_CHUNK_END_FUNCTION – callback after a transfer with FTP wildcardmatch"
---

<p>CURLOPT_CHUNK_END_FUNCTION &#8211; callback after a transfer with FTP wildcardmatch</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
long chunk_end_callback(void *ptr);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CHUNK_END_FUNCTION,
 chunk_end_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This function gets called by libcurl as soon as a part of the stream has been transferred (or skipped). </p>
<p> Return <i>CURL_CHUNK_END_FUNC_OK</i> if everything is fine or <code>CURL_CHUNK_END_FUNC_FAIL</code> to tell the lib to stop if some error occurred.</p>
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
<p><code><a href="/docs/linux/man/3-curlopt_wildcardmatch/">CURLOPT_WILDCARDMATCH</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_chunk_bgn_function/">CURLOPT_CHUNK_BGN_FUNCTION</a></code>(3),</p>
