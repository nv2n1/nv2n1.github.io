---
title: "curlopt_proxy_transfer_mode(3)"
name: "curlopt_proxy_transfer_mode"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_proxy_transfer_mode/"
description: "CURLOPT_PROXY_TRANSFER_MODE – append FTP transfer mode to URL for proxy"
---

<p>CURLOPT_PROXY_TRANSFER_MODE &#8211; append FTP transfer mode to URL for proxy</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROXY_TRANSFER_MODE, long enabled);</p>
<h2>Description</h2>
<p>Pass a long. If the value is set to 1 (one), it tells libcurl to set the transfer mode (binary or ASCII) for FTP transfers done via a HTTP proxy, by appending ;type=a or ;type=i to the URL. Without this setting, or it being set to 0 (zero, the default), <i><a href="/docs/linux/man/3-curlopt_transfertext/">CURLOPT_TRANSFERTEXT</a>(3)</i> has no effect when doing FTP via a proxy. Beware that not all proxies support this feature.</p>
<h2>Default</h2>
<p>0, disabled</p>
<h2>Protocols</h2>
<p>FTP over proxy</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.18.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if the enabled value is not supported.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpproxytunnel/">CURLOPT_HTTPPROXYTUNNEL</a></code>(3),</p>
