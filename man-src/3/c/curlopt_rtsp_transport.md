---
title: "curlopt_rtsp_transport(3)"
name: "curlopt_rtsp_transport"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_rtsp_transport/"
description: "CURLOPT_RTSP_TRANSPORT – set RTSP Transport: header"
---

<p>CURLOPT_RTSP_TRANSPORT &#8211; set RTSP Transport: header</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_RTSP_TRANSPORT,
 char *transport);</pre>
<h2>Description</h2>
<p>Pass a char * to tell libcurl what to pass for the Transport: header for this RTSP session. This is mainly a convenience method to avoid needing to set a custom Transport: header for every SETUP request. The application must set a Transport: header before issuing a SETUP request.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>RTSP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.20.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_rtsp_request/">CURLOPT_RTSP_REQUEST</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_rtsp_session_id/">CURLOPT_RTSP_SESSION_ID</a></code>(3),</p>
