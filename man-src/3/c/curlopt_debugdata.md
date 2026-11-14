---
title: "curlopt_debugdata(3)"
name: "curlopt_debugdata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_debugdata/"
description: "CURLOPT_DEBUGDATA – custom pointer for debug callback"
---

<p>CURLOPT_DEBUGDATA &#8211; custom pointer for debug callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_DEBUGDATA, void *pointer);</p>
<h2>Description</h2>
<p>Pass a <i>pointer</i> to whatever you want passed in to your <i><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a>(3)</i> in the last void * argument. This pointer is not used by libcurl, it is only passed to the callback.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p><a rel="nofollow" href="http://curl.haxx.se/libcurl/c/debug.html">http://curl.haxx.se/libcurl/c/debug.html</a></p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_stderr/">CURLOPT_STDERR</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a></code>(3),</p>
