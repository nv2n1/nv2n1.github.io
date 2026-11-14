---
title: "curl_easy_duphandle(3)"
name: "curl_easy_duphandle"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_duphandle/"
description: "curl_easy_duphandle – Clone a libcurl session handle"
---

<h2>NAME</h2>
<p> curl_easy_duphandle &#8211; Clone a libcurl session handle</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURL *curl_easy_duphandle(CURL *handle</code><i>);</i> </p>
<h2>DESCRIPTION</h2>
<p> This function will return a new curl handle, a duplicate, using all the options previously set in the input curl <i>handle</i>. Both handles can subsequently be used independently and they must both be freed with <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i>. </p>
<p> All strings that the input handle has been told to point to (as opposed to copy) with previous calls to <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> using char * inputs, will be pointed to by the new handle as well. You must therefore make sure to keep the data around until both handles have been cleaned up. </p>
<p> The new handle will <code>not</code> inherit any state information, no connections, no SSL sessions and no cookies. </p>
<p> <code>Note</code> that even in multi-threaded programs, this function must be called in a synchronous way, the input handle may not be in use when cloned.</p>
<h2>RETURN VALUE</h2>
<p> If this function returns NULL, something went wrong and no valid handle was returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a></code>(3),<code><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a></code>(3),<code><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a></code>(3) </p>
<h2>Index</h2>
