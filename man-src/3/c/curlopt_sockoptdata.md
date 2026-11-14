---
title: "curlopt_sockoptdata(3)"
name: "curlopt_sockoptdata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_sockoptdata/"
description: "CURLOPT_SOCKOPTDATA – custom pointer to pass to sockopt callback"
---

<p>CURLOPT_SOCKOPTDATA &#8211; custom pointer to pass to sockopt callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SOCKOPTDATA, void *pointer);</p>
<h2>Description</h2>
<p>Pass a <i>pointer</i> that will be untouched by libcurl and passed as the first argument in the sockopt callback set with <i><a href="/docs/linux/man/3-curlopt_sockoptfunction/">CURLOPT_SOCKOPTFUNCTION</a>(3)</i>.</p>
<h2>Default</h2>
<p>The default value of this parameter is NULL.</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.16.0</p>
<h2>Return Value</h2>
<p>Returns <i>CURLE_OK</i> if the option is supported, and <i>CURLE_UNKNOWN_OPTION</i> if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sockoptfunction/">CURLOPT_SOCKOPTFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_opensocketfunction/">CURLOPT_OPENSOCKETFUNCTION</a></code>(3),</p>
