---
title: "curl_multi_strerror(3)"
name: "curl_multi_strerror"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_strerror/"
description: "curl_multi_strerror – return string describing error code"
---

<h2>NAME</h2>
<p> curl_multi_strerror &#8211; return string describing error code</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;curl/curl.h&gt;
const char *curl_multi_strerror(CURLMcode errornum);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The curl_multi_strerror() function returns a string describing the CURLMcode error code passed in the argument <i>errornum</i>.</p>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.12.0</p>
<h2>RETURN VALUE</h2>
<p> A pointer to a zero terminated string.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libcurl-errors/">libcurl-errors</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_strerror/">curl_easy_strerror</a></code>(3), <code><a href="/docs/linux/man/3-curl_share_strerror/">curl_share_strerror</a></code>(3) </p>
<h2>Index</h2>
