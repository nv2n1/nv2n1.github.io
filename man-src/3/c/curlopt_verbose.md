---
title: "curlopt_verbose(3)"
name: "curlopt_verbose"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_verbose/"
description: "CURLOPT_VERBOSE – set verbose mode on/off"
---

<p>CURLOPT_VERBOSE &#8211; set verbose mode on/off</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_VERBOSE, long onoff);</p>
<h2>Description</h2>
<p>Set the <i>onoff</i> parameter to 1 to make the library display a lot of verbose information about its operations on this <i>handle</i>. Very useful for libcurl and/or protocol debugging and understanding. The verbose information will be sent to stderr, or the stream set with <i><a href="/docs/linux/man/3-curlopt_stderr/">CURLOPT_STDERR</a>(3)</i>. </p>
<p> You hardly ever want this set in production use, you will almost always want this when you debug/report problems. </p>
<p> To also get all the protocol data sent and received, consider using the <i><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a>(3)</i>.</p>
<h2>Default</h2>
<p>0, meaning disabled.</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* ask libcurl to show us the verbose output */
 curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_stderr/">CURLOPT_STDERR</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a></code>(3),</p>
