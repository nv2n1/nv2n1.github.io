---
title: "curlopt_http_content_decoding(3)"
name: "curlopt_http_content_decoding"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_http_content_decoding/"
description: "CURLOPT_HTTP_CONTENT_DECODING – enable/disable HTTP content decoding"
---

<p>CURLOPT_HTTP_CONTENT_DECODING &#8211; enable/disable HTTP content decoding</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HTTP_CONTENT_DECODING,
 long enabled);</pre>
<h2>Description</h2>
<p>Pass a long to tell libcurl how to act on content decoding. If set to zero, content decoding will be disabled. If set to 1 it is enabled. Libcurl has no default content decoding but requires you to use <i><a href="/docs/linux/man/3-curlopt_accept_encoding/">CURLOPT_ACCEPT_ENCODING</a>(3)</i> for that.</p>
<h2>Default</h2>
<p>1</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.16.2</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_stderr/">CURLOPT_STDERR</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_accept_encoding/">CURLOPT_ACCEPT_ENCODING</a></code>(3)</p>
