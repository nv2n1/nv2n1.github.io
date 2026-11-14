---
title: "curlopt_tcp_keepalive(3)"
name: "curlopt_tcp_keepalive"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_tcp_keepalive/"
description: "CURLOPT_TCP_KEEPALIVE – enable TCP keep-alive probing"
---

<p>CURLOPT_TCP_KEEPALIVE &#8211; enable TCP keep-alive probing</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TCP_KEEPALIVE, long probe);</p>
<h2>Description</h2>
<p>Pass a long. If set to 1, TCP keepalive probes will be sent. The delay and frequency of these probes can be controlled by the <i><a href="/docs/linux/man/3-curlopt_tcp_keepidle/">CURLOPT_TCP_KEEPIDLE</a>(3)</i> and <i><a href="/docs/linux/man/3-curlopt_tcp_keepintvl/">CURLOPT_TCP_KEEPINTVL</a>(3)</i> options, provided the operating system supports them. Set to 0 (default behavior) to disable keepalive probes</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.25.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_tcp_keepidle/">CURLOPT_TCP_KEEPIDLE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_tcp_keepintvl/">CURLOPT_TCP_KEEPINTVL</a></code>(3),</p>
