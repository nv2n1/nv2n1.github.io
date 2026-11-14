---
title: "curl_easy_init(3)"
name: "curl_easy_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_init/"
description: "curl_easy_init – Start a libcurl easy session"
---

<h2>NAME</h2>
<p> curl_easy_init &#8211; Start a libcurl easy session</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURL *curl_easy_init( );</code> </p>
<h2>DESCRIPTION</h2>
<p> This function must be the first function to call, and it returns a CURL easy handle that you must use as input to other easy-functions. curl_easy_init initializes curl and this call <code>MUST</code> have a corresponding call to <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> when the operation is complete. </p>
<p> If you did not already call <i><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</i>, <i><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a>(3)</i> does it automatically. This may be lethal in multi-threaded cases, since <i><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</i> is not thread-safe, and it may result in resource problems because there is no corresponding cleanup. </p>
<p> You are strongly advised to not allow this automatic behaviour, by calling <i><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</i> yourself properly. See the description in <code><a href="/docs/linux/man/3-libcurl/">libcurl</a></code>(3) of global environment requirements for details of how to use this function. </p>
<h2>RETURN VALUE</h2>
<p> If this function returns NULL, something went wrong and you cannot use the other curl functions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_reset/">curl_easy_reset</a></code>(3) </p>
<h2>Index</h2>
