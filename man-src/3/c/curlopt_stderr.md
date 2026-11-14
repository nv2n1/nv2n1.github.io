---
title: "curlopt_stderr(3)"
name: "curlopt_stderr"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_stderr/"
description: "CURLOPT_STDERR – redirect stderr to another stream"
---

<p>CURLOPT_STDERR &#8211; redirect stderr to another stream</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_STDERR, FILE *stream);</p>
<h2>Description</h2>
<p>Pass a FILE * as parameter. Tell libcurl to use this <i>stream</i> instead of stderr when showing the progress meter and displaying <i><a href="/docs/linux/man/3-curlopt_verbose/">CURLOPT_VERBOSE</a>(3)</i> data.</p>
<h2>Default</h2>
<p>stderr</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_verbose/">CURLOPT_VERBOSE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_noprogress/">CURLOPT_NOPROGRESS</a></code>(3),</p>
