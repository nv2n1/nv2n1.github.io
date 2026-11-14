---
title: "curlopt_tcp_keepintvl(3)"
name: "curlopt_tcp_keepintvl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_tcp_keepintvl/"
description: "CURLOPT_TCP_KEEPINTVL – set TCP keep-alive interval"
---

<p>CURLOPT_TCP_KEEPINTVL &#8211; set TCP keep-alive interval</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TCP_KEEPINTVL, long interval);</p>
<h2>Description</h2>
<p>Pass a long. Sets the interval, in seconds, that the operating system will wait between sending keepalive probes. Not all operating systems support this option. (Added in 7.25.0)</p>
<h2>Default</h2>
<h2>Protocols</h2>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_tcp_keepalive/">CURLOPT_TCP_KEEPALIVE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_tcp_keepidle/">CURLOPT_TCP_KEEPIDLE</a></code>(3),</p>
