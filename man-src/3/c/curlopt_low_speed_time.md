---
title: "curlopt_low_speed_time(3)"
name: "curlopt_low_speed_time"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_low_speed_time/"
description: "CURLOPT_LOW_SPEED_TIME – set low speed limit time period"
---

<p>CURLOPT_LOW_SPEED_TIME &#8211; set low speed limit time period</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_LOW_SPEED_TIME, long speedtime);</p>
<h2>Description</h2>
<p>Pass a long as parameter. It contains the time in number seconds that the transfer speed should be below the <i><a href="/docs/linux/man/3-curlopt_low_speed_limit/">CURLOPT_LOW_SPEED_LIMIT</a>(3)</i> for the library to consider it too slow and abort.</p>
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
<p><code><a href="/docs/linux/man/3-curlopt_low_speed_limit/">CURLOPT_LOW_SPEED_LIMIT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_timeout/">CURLOPT_TIMEOUT</a></code>(3),</p>
