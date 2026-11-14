---
title: "curlopt_tcp_keepidle(3)"
name: "curlopt_tcp_keepidle"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_tcp_keepidle/"
description: "CURLOPT_TCP_KEEPIDLE – set TCP keep-alive idle time wait"
---

<p>CURLOPT_TCP_KEEPIDLE &#8211; set TCP keep-alive idle time wait</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TCP_KEEPIDLE, long delay);</p>
<h2>Description</h2>
<p>Pass a long. Sets the <i>delay</i>, in seconds, that the operating system will wait while the connection is idle before sending keepalive probes. Not all operating systems support this option.</p>
<h2>Default</h2>
<p>?</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.25.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_tcp_keepalive/">CURLOPT_TCP_KEEPALIVE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_tcp_keepintvl/">CURLOPT_TCP_KEEPINTVL</a></code>(3),</p>
