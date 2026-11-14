---
title: "curlopt_forbid_reuse(3)"
name: "curlopt_forbid_reuse"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_forbid_reuse/"
description: "CURLOPT_FORBID_REUSE – make connection get closed at once after use"
---

<p>CURLOPT_FORBID_REUSE &#8211; make connection get closed at once after use</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FORBID_REUSE, long close);</p>
<h2>Description</h2>
<p>Pass a long. Set <i>close</i> to 1 to make libcurl explicitly close the connection when done with the transfer. Normally, libcurl keeps all connections alive when done with one transfer in case a succeeding one follows that can re-use them. This option should be used with caution and only if you understand what it does as it can seriously impact performance. </p>
<p> Set to 0 to have libcurl keep the connection open for possible later re-use (default behavior).</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_fresh_connect/">CURLOPT_FRESH_CONNECT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_maxconnects/">CURLOPT_MAXCONNECTS</a></code>(3),</p>
