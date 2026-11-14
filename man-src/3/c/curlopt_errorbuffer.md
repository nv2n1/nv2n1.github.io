---
title: "curlopt_errorbuffer(3)"
name: "curlopt_errorbuffer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_errorbuffer/"
description: "CURLOPT_ERRORBUFFER – set error buffer for error messages"
---

<p>CURLOPT_ERRORBUFFER &#8211; set error buffer for error messages</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_ERRORBUFFER, char *buf);</p>
<h2>Description</h2>
<p>Pass a char * to a buffer that the libcurl may store human readable error messages in on failures or problems. This may be more helpful than just the return code from <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> and related functions. The buffer <code>must be at least CURL_ERROR_SIZE bytes big</code>. </p>
<p> You must keep the associated buffer available until libcurl no longer needs it. Failing to do so will cause very odd behavior or even crashes. libcurl will need it until you call <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> or you set the same option again to use a different pointer. </p>
<p> Consider <i><a href="/docs/linux/man/3-curlopt_verbose/">CURLOPT_VERBOSE</a>(3)</i> and <i><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a>(3)</i> to better debug and trace why errors happen. </p>
<p> If the library does not return an error, the buffer may not have been touched. Do not rely on the contents in those cases.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<pre>curl = curl_easy_init();
if(curl) {
 char error[CURL_ERROR_SIZE]
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* provide a buffer to store errors in */
 curl_easy_setopt(curl, CURLOPT_ERRORBUFFER, error);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_verbose/">CURLOPT_VERBOSE</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_strerror/">curl_easy_strerror</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_strerror/">curl_multi_strerror</a></code>(3), <code><a href="/docs/linux/man/3-curl_share_strerror/">curl_share_strerror</a></code>(3)</p>
