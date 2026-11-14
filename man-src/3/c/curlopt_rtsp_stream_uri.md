---
title: "curlopt_rtsp_stream_uri(3)"
name: "curlopt_rtsp_stream_uri"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_rtsp_stream_uri/"
description: "CURLOPT_RTSP_STREAM_URI – set RTSP stream URI"
---

<p>CURLOPT_RTSP_STREAM_URI &#8211; set RTSP stream URI</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_RTSP_STREAM_URI, char *URI);</p>
<h2>Description</h2>
<p>Set the stream <i>URI</i> to operate on by passing a char * . For example, a single session may be controlling <i><a href="rtsp://foo/twister/audio">rtsp://foo/twister/audio</a></i> and <i><a href="rtsp://foo/twister/video">rtsp://foo/twister/video</a></i> and the application can switch to the appropriate stream using this option. If unset, libcurl will default to operating on generic server options by passing &#8216;*&#8217; in the place of the RTSP Stream URI. This option is distinct from <i><a href="/docs/linux/man/3-curlopt_url/">CURLOPT_URL</a>(3)</i>. When working with RTSP, the <i><a href="/docs/linux/man/3-curlopt_stream_uri/">CURLOPT_STREAM_URI</a>(3)</i> indicates what URL to send to the server in the request header while the <i><a href="/docs/linux/man/3-curlopt_url/">CURLOPT_URL</a>(3)</i> indicates where to make the connection to. (e.g. the <i><a href="/docs/linux/man/3-curlopt_url/">CURLOPT_URL</a>(3)</i> for the above examples might be set to <i><a href="rtsp://foo/twister">rtsp://foo/twister</a></i></p>
<h2>Default</h2>
<h2>Protocols</h2>
<p>RTSP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.20.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_rtsp_request/">CURLOPT_RTSP_REQUEST</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_rtsp_transport/">CURLOPT_RTSP_TRANSPORT</a></code>(3),</p>
