---
title: "curlopt_random_file(3)"
name: "curlopt_random_file"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_random_file/"
description: "CURLOPT_RANDOM_FILE – specify a source for random data"
---

<p>CURLOPT_RANDOM_FILE &#8211; specify a source for random data</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_RANDOM_FILE, char *path);</p>
<h2>Description</h2>
<p>Pass a char * to a zero terminated file name. The file will be used to read from to seed the random engine for SSL and more.</p>
<h2>Default</h2>
<p>NULL, not used</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK on success or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_egdsocket/">CURLOPT_EGDSOCKET</a></code>(3),</p>
