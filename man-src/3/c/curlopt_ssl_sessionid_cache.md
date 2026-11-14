---
title: "curlopt_ssl_sessionid_cache(3)"
name: "curlopt_ssl_sessionid_cache"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssl_sessionid_cache/"
description: "CURLOPT_SSL_SESSIONID_CACHE – enable/disable use of the SSL session-ID cache"
---

<p>CURLOPT_SSL_SESSIONID_CACHE &#8211; enable/disable use of the SSL session-ID cache</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSL_SESSIONID_CACHE,
 long enabled);</pre>
<h2>Description</h2>
<p>Pass a long set to 0 to disable libcurl&#8217;s use of SSL session-ID caching. Set this to 1 to enable it. By default all transfers are done using the cache enabled. While nothing ever should get hurt by attempting to reuse SSL session-IDs, there seem to be or have been broken SSL implementations in the wild that may require you to disable this in order for you to succeed.</p>
<h2>Default</h2>
<p>1</p>
<h2>Protocols</h2>
<p>All TLS-based</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.16.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_dns_cache_timeout/">CURLOPT_DNS_CACHE_TIMEOUT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_sslversion/">CURLOPT_SSLVERSION</a></code>(3),</p>
