---
title: "curlopt_followlocation(3)"
name: "curlopt_followlocation"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_followlocation/"
description: "CURLOPT_FOLLOWLOCATION – follow HTTP 3xx redirects"
---

<p>CURLOPT_FOLLOWLOCATION &#8211; follow HTTP 3xx redirects</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FOLLOWLOCATION, long enable);</p>
<h2>Description</h2>
<p>A parameter set to 1 tells the library to follow any Location: header that the server sends as part of a HTTP header in a 3xx response. </p>
<p> This means that libcurl will re-send the same request on the new location and follow new Location: headers all the way until no more such headers are returned. <i><a href="/docs/linux/man/3-curlopt_maxredirs/">CURLOPT_MAXREDIRS</a>(3)</i> can be used to limit the number of redirects libcurl will follow. </p>
<p> libcurl can limit to what protocols it will automatically follow. The accepted protocols are set with <i><a href="/docs/linux/man/3-curlopt_redir_protocols/">CURLOPT_REDIR_PROTOCOLS</a>(3)</i> and it excludes the FILE protocol by default. </p>
<p> For users who think the existing location following is too naive, too simple or just lacks features, it is very easy to instead implement your own redirect follow logic with the use of <i><a href="/docs/linux/man/3-curl_easy_getinfo/">curl_easy_getinfo</a>(3)</i>&#8216;s <i>CURLINFO_REDIRECT_URL</i> option instead of using <i><a href="/docs/linux/man/3-curlopt_followlocation/">CURLOPT_FOLLOWLOCATION</a>(3)</i>.</p>
<h2>Default</h2>
<p>0, disabled</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* example.com is redirected, so we tell libcurl to follow redirection */
 curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_redir_protocols/">CURLOPT_REDIR_PROTOCOLS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_protocols/">CURLOPT_PROTOCOLS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_postredir/">CURLOPT_POSTREDIR</a></code>(3),</p>
