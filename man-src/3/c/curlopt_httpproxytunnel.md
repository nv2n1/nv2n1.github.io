---
title: "curlopt_httpproxytunnel(3)"
name: "curlopt_httpproxytunnel"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_httpproxytunnel/"
description: "CURLOPT_HTTPPROXYTUNNEL – tunnel through HTTP proxy"
---

<p>CURLOPT_HTTPPROXYTUNNEL &#8211; tunnel through HTTP proxy</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HTTPPROXYTUNNEL, long tunnel);</p>
<h2>Description</h2>
<p>Set the parameter to 1 to make libcurl tunnel all operations through the HTTP proxy. There is a big difference between using a proxy and to tunnel through it. If you don&#8217;t know what this means, you probably don&#8217;t want this tunneling option. </p>
<p> Tunneling essentially means that a CONNECT is sent to the proxy, asking it to connect to a remote host on a specific port number and then the traffic is just passed through the proxy. Proxies tend to whitelist specific port numbers it allows CONNECT requests to and often only port 80 and 443 are allowed.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>All network protocols</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a></code>(3),</p>
