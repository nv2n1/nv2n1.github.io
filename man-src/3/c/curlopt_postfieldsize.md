---
title: "curlopt_postfieldsize(3)"
name: "curlopt_postfieldsize"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_postfieldsize/"
description: "CURLOPT_POSTFIELDSIZE – size of POST data pointed to"
---

<p>CURLOPT_POSTFIELDSIZE &#8211; size of POST data pointed to</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_POSTFIELDSIZE, long size);</p>
<h2>Description</h2>
<p>If you want to post data to the server without having libcurl do a strlen() to measure the data size, this option must be used. When this option is used you can post fully binary data, which otherwise is likely to fail. If this size is set to -1, the library will use strlen() to get the size. </p>
<p> If you post more than 2GB, use <i><a href="/docs/linux/man/3-curlopt_postfieldsize_large/">CURLOPT_POSTFIELDSIZE_LARGE</a>(3)</i>.</p>
<h2>Default</h2>
<p>-1</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 const char *data = &quot;data to send&quot;;
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* size of the POST data */
 curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, (long) strlen(data));
 curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_postfieldsize_large/">CURLOPT_POSTFIELDSIZE_LARGE</a></code>(3),</p>
