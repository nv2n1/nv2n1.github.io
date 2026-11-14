---
title: "curlopt_buffersize(3)"
name: "curlopt_buffersize"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_buffersize/"
description: "CURLOPT_BUFFERSIZE – set preferred receive buffer size"
---

<p>CURLOPT_BUFFERSIZE &#8211; set preferred receive buffer size</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_BUFFERSIZE, long size);</p>
<h2>Description</h2>
<p>Pass a long specifying your preferred <i>size</i> (in bytes) for the receive buffer in libcurl. The main point of this would be that the write callback gets called more often and with smaller chunks. This is just treated as a request, not an order. You cannot be guaranteed to actually get the given size. </p>
<p> This size is by default set as big as possible (<i>CURL_MAX_WRITE_SIZE</i>), so it only makes sense to use this option if you want it smaller.</p>
<h2>Default</h2>
<p>CURL_MAX_WRITE_SIZE</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.10</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_max_recv_speed/">CURLOPT_MAX_RECV_SPEED</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_writefunction/">CURLOPT_WRITEFUNCTION</a></code>(3),</p>
