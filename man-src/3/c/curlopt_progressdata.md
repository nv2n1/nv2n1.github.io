---
title: "curlopt_progressdata(3)"
name: "curlopt_progressdata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_progressdata/"
description: "CURLOPT_PROGRESSDATA – custom pointer passed to the progress callback"
---

<p>CURLOPT_PROGRESSDATA &#8211; custom pointer passed to the progress callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROGRESSDATA, void *pointer);</p>
<h2>Description</h2>
<p>Pass a <i>pointer</i> that will be untouched by libcurl and passed as the first argument in the progress callback set with <i><a href="/docs/linux/man/3-curlopt_progressfunction/">CURLOPT_PROGRESSFUNCTION</a>(3)</i>.</p>
<h2>Default</h2>
<p>The default value of this parameter is NULL.</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p><a rel="nofollow" href="http://curl.haxx.se/libcurl/c/progressfunc.html">http://curl.haxx.se/libcurl/c/progressfunc.html</a></p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_progressfunction/">CURLOPT_PROGRESSFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_xferinfofunction/">CURLOPT_XFERINFOFUNCTION</a></code>(3),</p>
