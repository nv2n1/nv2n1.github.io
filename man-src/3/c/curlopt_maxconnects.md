---
title: "curlopt_maxconnects(3)"
name: "curlopt_maxconnects"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_maxconnects/"
description: "CURLOPT_MAXCONNECTS – maximum connection cache size"
---

<p>CURLOPT_MAXCONNECTS &#8211; maximum connection cache size</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_MAXCONNECTS, long amount);</p>
<h2>Description</h2>
<p>Pass a long. The set <i>amount</i> will be the maximum number of simultaneously open persistent connections that libcurl may cache in the pool associated with this handle. The default is 5, and there isn&#8217;t much point in changing this value unless you are perfectly aware of how this works and changes libcurl&#8217;s behaviour. This concerns connections using any of the protocols that support persistent connections. </p>
<p> When reaching the maximum limit, curl closes the oldest one in the cache to prevent increasing the number of open connections. </p>
<p> If you already have performed transfers with this curl handle, setting a smaller <i><a href="/docs/linux/man/3-curlopt_maxconnects/">CURLOPT_MAXCONNECTS</a>(3)</i> than before may cause open connections to get closed unnecessarily. </p>
<p> If you add this easy handle to a multi handle, this setting is not acknowledged, and you must instead use <i><a href="/docs/linux/man/3-curl_multi_setopt/">curl_multi_setopt</a>(3)</i> and the <i>CURLMOPT_MAXCONNECTS</i> option.</p>
<h2>Default</h2>
<p>5</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_maxconnects/">CURLMOPT_MAXCONNECTS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_maxredirs/">CURLOPT_MAXREDIRS</a></code>(3),</p>
