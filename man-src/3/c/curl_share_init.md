---
title: "curl_share_init(3)"
name: "curl_share_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_share_init/"
description: "curl_share_init – Create a shared object"
---

<h2>NAME</h2>
<p> curl_share_init &#8211; Create a shared object</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURLSH *curl_share_init( );</code></p>
<h2>DESCRIPTION</h2>
<p> This function returns a CURLSH handle to be used as input to all the other share-functions, sometimes referred to as a share handle in some places in the documentation. This init call MUST have a corresponding call to <i>curl_share_cleanup</i> when all operations using the share are complete. </p>
<p> This <i>share handle</i> is what you pass to curl using the <i>CURLOPT_SHARE</i> option with <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i>, to make that specific curl handle use the data in this share.</p>
<h2>RETURN VALUE</h2>
<p> If this function returns NULL, something went wrong (out of memory, etc.) and therefore the share object was not created.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_share_cleanup/">curl_share_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-curl_share_setopt/">curl_share_setopt</a></code>(3) </p>
<h2>Index</h2>
