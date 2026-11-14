---
title: "curlopt_dns_cache_timeout(3)"
name: "curlopt_dns_cache_timeout"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_dns_cache_timeout/"
description: "CURLOPT_DNS_CACHE_TIMEOUT – set life-time for DNS cache entries"
---

<p>CURLOPT_DNS_CACHE_TIMEOUT &#8211; set life-time for DNS cache entries</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_DNS_CACHE_TIMEOUT, long age);</p>
<h2>Description</h2>
<p>Pass a long, this sets the timeout in seconds. Name resolves will be kept in memory and used for this number of seconds. Set to zero to completely disable caching, or set to -1 to make the cached entries remain forever. By default, libcurl caches this info for 60 seconds. </p>
<p> The name resolve functions of various libc implementations don&#8217;t re-read name server information unless explicitly told so (for example, by calling <i><a href="/docs/linux/man/3-res_init/">res_init</a>(3)</i>). This may cause libcurl to keep using the older server even if DHCP has updated the server info, and this may look like a DNS cache issue to the casual libcurl-app user. </p>
<p> Note that DNS entries have a &quot;TTL&quot; property but libcurl doesn&#8217;t use that. This DNS cache timeout is entirely speculative that a name will resolve to the same address for a certain small amount of time into the future.</p>
<h2>Default</h2>
<p>60</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_dns_use_global_cache/">CURLOPT_DNS_USE_GLOBAL_CACHE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_dns_servers/">CURLOPT_DNS_SERVERS</a></code>(3),</p>
