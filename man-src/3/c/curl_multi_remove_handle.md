---
title: "curl_multi_remove_handle(3)"
name: "curl_multi_remove_handle"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_remove_handle/"
description: "curl_multi_remove_handle – remove an easy handle from a multi session"
---

<h2>NAME</h2>
<p> curl_multi_remove_handle &#8211; remove an easy handle from a multi session</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_remove_handle(CURLM *multi_handle, CURL *easy_handle);</p>
<h2>DESCRIPTION</h2>
<p> Removes a given easy_handle from the multi_handle. This will make the specified easy handle be removed from this multi handle&#8217;s control. </p>
<p> When the easy handle has been removed from a multi stack, it is again perfectly legal to invoke <i>curl_easy_perform()</i> on this easy handle. </p>
<p> Removing an easy handle while being used, will effectively halt the transfer in progress involving that easy handle. All other easy handles and transfers will remain unaffected.</p>
<h2>RETURN VALUE</h2>
<p> CURLMcode type, general libcurl multi interface error code.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a></code>(3),<code><a href="/docs/linux/man/3-curl_multi_init/">curl_multi_init</a></code>(3) </p>
<h2>Index</h2>
