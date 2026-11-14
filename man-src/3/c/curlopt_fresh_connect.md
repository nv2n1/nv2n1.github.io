---
title: "curlopt_fresh_connect(3)"
name: "curlopt_fresh_connect"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_fresh_connect/"
description: "CURLOPT_FRESH_CONNECT – force a new connection to be used"
---

<p>CURLOPT_FRESH_CONNECT &#8211; force a new connection to be used</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FRESH_CONNECT, long fresh);</p>
<h2>Description</h2>
<p>Pass a long. Set to 1 to make the next transfer use a new (fresh) connection by force instead of trying to re-use an existing one. This option should be used with caution and only if you understand what it does as it may seriously impact performance. </p>
<p> Related functionality is <i><a href="/docs/linux/man/3-curlopt_forbid_reuse/">CURLOPT_FORBID_REUSE</a>(3)</i> which makes sure the connection is closed after use so that it won&#8217;t be re-used. </p>
<p> Set <i>fresh</i> to 0 to have libcurl attempt re-using an existing connection (default behavior).</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_forbid_reuse/">CURLOPT_FORBID_REUSE</a></code>(3),</p>
