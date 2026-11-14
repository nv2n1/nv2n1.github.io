---
title: "curlopt_postfieldsize_large(3)"
name: "curlopt_postfieldsize_large"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_postfieldsize_large/"
description: "CURLOPT_POSTFIELDSIZE_LARGE – size of POST data pointed to"
---

<p>CURLOPT_POSTFIELDSIZE_LARGE &#8211; size of POST data pointed to</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_POSTFIELDSIZE_LARGE,
 curl_off_t size);</pre>
<h2>Description</h2>
<p>If you want to post data to the server without having libcurl do a strlen() to measure the data size, this option must be used. When this option is used you can post fully binary data, which otherwise is likely to fail. If this size is set to -1, the library will use strlen() to get the size.</p>
<h2>Default</h2>
<p>-1</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 const char *data = large_chunk;
 curl_off_t length_of_data; /* set somehow */
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* size of the POST data */
 curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE_LARGE, length_of_data);
 curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_copypostfields/">CURLOPT_COPYPOSTFIELDS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_postfieldsize/">CURLOPT_POSTFIELDSIZE</a></code>(3),</p>
