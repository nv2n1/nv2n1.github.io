---
title: "curlopt_noprogress(3)"
name: "curlopt_noprogress"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_noprogress/"
description: "CURLOPT_NOPROGRESS – switch off the progress meter"
---

<p>CURLOPT_NOPROGRESS &#8211; switch off the progress meter</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_NOPROGRESS, long onoff);</p>
<h2>Description</h2>
<p>If <i>onoff</i> is to 1, it tells the library to shut off the progress meter completely for requests done with this <i>handle</i>. It will also prevent the <i><a href="/docs/linux/man/3-curlopt_progressfunction/">CURLOPT_PROGRESSFUNCTION</a>(3)</i> from getting called. </p>
<p> Future versions of libcurl are likely to not have any built-in progress meter at all.</p>
<h2>Default</h2>
<p>1, meaning it normally runs without a progress meter.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_progressfunction/">CURLOPT_PROGRESSFUNCTION</a></code>(3),</p>
