---
title: "curlopt_interleavedata(3)"
name: "curlopt_interleavedata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_interleavedata/"
description: "CURLOPT_INTERLEAVEDATA – custom pointer to RTSP interleave callback"
---

<p>CURLOPT_INTERLEAVEDATA &#8211; custom pointer to RTSP interleave callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_INTERLEAVEDATA, void *pointer);</p>
<h2>Description</h2>
<p>This is the userdata <i>pointer</i> that will be passed to <i><a href="/docs/linux/man/3-curlopt_interleavefunction/">CURLOPT_INTERLEAVEFUNCTION</a>(3)</i> when interleaved RTP data is received.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>RTSP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.20.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_interleavefunction/">CURLOPT_INTERLEAVEFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_rtsp_request/">CURLOPT_RTSP_REQUEST</a></code>(3),</p>
