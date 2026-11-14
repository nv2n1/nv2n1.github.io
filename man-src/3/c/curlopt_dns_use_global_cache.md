---
title: "curlopt_dns_use_global_cache(3)"
name: "curlopt_dns_use_global_cache"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_dns_use_global_cache/"
description: "CURLOPT_DNS_USE_GLOBAL_CACHE – enable/disable global DNS cache"
---

<p>CURLOPT_DNS_USE_GLOBAL_CACHE &#8211; enable/disable global DNS cache</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_DNS_USE_GLOBAL_CACHE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>long enable);</p>
<h2>Description</h2>
<p>Pass a long. If the <i>enable</i> value is 1, it tells curl to use a global DNS cache that will survive between easy handle creations and deletions. This is not thread-safe and this will use a global variable. </p>
<p> <code>WARNING:</code> this option is considered obsolete. Stop using it. Switch over to using the share interface instead! See <i><a href="/docs/linux/man/3-curlopt_share/">CURLOPT_SHARE</a>(3)</i> and <i><a href="/docs/linux/man/3-curl_share_init/">curl_share_init</a>(3)</i>.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Subject for removal in the future. Do not use!</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_share/">CURLOPT_SHARE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_dns_cache_timeout/">CURLOPT_DNS_CACHE_TIMEOUT</a></code>(3),</p>
