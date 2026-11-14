---
title: "curlopt_expect_100_timeout_ms(3)"
name: "curlopt_expect_100_timeout_ms"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_expect_100_timeout_ms/"
description: "CURLOPT_EXPECT_100_TIMEOUT_MS – timeout for Expect: 100-continue response"
---

<p>CURLOPT_EXPECT_100_TIMEOUT_MS &#8211; timeout for Expect: 100-continue response</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_EXPECT_100_TIMEOUT_MS,
 long milliseconds);</pre>
<h2>Description</h2>
<p>Pass a long to tell libcurl the number of <i>milliseconds</i> to wait for a server response with the HTTP status 100 (Continue), 417 (Expectation Failed) or similar after sending a HTTP request containing an Expect: 100-continue header. If this times out before a response is received, the request body is sent anyway.</p>
<h2>Default</h2>
<p>1000 milliseconds</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.36.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_post/">CURLOPT_POST</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httppost/">CURLOPT_HTTPPOST</a></code>(3),</p>
