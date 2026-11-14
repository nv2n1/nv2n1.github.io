---
title: "curl_share_strerror(3)"
name: "curl_share_strerror"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_share_strerror/"
description: "curl_share_strerror – return string describing error code"
---

<h2>NAME</h2>
<p> curl_share_strerror &#8211; return string describing error code</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;curl/curl.h&gt;
const char *curl_share_strerror(CURLSHcode errornum);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The curl_share_strerror() function returns a string describing the CURLSHcode error code passed in the argument <i>errornum</i>.</p>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.12.0</p>
<h2>RETURN VALUE</h2>
<p> A pointer to a zero terminated string.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libcurl-errors/">libcurl-errors</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_strerror/">curl_multi_strerror</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_strerror/">curl_easy_strerror</a></code>(3) </p>
<h2>Index</h2>
