---
title: "curlmopt_maxconnects(3)"
name: "curlmopt_maxconnects"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_maxconnects/"
description: "CURLMOPT_MAXCONNECTS – set size of connection cache"
---

<p>CURLMOPT_MAXCONNECTS &#8211; set size of connection cache</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_MAXCONNECTS, long max);</p>
<h2>Description</h2>
<p>Pass a long indicating the <code>max</code>. The set number will be used as the maximum amount of simultaneously open connections that libcurl may keep in its connection cache after completed use. By default libcurl will enlarge the size for each added easy handle to make it fit 4 times the number of added easy handles. </p>
<p> By setting this option, you can prevent the cache size from growing beyond the limit set by you. </p>
<p> When the cache is full, curl closes the oldest one in the cache to prevent the number of open connections from increasing. </p>
<p> This option is for the multi handle&#8217;s use only, when using the easy interface you should instead use the <i><a href="/docs/linux/man/3-curlopt_maxconnects/">CURLOPT_MAXCONNECTS</a>(3)</i> option. </p>
<p> See <i><a href="/docs/linux/man/3-curlmopt_max_total_connections/">CURLMOPT_MAX_TOTAL_CONNECTIONS</a>(3)</i> for limiting the number of active connections. </p>
<h2>Default</h2>
<p>See DESCRIPTION</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.16.3</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK if the option is supported, and CURLM_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_max_host_connections/">CURLMOPT_MAX_HOST_CONNECTIONS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_maxconnects/">CURLOPT_MAXCONNECTS</a></code>(3),</p>
