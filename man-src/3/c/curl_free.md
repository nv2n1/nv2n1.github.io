---
title: "curl_free(3)"
name: "curl_free"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_free/"
description: "curl_free – reclaim memory that has been obtained through a libcurl call"
---

<h2>NAME</h2>
<p> curl_free &#8211; reclaim memory that has been obtained through a libcurl call</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>void curl_free( char *</code><i>ptr</i><code> );</code></p>
<h2>DESCRIPTION</h2>
<p> curl_free reclaims memory that has been obtained through a libcurl call. Use curl_free() instead of free() to avoid anomalies that can result from differences in memory management between your application and libcurl.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-curl_unescape/">curl_unescape</a>(3)</i> </p>
<h2>Index</h2>
