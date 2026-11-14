---
title: "curlopt_useragent(3)"
name: "curlopt_useragent"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_useragent/"
description: "CURLOPT_USERAGENT – set HTTP user-agent header"
---

<p>CURLOPT_USERAGENT &#8211; set HTTP user-agent header</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_USERAGENT, char *ua);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. It will be used to set the User-Agent: header in the HTTP request sent to the remote server. This can be used to fool servers or scripts. You can also set any custom header with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i>.</p>
<h2>Default</h2>
<p>NULL, no User-Agent: header is used by default.</p>
<h2>Protocols</h2>
<p>HTTP, HTTPS</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>As long as HTTP is supported</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_referer/">CURLOPT_REFERER</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a></code>(3),</p>
