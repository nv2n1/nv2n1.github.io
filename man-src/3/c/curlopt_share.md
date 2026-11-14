---
title: "curlopt_share(3)"
name: "curlopt_share"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_share/"
description: "CURLOPT_SHARE – specify share handle to use"
---

<p>CURLOPT_SHARE &#8211; specify share handle to use</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SHARE, CURLSH *share);</p>
<h2>Description</h2>
<p>Pass a <i>share</i> handle as a parameter. The share handle must have been created by a previous call to <i><a href="/docs/linux/man/3-curl_share_init/">curl_share_init</a>(3)</i>. Setting this option, will make this curl handle use the data from the shared handle instead of keeping the data to itself. This enables several curl handles to share data. If the curl handles are used simultaneously in multiple threads, you <code>MUST</code> use the locking methods in the share handle. See <i><a href="/docs/linux/man/3-curl_share_setopt/">curl_share_setopt</a>(3)</i> for details. </p>
<p> If you add a share that is set to share cookies, your easy handle will use that cookie cache and get the cookie engine enabled. If you unshare an object that was using cookies (or change to another object that doesn&#8217;t share cookies), the easy handle will get its cookie engine disabled. </p>
<p> Data that the share object is not set to share will be dealt with the usual way, as if no share was used. </p>
<p> Set this option to NULL again to stop using that share object.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_cookie/">CURLOPT_COOKIE</a></code>(3),</p>
