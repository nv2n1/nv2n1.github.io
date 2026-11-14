---
title: "curlopt_timevalue(3)"
name: "curlopt_timevalue"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_timevalue/"
description: "CURLOPT_TIMEVALUE – set time value for conditional"
---

<p>CURLOPT_TIMEVALUE &#8211; set time value for conditional</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TIMEVALUE, long val);</p>
<h2>Description</h2>
<p>Pass a long <i>val</i> as parameter. This should be the time counted as seconds since 1 Jan 1970, and the time will be used in a condition as specified with <i><a href="/docs/linux/man/3-curlopt_timecondition/">CURLOPT_TIMECONDITION</a>(3)</i>.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>HTTP, FTP, RTSP, and FILE</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_timecondition/">CURLOPT_TIMECONDITION</a></code>(3),</p>
