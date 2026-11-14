---
title: "curlopt_post(3)"
name: "curlopt_post"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_post/"
description: "CURLOPT_POST – request a HTTP POST"
---

<p>CURLOPT_POST &#8211; request a HTTP POST</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_POST, long post);</p>
<h2>Description</h2>
<p>A parameter set to 1 tells libcurl to do a regular HTTP post. This will also make the library use a &quot;Content-Type: application/x-www-form-urlencoded&quot; header. (This is by far the most commonly used POST method). </p>
<p> Use one of <i><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_copypostfields/">CURLOPT_COPYPOSTFIELDS</a>(3)</i> options to specify what data to post and <i><a href="/docs/linux/man/3-curlopt_postfieldsize/">CURLOPT_POSTFIELDSIZE</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_postfieldsize_large/">CURLOPT_POSTFIELDSIZE_LARGE</a>(3)</i> to set the data size. </p>
<p> Optionally, you can provide data to POST using the <i><a href="/docs/linux/man/3-curlopt_readfunction/">CURLOPT_READFUNCTION</a>(3)</i> and <i><a href="/docs/linux/man/3-curlopt_readdata/">CURLOPT_READDATA</a>(3)</i> options but then you must make sure to not set <i><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a>(3)</i> to anything but NULL. When providing data with a callback, you must transmit it using chunked transfer-encoding or you must set the size of the data with the <i><a href="/docs/linux/man/3-curlopt_postfieldsize/">CURLOPT_POSTFIELDSIZE</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_postfieldsize_large/">CURLOPT_POSTFIELDSIZE_LARGE</a>(3)</i> options. To enable chunked encoding, you simply pass in the appropriate Transfer-Encoding header, see the post-callback.c example. </p>
<p> You can override the default POST Content-Type: header by setting your own with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i>. </p>
<p> Using POST with HTTP 1.1 implies the use of a &quot;Expect: 100-continue&quot; header. You can disable this header with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i> as usual. </p>
<p> If you use POST to a HTTP 1.1 server, you can send data without knowing the size before starting the POST if you use chunked encoding. You enable this by adding a header like &quot;Transfer-Encoding: chunked&quot; with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i>. With HTTP 1.0 or without chunked transfer, you must specify the size in the request. </p>
<p> When setting <i><a href="/docs/linux/man/3-curlopt_post/">CURLOPT_POST</a>(3)</i> to 1, it will automatically set <i><a href="/docs/linux/man/3-curlopt_nobody/">CURLOPT_NOBODY</a>(3)</i> to 0. </p>
<p> If you issue a POST request and then want to make a HEAD or GET using the same re-used handle, you must explicitly set the new request type using <i><a href="/docs/linux/man/3-curlopt_nobody/">CURLOPT_NOBODY</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_httpget/">CURLOPT_HTTPGET</a>(3)</i> or similar.</p>
<h2>Default</h2>
<p>0, disabled</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httppost/">CURLOPT_HTTPPOST</a></code>(3),</p>
