---
title: "curlopt_crlf(3)"
name: "curlopt_crlf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_crlf/"
description: "CURLOPT_CRLF – enable/disable CRLF conversion"
---

<p>CURLOPT_CRLF &#8211; enable/disable CRLF conversion</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CRLF, long conv);</p>
<h2>Description</h2>
<p>Pass a long. If the value is set to 1 (one), libcurl converts Unix newlines to CRLF newlines on transfers. Disable this option again by setting the value to 0 (zero). </p>
<p> This is a legacy option of questionable use.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>SMTP since 7.40.0, other protocols since they were introduced</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_conv_from_network_function/">CURLOPT_CONV_FROM_NETWORK_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_conv_to_network_function/">CURLOPT_CONV_TO_NETWORK_FUNCTION</a></code>(3),</p>
