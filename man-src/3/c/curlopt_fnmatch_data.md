---
title: "curlopt_fnmatch_data(3)"
name: "curlopt_fnmatch_data"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_fnmatch_data/"
description: "CURLOPT_FNMATCH_DATA – custom pointer to fnmatch callback"
---

<p>CURLOPT_FNMATCH_DATA &#8211; custom pointer to fnmatch callback</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FNMATCH_DATA,
 void *pointer);</pre>
<h2>Description</h2>
<p>Pass a pointer that will be untouched by libcurl and passed as the ptr argument to the <i><a href="/docs/linux/man/3-curl_fnmatch_function/">CURL_FNMATCH_FUNCTION</a>(3)</i>.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.21.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_fnmatch_function/">CURLOPT_FNMATCH_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_wildcardmatch/">CURLOPT_WILDCARDMATCH</a></code>(3),</p>
