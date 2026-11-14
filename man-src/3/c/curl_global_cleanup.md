---
title: "curl_global_cleanup(3)"
name: "curl_global_cleanup"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_global_cleanup/"
description: "curl_global_cleanup – global libcurl cleanup"
---

<h2>NAME</h2>
<p> curl_global_cleanup &#8211; global libcurl cleanup</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>void curl_global_cleanup(void);</code></p>
<h2>DESCRIPTION</h2>
<p> This function releases resources acquired by <code><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</code>. </p>
<p> You should call <i><a href="/docs/linux/man/3-curl_global_cleanup/">curl_global_cleanup</a>(3)</i> once for each call you make to <i><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</i>, after you are done using libcurl. </p>
<p> <code>This function is not thread safe.</code> You must not call it when any other thread in the program (i.e. a thread sharing the same memory) is running. This doesn&#8217;t just mean no other thread that is using libcurl. Because <code><a href="/docs/linux/man/3-curl_global_cleanup/">curl_global_cleanup</a>(3)</code> calls functions of other libraries that are similarly thread unsafe, it could conflict with any other thread that uses these other libraries. </p>
<p> See the description in <code><a href="/docs/linux/man/3-libcurl/">libcurl</a>(3)</code> of global environment requirements for details of how to use this function. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a></code>(3), <code><a href="/docs/linux/man/3-libcurl/">libcurl</a></code>(3), </p>
<h2>Index</h2>
