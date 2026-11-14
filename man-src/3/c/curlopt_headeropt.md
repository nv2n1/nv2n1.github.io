---
title: "curlopt_headeropt(3)"
name: "curlopt_headeropt"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_headeropt/"
description: "CURLOPT_HEADEROPT – set how to send HTTP headers"
---

<p>CURLOPT_HEADEROPT &#8211; set how to send HTTP headers</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HEADEROPT, long bitmask);</p>
<h2>Description</h2>
<p>Pass a long that is a bitmask of options of how to deal with headers. The two mutually exclusive options are: </p>
<p> <code>CURLHEADER_UNIFIED</code> &#8211; keep working as before. This means <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i> headers will be used in requests both to servers and proxies. With this option enabled, <i><a href="/docs/linux/man/3-curlopt_proxyheader/">CURLOPT_PROXYHEADER</a>(3)</i> will not have any effect. </p>
<p> <code>CURLHEADER_SEPARATE</code> &#8211; makes <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i> headers only get sent to a server and not to a proxy. Proxy headers must be set with <i><a href="/docs/linux/man/3-curlopt_proxyheader/">CURLOPT_PROXYHEADER</a>(3)</i> to get used. Note that if a non-CONNECT request is sent to a proxy, libcurl will send both server headers and proxy headers. When doing CONNECT, libcurl will send <i><a href="/docs/linux/man/3-curlopt_proxyheader/">CURLOPT_PROXYHEADER</a>(3)</i> headers only to the proxy and then <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i> headers only to the server.</p>
<h2>Default</h2>
<p>CURLHEADER_UNIFIED</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.37.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyheader/">CURLOPT_PROXYHEADER</a></code>(3),</p>
