---
title: "curl_easy_reset(3)"
name: "curl_easy_reset"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_reset/"
description: "curl_easy_reset – reset all options of a libcurl session handle"
---

<h2>NAME</h2>
<p> curl_easy_reset &#8211; reset all options of a libcurl session handle</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>void curl_easy_reset(CURL *handle</code><i>);</i> </p>
<h2>DESCRIPTION</h2>
<p> Re-initializes all options previously set on a specified CURL handle to the default values. This puts back the handle to the same state as it was in when it was just created with <i><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a>(3)</i>. </p>
<p> It does not change the following information kept in the handle: live connections, the Session ID cache, the DNS cache, the cookies and shares.</p>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.12.1</p>
<h2>RETURN VALUE</h2>
<p> Nothing</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a></code>(3),<code><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a></code>(3),<code><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a></code>(3) </p>
<h2>Index</h2>
