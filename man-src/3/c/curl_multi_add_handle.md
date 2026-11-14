---
title: "curl_multi_add_handle(3)"
name: "curl_multi_add_handle"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_add_handle/"
description: "curl_multi_add_handle – add an easy handle to a multi session"
---

<h2>NAME</h2>
<p> curl_multi_add_handle &#8211; add an easy handle to a multi session</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_add_handle(CURLM *multi_handle, CURL *easy_handle);</p>
<h2>DESCRIPTION</h2>
<p> Adds a standard easy handle to the multi stack. This function call will make this <i>multi_handle</i> control the specified <i>easy_handle</i>. Furthermore, libcurl now initiates the connection associated with the specified <i>easy_handle</i>. </p>
<p> When an easy handle has been added to a multi stack, you can not and you must not use <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> on that handle! </p>
<p> If the easy handle is not set to use a shared (CURLOPT_SHARE) or global DNS cache (CURLOPT_DNS_USE_GLOBAL_CACHE), it will be made to use the DNS cache that is shared between all easy handles within the multi handle when <i><a href="/docs/linux/man/3-curl_multi_add_handle/">curl_multi_add_handle</a>(3)</i> is called. </p>
<p> The easy handle will remain added until you remove it again with <i><a href="/docs/linux/man/3-curl_multi_remove_handle/">curl_multi_remove_handle</a>(3)</i>. You should remove the easy handle from the multi stack before you terminate first the easy handle and then the multi handle: </p>
<p> 1 &#8211; <i><a href="/docs/linux/man/3-curl_multi_remove_handle/">curl_multi_remove_handle</a>(3)</i> </p>
<p> 2 &#8211; <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> </p>
<p> 3 &#8211; <i><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a>(3)</i></p>
<h2>RETURN VALUE</h2>
<p> CURLMcode type, general libcurl multi interface error code.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a></code>(3),<code><a href="/docs/linux/man/3-curl_multi_init/">curl_multi_init</a></code>(3) </p>
<h2>Index</h2>
