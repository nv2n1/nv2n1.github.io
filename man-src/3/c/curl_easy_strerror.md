---
title: "curl_easy_strerror(3)"
name: "curl_easy_strerror"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_strerror/"
description: "curl_easy_strerror – return string describing error code"
---

<h2>NAME</h2>
<p> curl_easy_strerror &#8211; return string describing error code</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;curl/curl.h&gt; </p>
<p> const char *curl_easy_strerror(CURLcode errornum);</p>
<h2>DESCRIPTION</h2>
<p> The curl_easy_strerror() function returns a string describing the CURLcode error code passed in the argument <i>errornum</i>.</p>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.12.0</p>
<h2>RETURN VALUE</h2>
<p> A pointer to a zero terminated string.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libcurl-errors/">libcurl-errors</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_strerror/">curl_multi_strerror</a></code>(3), <code><a href="/docs/linux/man/3-curl_share_strerror/">curl_share_strerror</a></code>(3) </p>
<h2>Index</h2>
