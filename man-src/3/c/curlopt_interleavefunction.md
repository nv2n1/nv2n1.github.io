---
title: "curlopt_interleavefunction(3)"
name: "curlopt_interleavefunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_interleavefunction/"
description: "CURLOPT_INTERLEAVEFUNCTION – callback function for RTSP interleaved data"
---

<p>CURLOPT_INTERLEAVEFUNCTION &#8211; callback function for RTSP interleaved data</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
size_t interleave_callback(void *ptr, size_t size, size_t nmemb,
 void *userdata);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_INTERLEAVEFUNCTION,
 interleave_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This callback function gets called by libcurl as soon as it has received interleaved RTP data. This function gets called for each $ block and therefore contains exactly one upper-layer protocol unit (e.g. one RTP packet). Curl writes the interleaved header as well as the included data for each call. The first byte is always an ASCII dollar sign. The dollar sign is followed by a one byte channel identifier and then a 2 byte integer length in network byte order. See <i>RFC2326 Section 10.12</i> for more information on how RTP interleaving behaves. If unset or set to NULL, curl will use the default write function. </p>
<p> Interleaved RTP poses some challenges for the client application. Since the stream data is sharing the RTSP control connection, it is critical to service the RTP in a timely fashion. If the RTP data is not handled quickly, subsequent response processing may become unreasonably delayed and the connection may close. The application may use <i>CURL_RTSPREQ_RECEIVE</i> to service RTP data when no requests are desired. If the application makes a request, (e.g. <i>CURL_RTSPREQ_PAUSE</i>) then the response handler will process any pending RTP data before marking the request as finished.</p>
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
