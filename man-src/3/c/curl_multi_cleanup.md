---
title: "curl_multi_cleanup(3)"
name: "curl_multi_cleanup"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_cleanup/"
description: "curl_multi_cleanup – close down a multi session"
---

<h2>NAME</h2>
<p> curl_multi_cleanup &#8211; close down a multi session</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURLMcode curl_multi_cleanup( CURLM *multi_handle );</code></p>
<h2>DESCRIPTION</h2>
<p> Cleans up and removes a whole multi stack. It does not free or touch any individual easy handles in any way &#8211; they still need to be closed individually, using the usual <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> way. The order of cleaning up should be: </p>
<p> 1 &#8211; <i><a href="/docs/linux/man/3-curl_multi_remove_handle/">curl_multi_remove_handle</a>(3)</i> before any easy handles are cleaned up </p>
<p> 2 &#8211; <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> can now be called independently since the easy handle is no longer connected to the multi handle </p>
<p> 3 &#8211; <i><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a>(3)</i> should be called when all easy handles are removed</p>
<h2>RETURN VALUE</h2>
<p> CURLMcode type, general libcurl multi interface error code.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_init/">curl_multi_init</a></code>(3),<code><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a></code>(3),<code><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a></code>(3) </p>
<h2>Index</h2>
