---
title: "curlopt_low_speed_limit(3)"
name: "curlopt_low_speed_limit"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_low_speed_limit/"
description: "CURLOPT_LOW_SPEED_LIMIT – set low speed limit in bytes per second"
---

<p>CURLOPT_LOW_SPEED_LIMIT &#8211; set low speed limit in bytes per second</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_LOW_SPEED_LIMIT, long speedlimit);</p>
<h2>Description</h2>
<p>Pass a long as parameter. It contains the average transfer speed in bytes per second that the transfer should be below during <i><a href="/docs/linux/man/3-curlopt_low_speed_time/">CURLOPT_LOW_SPEED_TIME</a>(3)</i> seconds for libcurl to consider it to be too slow and abort.</p>
<h2>Default</h2>
<p>0, disabled</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_low_speed_time/">CURLOPT_LOW_SPEED_TIME</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_timeout/">CURLOPT_TIMEOUT</a></code>(3),</p>
