---
title: "libcurl-share(3)"
name: "libcurl-share"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libcurl-share/"
description: "libcurl-share – how to use the share interface"
---

<h2>NAME</h2>
<p> libcurl-share &#8211; how to use the share interface</p>
<h2>DESCRIPTION</h2>
<p> This is an overview on how to use the libcurl share interface in your C programs. There are specific man pages for each function mentioned in here. </p>
<p> All functions in the share interface are prefixed with curl_share. </p>
<h2>OBJECTIVES</h2>
<p> The share interface was added to enable sharing of data between curl &quot;handles&quot;.</p>
<h2>ONE SET OF DATA &#8211; MANY TRANSFERS</h2>
<p> You can have multiple easy handles share data between them. Have them update and use the <code>same</code> cookie database or DNS cache! This way, each single transfer will take advantage from data updates made by the other transfer(s).</p>
<h2>SHARE OBJECT</h2>
<p> You create a shared object with <i><a href="/docs/linux/man/3-curl_share_init/">curl_share_init</a>(3)</i>. It returns a handle for a newly created one. </p>
<p> You tell the shared object what data you want it to share by using <i><a href="/docs/linux/man/3-curl_share_setopt/">curl_share_setopt</a>(3)</i>. </p>
<p> Since you can use this share from multiple threads, and libcurl has no internal thread synchronization, you must provide mutex callbacks if you&#8217;re using this multi-threaded. You set lock and unlock functions with <i><a href="/docs/linux/man/3-curl_share_setopt/">curl_share_setopt</a>(3)</i> too. </p>
<p> Then, you make an easy handle to use this share, you set the <i>CURLOPT_SHARE</i> option with <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i>, and pass in share handle. You can make any number of easy handles share the same share handle. </p>
<p> To make an easy handle stop using that particular share, you set <i>CURLOPT_SHARE</i> to NULL for that easy handle. To make a handle stop sharing a particular data, you can <i>CURLSHOPT_UNSHARE</i> it. </p>
<p> When you&#8217;re done using the share, make sure that no easy handle is still using it, and call <i><a href="/docs/linux/man/3-curl_share_cleanup/">curl_share_cleanup</a>(3)</i> on the handle.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_share_init/">curl_share_init</a></code>(3), <code><a href="/docs/linux/man/3-curl_share_setopt/">curl_share_setopt</a></code>(3), <code><a href="/docs/linux/man/3-curl_share_cleanup/">curl_share_cleanup</a></code>(3) </p>
<h2>Index</h2>
