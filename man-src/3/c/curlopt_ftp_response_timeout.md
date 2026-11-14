---
title: "curlopt_ftp_response_timeout(3)"
name: "curlopt_ftp_response_timeout"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftp_response_timeout/"
description: "CURLOPT_FTP_RESPONSE_TIMEOUT – time allowed to wait for FTP response"
---

<p>CURLOPT_FTP_RESPONSE_TIMEOUT &#8211; time allowed to wait for FTP response</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTP_RESPONSE_TIMEOUT, long timeout);</p>
<h2>Description</h2>
<p>Pass a long. Causes libcurl to set a <i>timeout</i> period (in seconds) on the amount of time that the server is allowed to take in order to send a response message for a command before the session is considered dead. While libcurl is waiting for a response, this value overrides <i><a href="/docs/linux/man/3-curlopt_timeout/">CURLOPT_TIMEOUT</a>(3)</i>. It is recommended that if used in conjunction with <i><a href="/docs/linux/man/3-curlopt_timeout/">CURLOPT_TIMEOUT</a>(3)</i>, you set <i><a href="/docs/linux/man/3-curlopt_ftp_response_timeout/">CURLOPT_FTP_RESPONSE_TIMEOUT</a>(3)</i> to a value smaller than <i><a href="/docs/linux/man/3-curlopt_timeout/">CURLOPT_TIMEOUT</a>(3)</i>.</p>
<h2>Default</h2>
<p>None</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.10.8</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if FTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_timeout/">CURLOPT_TIMEOUT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_connecttimeout/">CURLOPT_CONNECTTIMEOUT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_low_speed_limit/">CURLOPT_LOW_SPEED_LIMIT</a></code>(3),</p>
