---
title: "curl_easy_perform(3)"
name: "curl_easy_perform"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_perform/"
description: "curl_easy_perform – Perform a file transfer"
---

<h2>NAME</h2>
<p> curl_easy_perform &#8211; Perform a file transfer</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURLcode curl_easy_perform(CURL *</code><i>handle</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> This function is called after the init and all the <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> calls are made, and will perform the transfer as described in the options. It must be called with the same <i>handle</i> as input as the curl_easy_init call returned. </p>
<p> You can do any amount of calls to <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> while using the same handle. If you intend to transfer more than one file, you are even encouraged to do so. libcurl will then attempt to re-use the same connection for the following transfers, thus making the operations faster, less CPU intense and using less network resources. Just note that you will have to use <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> between the invokes to set options for the following curl_easy_perform. </p>
<p> You must never call this function simultaneously from two places using the same handle. Let the function return first before invoking it another time. If you want parallel transfers, you must use several curl handles.</p>
<h2>RETURN VALUE</h2>
<p> 0 means everything was ok, non-zero means an error occurred as <i>&lt;curl/curl.h&gt;</i> defines. If the CURLOPT_ERRORBUFFER was set with <i>curl_easy_setopt</i> there will be a readable error message in the error buffer when non-zero is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a></code>(3), </p>
<h2>Index</h2>
