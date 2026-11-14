---
title: "curlopt_timecondition(3)"
name: "curlopt_timecondition"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_timecondition/"
description: "CURLOPT_TIMECONDITION – select condition for a time request"
---

<p>CURLOPT_TIMECONDITION &#8211; select condition for a time request</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TIMECONDITION, long cond);</p>
<h2>Description</h2>
<p>Pass a long as parameter. This defines how the <i><a href="/docs/linux/man/3-curlopt_timevalue/">CURLOPT_TIMEVALUE</a>(3)</i> time value is treated. You can set this parameter to <i>CURL_TIMECOND_IFMODSINCE</i> or <i>CURL_TIMECOND_IFUNMODSINCE</i>. </p>
<p> The last modification time of a file is not always known and in such instances this feature will have no effect even if the given time condition would not have been met. <i><a href="/docs/linux/man/3-curl_easy_getinfo/">curl_easy_getinfo</a>(3)</i> with the <i>CURLINFO_CONDITION_UNMET</i> option can be used after a transfer to learn if a zero-byte successful &quot;transfer&quot; was due to this condition not matching.</p>
<h2>Default</h2>
<p>CURL_TIMECOND_NONE (0)</p>
<h2>Protocols</h2>
<p>HTTP, FTP, RTSP, and FILE</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_timevalue/">CURLOPT_TIMEVALUE</a></code>(3),</p>
