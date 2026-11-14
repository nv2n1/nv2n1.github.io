---
title: "curlopt_proxytype(3)"
name: "curlopt_proxytype"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_proxytype/"
description: "CURLOPT_PROXYTYPE – proxy protocol type"
---

<p>CURLOPT_PROXYTYPE &#8211; proxy protocol type</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROXYTYPE, long type);</p>
<h2>Description</h2>
<p>Pass a long with this option to set type of the proxy. Available options for this are <i>CURLPROXY_HTTP</i>, <i>CURLPROXY_HTTP_1_0</i> <i>CURLPROXY_SOCKS4</i>, <i>CURLPROXY_SOCKS5</i>, <i>CURLPROXY_SOCKS4A</i> and <i>CURLPROXY_SOCKS5_HOSTNAME</i>. The HTTP type is default. </p>
<p> If you set <code><a href="/docs/linux/man/3-curlopt_proxytype/">CURLOPT_PROXYTYPE</a>(3)</code> to <i>CURLPROXY_HTTP_1_0</i>, it will only affect how libcurl speaks to a proxy when CONNECT is used. The HTTP version used for &quot;regular&quot; HTTP requests is instead controlled with <i><a href="/docs/linux/man/3-curlopt_http_version/">CURLOPT_HTTP_VERSION</a>(3)</i>. </p>
<p> Often it is more convenient to specify the proxy type with the scheme part of the <i><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a>(3)</i> string.</p>
<h2>Default</h2>
<p>CURLPROXY_HTTP</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyport/">CURLOPT_PROXYPORT</a></code>(3),</p>
