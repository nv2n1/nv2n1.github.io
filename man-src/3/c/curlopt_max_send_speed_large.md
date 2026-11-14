---
title: "curlopt_max_send_speed_large(3)"
name: "curlopt_max_send_speed_large"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_max_send_speed_large/"
description: "CURLOPT_MAX_SEND_SPEED_LARGE – rate limit data upload speed"
---

<p>CURLOPT_MAX_SEND_SPEED_LARGE &#8211; rate limit data upload speed</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_MAX_SEND_SPEED_LARGE,
 curl_off_t maxspeed);</pre>
<h2>Description</h2>
<p>Pass a curl_off_t as parameter with the <i>maxspeed</i>. If an upload exceeds this speed (counted in bytes per second) on cumulative average during the transfer, the transfer will pause to keep the average rate less than or equal to the parameter value. Defaults to unlimited speed. </p>
<p> This option doesn&#8217;t affect transfer speeds done with FILE:// URLs.</p>
<h2>Default</h2>
<p>0, disabled</p>
<h2>Protocols</h2>
<p>All except file://</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.15.5</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_max_recv_speed_large/">CURLOPT_MAX_RECV_SPEED_LARGE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_low_speed_limit/">CURLOPT_LOW_SPEED_LIMIT</a></code>(3),</p>
