---
title: "curlopt_referer(3)"
name: "curlopt_referer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_referer/"
description: "CURLOPT_REFERER – set the HTTP referer header"
---

<p>CURLOPT_REFERER &#8211; set the HTTP referer header</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_REFERER, char *where);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. It will be used to set the Referer: header in the http request sent to the remote server. This can be used to fool servers or scripts. You can also set any custom header with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i>.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built with HTTP support</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP support is enabled, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_useragent/">CURLOPT_USERAGENT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a></code>(3),</p>
