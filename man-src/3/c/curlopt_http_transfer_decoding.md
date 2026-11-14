---
title: "curlopt_http_transfer_decoding(3)"
name: "curlopt_http_transfer_decoding"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_http_transfer_decoding/"
description: "CURLOPT_HTTP_TRANSFER_DECODING – enable/disable HTTP transfer decoding"
---

<p>CURLOPT_HTTP_TRANSFER_DECODING &#8211; enable/disable HTTP transfer decoding</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HTTP_TRANSFER_DECODING,
 long enabled);</pre>
<h2>Description</h2>
<p>Pass a long to tell libcurl how to act on transfer decoding. If set to zero, transfer decoding will be disabled, if set to 1 it is enabled (default). libcurl does chunked transfer decoding by default unless this option is set to zero.</p>
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
<p><code><a href="/docs/linux/man/3-curlopt_http_content_decoding/">CURLOPT_HTTP_CONTENT_DECODING</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_accept_encoding/">CURLOPT_ACCEPT_ENCODING</a></code>(3),</p>
