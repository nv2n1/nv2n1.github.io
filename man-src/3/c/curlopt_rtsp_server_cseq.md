---
title: "curlopt_rtsp_server_cseq(3)"
name: "curlopt_rtsp_server_cseq"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_rtsp_server_cseq/"
description: "CURLOPT_RTSP_SERVER_CSEQ – set the RTSP server CSEQ number"
---

<p>CURLOPT_RTSP_SERVER_CSEQ &#8211; set the RTSP server CSEQ number</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_RTSP_SERVER_CSEQ, long cseq);</p>
<h2>Description</h2>
<p>Pass a long to set the CSEQ number to expect for the next RTSP Server-&gt;Client request. <code>NOTE</code>: this feature (listening for Server requests) is unimplemented.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>RTSP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.20.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_rtsp_client_cseq/">CURLOPT_RTSP_CLIENT_CSEQ</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_rtsp_stream_uri/">CURLOPT_RTSP_STREAM_URI</a></code>(3),</p>
