---
title: "curlopt_closesocketdata(3)"
name: "curlopt_closesocketdata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_closesocketdata/"
description: "CURLOPT_CLOSESOCKETDATA – pointer passed to the socket close callback"
---

<p>CURLOPT_CLOSESOCKETDATA &#8211; pointer passed to the socket close callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CLOSESOCKETDATA, void *pointer);</p>
<h2>Description</h2>
<p>Pass a <i>pointer</i> that will be untouched by libcurl and passed as the first argument in the closesocket callback set with <i><a href="/docs/linux/man/3-curlopt_closesocketfunction/">CURLOPT_CLOSESOCKETFUNCTION</a>(3)</i>.</p>
<h2>Default</h2>
<p>The default value of this parameter is NULL.</p>
<h2>Protocols</h2>
<p>All except file:</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.21.7</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_closesocketfunction/">CURLOPT_CLOSESOCKETFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_opensocketfunction/">CURLOPT_OPENSOCKETFUNCTION</a></code>(3),</p>
