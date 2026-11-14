---
title: "curl_multi_init(3)"
name: "curl_multi_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_init/"
description: "curl_multi_init – create a multi handle"
---

<h2>NAME</h2>
<p> curl_multi_init &#8211; create a multi handle</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURLM *curl_multi_init( );</code></p>
<h2>DESCRIPTION</h2>
<p> This function returns a CURLM handle to be used as input to all the other multi-functions, sometimes referred to as a multi handle in some places in the documentation. This init call MUST have a corresponding call to <i><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a>(3)</i> when the operation is complete.</p>
<h2>RETURN VALUE</h2>
<p> If this function returns NULL, something went wrong and you cannot use the other curl functions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a></code>(3),<code><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a></code>(3),<code><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a></code>(3) </p>
<h2>Index</h2>
