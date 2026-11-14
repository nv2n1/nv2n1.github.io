---
title: "curlopt_chunk_bgn_function(3)"
name: "curlopt_chunk_bgn_function"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_chunk_bgn_function/"
description: "CURLOPT_CHUNK_BGN_FUNCTION – callback before a transfer with FTP wildcardmatch"
---

<p>CURLOPT_CHUNK_BGN_FUNCTION &#8211; callback before a transfer with FTP wildcardmatch</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
long chunk_bgn_callback(const void *transfer_info, void *ptr,
 int remains);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CHUNK_BGN_FUNCTION,
 chunk_bgn_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This callback function gets called by libcurl before a part of the stream is going to be transferred (if the transfer supports chunks). </p>
<p> The <i>transfer_info</i> pointer will point to a struct curl_fileinfo with details about the file that is about to get transferred. </p>
<p> This callback makes sense only when using the <i><a href="/docs/linux/man/3-curlopt_wildcardmatch/">CURLOPT_WILDCARDMATCH</a>(3)</i> option for now. </p>
<p> The target of transfer_info parameter is a &quot;feature depended&quot; structure. For the FTP wildcard download, the target is curl_fileinfo structure (see <i>curl/curl.h</i>). The parameter <i>ptr</i> is a pointer given by <i><a href="/docs/linux/man/3-curlopt_chunk_data/">CURLOPT_CHUNK_DATA</a>(3)</i>. The parameter remains contains number of chunks remaining per the transfer. If the feature is not available, the parameter has zero value. </p>
<p> Return <i>CURL_CHUNK_BGN_FUNC_OK</i> if everything is fine, <i>CURL_CHUNK_BGN_FUNC_SKIP</i> if you want to skip the concrete chunk or <i>CURL_CHUNK_BGN_FUNC_FAIL</i> to tell libcurl to stop if some error occurred.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>This was added in 7.21.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_chunk_end_function/">CURLOPT_CHUNK_END_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_wildcardmatch/">CURLOPT_WILDCARDMATCH</a></code>(3),</p>
