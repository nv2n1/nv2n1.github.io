---
title: "curlopt_rtsp_session_id(3)"
name: "curlopt_rtsp_session_id"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_rtsp_session_id/"
description: "CURLOPT_RTSP_SESSION_ID – set RTSP session ID"
---

<p>CURLOPT_RTSP_SESSION_ID &#8211; set RTSP session ID</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_RTSP_SESSION_ID, char *id);</p>
<h2>Description</h2>
<p>Pass a char * as a parameter to set the value of the current RTSP Session ID for the handle. Useful for resuming an in-progress session. Once this value is set to any non-NULL value, libcurl will return <i>CURLE_RTSP_SESSION_ERROR</i> if ID received from the server does not match. If unset (or set to NULL), libcurl will automatically set the ID the first time the server sets it in a response.</p>
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
<p><code><a href="/docs/linux/man/3-curlopt_rtsp_request/">CURLOPT_RTSP_REQUEST</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_rtsp_stream_uri/">CURLOPT_RTSP_STREAM_URI</a></code>(3),</p>
